import random
import torch
import torch.optim as optim
import torch.nn.functional as F
from collections import deque

from teacher.config import *
from teacher.env import PongWrapper
from teacher.models import DQNTeacher


def train_dqn():
    env = PongWrapper(ENV_NAME)
    model = DQNTeacher(NUM_ACTIONS).to(DEVICE)
    target = DQNTeacher(NUM_ACTIONS).to(DEVICE)
    target.load_state_dict(model.state_dict())

    optimizer = optim.Adam(model.parameters(), lr=LR)
    memory = deque(maxlen=10000)

    epsilon = 1.0
    batch_size = 32

    for episode in range(TOTAL_EPISODES):
        state = torch.tensor(env.reset(), device=DEVICE).unsqueeze(0)
        done = False
        ep_reward = 0

        while not done:
            if random.random() < epsilon:
                action = random.randint(0, NUM_ACTIONS - 1)
            else:
                with torch.no_grad():
                    action = model(state).argmax(dim=1).item()

            next_state, reward, done, _ = env.step(action)
            next_state = torch.tensor(next_state, device=DEVICE).unsqueeze(0)

            memory.append((state, action, reward, next_state, done))
            state = next_state
            ep_reward += reward

            if len(memory) >= batch_size:
                batch = random.sample(memory, batch_size)

                states = torch.cat([b[0] for b in batch])
                actions = torch.tensor([b[1] for b in batch], device=DEVICE)
                rewards = torch.tensor([b[2] for b in batch], device=DEVICE, dtype=torch.float32)
                next_states = torch.cat([b[3] for b in batch])
                dones = torch.tensor([b[4] for b in batch], device=DEVICE, dtype=torch.float32)

                q_values = model(states).gather(1, actions.unsqueeze(1)).squeeze()
                next_q = target(next_states).max(dim=1)[0]
                target_q = rewards + GAMMA * next_q * (1 - dones)

                loss = F.mse_loss(q_values, target_q.detach())

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

        epsilon = max(0.1, epsilon * 0.995)

        if episode % 10 == 0:
            target.load_state_dict(model.state_dict())

        print(f"DQN Episode {episode+1}, Reward: {ep_reward}")

    torch.save(model.state_dict(), DQN_SAVE)
    env.close()

