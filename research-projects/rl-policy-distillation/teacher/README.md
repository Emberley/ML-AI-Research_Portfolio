# Atari Pong Teacher Models (RL)

## Overview
This module implements three reinforcement learning teacher models trained on the Atari Pong environment. These models are used to learn strong control policies that will later be distilled into a lightweight student model.

## Algorithms
- **PPO (Proximal Policy Optimization)** — stable policy gradient method with clipped objective
- **A2C (Advantage Actor-Critic)** — actor (policy) + critic (value) framework
- **DQN (Deep Q-Network)** — value-based method learning Q(s, a)

## Architecture
All models share a CNN feature extractor:
- Input: 4 stacked grayscale frames (84×84)
- Convolutional layers -> feature representation
- Output heads:
  - Policy logits (PPO, A2C)
  - Value function (PPO, A2C)
  - Q-values (DQN)

## Structure
```text
teacher/
├── config.py
├── env.py
├── models.py
├── train_ppo.py
├── train_a2c.py
├── train_dqn.py
└── evaluate.py

## Environment
- Gymnasium Atari: `ALE/Pong-v5`
- Preprocessing:
  - Grayscale
  - Resize to 84×84
  - Frame stacking (4 frames)

```bash
python main.py
python -m teacher.evaluate
