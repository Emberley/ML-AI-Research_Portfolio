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





