# RayBNN Policy Distillation

## Overview

This project explores policy distillation and behavior cloning using reinforcement learning. A teacher agent is trained on an Atari environment using Proximal Policy Optimization (PPO) and two others models. The trained teacher generates state–action pairs that are used to train a student neural network, RayBNN through supervised learning.The goal is to evaulate how well the RayBNN learns the teacher’s policy and apply to different unseen Atari games without training to test adapatbility.

## Methods
1. Train a PPO reinforcement learning agent on an Atari environment-Pong
2. Convert into supervised learning data set with labels as action probabilities
3. Train RayBNN to imitate the teacher policy
4. Evaluate student policy performance in the Atari environment
5. Compare student and teacher rewards

## Technologies Used
- Python
- PyTorch
- Stable-Baselines3
- Gymnasium
- ALE (Atari Learning Environment)

## Results
* Successfully distill a simple teacher policy into the RayBNN and played the game cartpole.



# Atari Pong Teacher Models (RL)

## Overview
Thmode teacher folder implements three reinforcement learning teacher models trained on the Atari Pong environment. These models are used to learn strong control policies that will later be distilled into the RayBNN model.

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
- Gymnasium Atari: `ALE/Pong-v5`

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
```

## Run
```bash
python main.py
python -m teacher.evaluate






