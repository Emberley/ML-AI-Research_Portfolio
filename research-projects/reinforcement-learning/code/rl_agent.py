"""
rl_agent.py
-----------
A tabular Q-learning agent that learns to navigate a simple grid-world
environment.

Usage
-----
    python rl_agent.py

Results (rewards array, Q-table, and a training-curve plot) are saved to the
sibling ``results/`` directory.
"""

from __future__ import annotations

import os
import random
from pathlib import Path
from typing import Optional

import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
RESULTS_DIR = Path(__file__).parent.parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------
class GridWorld:
    """A simple N×N grid-world with a single goal state.

    States  : integer index  row * cols + col
    Actions : 0=UP, 1=DOWN, 2=LEFT, 3=RIGHT
    Reward  : +1 on reaching the goal, -0.01 step penalty elsewhere.
    """

    ACTION_DELTAS = {
        0: (-1, 0),  # UP
        1: (1, 0),   # DOWN
        2: (0, -1),  # LEFT
        3: (0, 1),   # RIGHT
    }

    def __init__(self, rows: int = 5, cols: int = 5,
                 start: tuple[int, int] = (0, 0),
                 goal: tuple[int, int] = (4, 4),
                 max_steps: int = 200) -> None:
        self.rows = rows
        self.cols = cols
        self.start = start
        self.goal = goal
        self.max_steps = max_steps
        self.n_states = rows * cols
        self.n_actions = 4
        self.reset()

    # ------------------------------------------------------------------
    def _to_state(self, row: int, col: int) -> int:
        return row * self.cols + col

    def _to_coords(self, state: int) -> tuple[int, int]:
        return divmod(state, self.cols)

    # ------------------------------------------------------------------
    def reset(self) -> int:
        self._pos = list(self.start)
        self._steps = 0
        return self._to_state(*self._pos)

    def step(self, action: int) -> tuple[int, float, bool]:
        dr, dc = self.ACTION_DELTAS[action]
        new_row = max(0, min(self.rows - 1, self._pos[0] + dr))
        new_col = max(0, min(self.cols - 1, self._pos[1] + dc))
        self._pos = [new_row, new_col]
        self._steps += 1

        state = self._to_state(*self._pos)
        goal_reached = (new_row, new_col) == self.goal
        done = goal_reached or self._steps >= self.max_steps

        reward = 1.0 if goal_reached else -0.01
        return state, reward, done


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------
class QLearningAgent:
    """Tabular Q-learning agent with ε-greedy exploration.

    Parameters
    ----------
    n_states:
        Total number of discrete states in the environment.
    n_actions:
        Total number of discrete actions available.
    alpha:
        Learning rate (step size).
    gamma:
        Discount factor for future rewards.
    epsilon_start:
        Initial exploration probability.
    epsilon_end:
        Minimum exploration probability.
    epsilon_decay:
        Multiplicative decay applied to ε after each episode.
    """

    def __init__(
        self,
        n_states: int,
        n_actions: int,
        alpha: float = 0.1,
        gamma: float = 0.99,
        epsilon_start: float = 1.0,
        epsilon_end: float = 0.01,
        epsilon_decay: float = 0.995,
    ) -> None:
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
        self.q_table = np.zeros((n_states, n_actions))

    # ------------------------------------------------------------------
    def select_action(self, state: int) -> int:
        """ε-greedy action selection."""
        if random.random() < self.epsilon:
            return random.randrange(self.n_actions)
        return int(np.argmax(self.q_table[state]))

    def update(self, state: int, action: int, reward: float,
               next_state: int, done: bool) -> None:
        """Single Q-learning update step."""
        best_next = 0.0 if done else float(np.max(self.q_table[next_state]))
        target = reward + self.gamma * best_next
        self.q_table[state, action] += self.alpha * (
            target - self.q_table[state, action]
        )

    def decay_epsilon(self) -> None:
        """Decay exploration rate after each episode."""
        self.epsilon = max(self.epsilon_end,
                           self.epsilon * self.epsilon_decay)


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------
def train(
    env: GridWorld,
    agent: QLearningAgent,
    n_episodes: int = 500,
    seed: Optional[int] = 42,
) -> np.ndarray:
    """Run the Q-learning training loop.

    Parameters
    ----------
    env:
        The grid-world environment instance.
    agent:
        The Q-learning agent to train.
    n_episodes:
        Number of episodes to train for.
    seed:
        Random seed for reproducibility (``None`` disables seeding).

    Returns
    -------
    rewards : np.ndarray, shape (n_episodes,)
        Total reward collected in each episode.
    """
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    episode_rewards = np.zeros(n_episodes)

    for ep in range(n_episodes):
        state = env.reset()
        total_reward = 0.0
        done = False

        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward

        agent.decay_epsilon()
        episode_rewards[ep] = total_reward

        if (ep + 1) % 100 == 0:
            avg = episode_rewards[max(0, ep - 99): ep + 1].mean()
            print(f"Episode {ep + 1:4d}/{n_episodes} | "
                  f"avg reward (last 100): {avg:.3f} | "
                  f"ε={agent.epsilon:.4f}")

    return episode_rewards


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------
def save_results(rewards: np.ndarray, agent: QLearningAgent) -> None:
    """Persist rewards array and Q-table, and plot the training curve."""
    np.save(RESULTS_DIR / "rewards.npy", rewards)
    np.save(RESULTS_DIR / "q_table.npy", agent.q_table)
    print(f"Saved rewards and Q-table to {RESULTS_DIR}/")

    try:
        import matplotlib.pyplot as plt  # optional dependency

        window = min(50, len(rewards))
        smoothed = np.convolve(rewards,
                               np.ones(window) / window,
                               mode="valid")

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(rewards, alpha=0.3, label="Episode reward")
        ax.plot(range(window - 1, len(rewards)), smoothed,
                label=f"Moving avg ({window})")
        ax.set_xlabel("Episode")
        ax.set_ylabel("Total reward")
        ax.set_title("Q-Learning Training Curve")
        ax.legend()
        fig.tight_layout()
        fig.savefig(RESULTS_DIR / "training_curve.png", dpi=150)
        plt.close(fig)
        print(f"Saved training_curve.png to {RESULTS_DIR}/")
    except ImportError:
        print("matplotlib not installed – skipping training curve plot.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    env = GridWorld(rows=5, cols=5, start=(0, 0), goal=(4, 4))
    agent = QLearningAgent(
        n_states=env.n_states,
        n_actions=env.n_actions,
        alpha=0.1,
        gamma=0.99,
        epsilon_start=1.0,
        epsilon_end=0.01,
        epsilon_decay=0.995,
    )

    print("Training Q-learning agent on 5×5 GridWorld …")
    rewards = train(env, agent, n_episodes=500)
    save_results(rewards, agent)
    print("Done.")
