import torch

from teacher.config import *
from teacher.env import PongWrapper
from teacher.models import PPOTeacher, A2CTeacher, DQNTeacher


def evaluate_policy_model(model, name):
    env = PongWrapper(ENV_NAME)
    rewards = []

    for _ in range(EVAL_EPISODES):
        state = torch.tensor(env.reset(), device=DEVICE).unsqueeze(0)
        done = False
        ep_reward = 0

        while not done:
            with torch.no_grad():
                out = model(state)
                if isinstance(out, tuple):
                    logits, _ = out
                    action = torch.argmax(logits, dim=1).item()
                else:
                    action = torch.argmax(out, dim=1).item()

            next_state, reward, done, _ = env.step(action)
            state = torch.tensor(next_state, device=DEVICE).unsqueeze(0)
            ep_reward += reward

        rewards.append(ep_reward)

    env.close()
    print(f"{name} Mean Reward: {sum(rewards)/len(rewards):.2f}")


def evaluate_all():
    ppo = PPOTeacher(NUM_ACTIONS).to(DEVICE)
    a2c = A2CTeacher(NUM_ACTIONS).to(DEVICE)
    dqn = DQNTeacher(NUM_ACTIONS).to(DEVICE)

    ppo.load_state_dict(torch.load(PPO_SAVE, map_location=DEVICE))
    a2c.load_state_dict(torch.load(A2C_SAVE, map_location=DEVICE))
    dqn.load_state_dict(torch.load(DQN_SAVE, map_location=DEVICE))

    ppo.eval()
    a2c.eval()
    dqn.eval()

    evaluate_policy_model(ppo, "PPO")
    evaluate_policy_model(a2c, "A2C")
    evaluate_policy_model(dqn, "DQN")