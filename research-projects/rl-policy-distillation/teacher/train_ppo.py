import torch
import torch.optim as optim
from torch.distributions import Categorical

from teacher.config import *
from teacher.env import PongWrapper
from teacher.models import PPOTeacher


def train_ppo():
    env = PongWrapper(ENV_NAME)
    model = PPOTeacher(NUM_ACTIONS).to(DEVICE)
    optimizer = optim.Adam(model.parameters(), lr=LR)

    for episode in range(TOTAL_EPISODES):
        state = torch.tensor(env.reset(), device=DEVICE).unsqueeze(0)
        done = False
        ep_reward = 0

        log_probs, values, rewards = [], [], []

        while not done:
            logits, value = model(state)
            dist = Categorical(logits=logits)
            action = dist.sample()

            next_state, reward, done, _ = env.step(action.item())
            next_state = torch.tensor(next_state, device=DEVICE).unsqueeze(0)

            log_probs.append(dist.log_prob(action))
            values.append(value.squeeze())
            rewards.append(torch.tensor(reward, device=DEVICE, dtype=torch.float32))

            state = next_state
            ep_reward += reward

        returns = []
        G = 0
        for r in reversed(rewards):
            G = r + GAMMA * G
            returns.insert(0, G)
        returns = torch.stack(returns)

        log_probs = torch.stack(log_probs)
        values = torch.stack(values)
        advantage = returns - values

        policy_loss = -(log_probs * advantage.detach()).mean()
        value_loss = advantage.pow(2).mean()
        loss = policy_loss + 0.5 * value_loss

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f"PPO Episode {episode+1}, Reward: {ep_reward}")

    torch.save(model.state_dict(), PPO_SAVE)
    env.close()