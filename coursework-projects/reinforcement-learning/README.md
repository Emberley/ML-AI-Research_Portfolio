# Reinforcement Learning for Battery Storage Optimization (ECE 569A)

## Overview
This project develops a Q-learning reinforcement learning agent to optimize a 24-hour battery storage policy in a simulated energy environment with stochastic demand and renewable supply. The goal is to minimize energy costs while satisfying demand and maximizing storage efficiency.

## Methods
- Simulated environment modeling stochastic energy demand and renewable supply
- Q-learning algorithm for agent-based policy learning
- Reward function design balancing energy cost, demand satisfaction, and storage efficiency
- Evaluation of convergence behavior and policy stability across multiple training episodes

## System Architecture
1. Environment simulation (energy demand + renewable supply)
2. State representation and action space definition
3. Q-learning agent implementation
4. Reward calculation
5. Policy evaluation and iteration

## Technologies
Python  
Reinforcement Learning  
Q-Learning  
Simulation Modeling  

## Results
- Agent successfully learned an optimal 24-hour battery policy
- Demonstrated convergence of Q-values and stable policy performance
- Achieved a balance between energy cost savings, demand satisfaction, and storage utilization

## Future Work
- Implement Deep Q-Network (DQN) for larger, more complex environments
- Integrate with real-world energy data for testing and validation
- Explore multi-agent reinforcement learning for distributed energy management

## Visuals
![Battery Storage Policy](images/battery_policy_plot.png)  
![Training Convergence](images/q_learning_convergence.png)
