# Atari CNN Teacher Policy Distillation  
**Independent AI Research Project (Ongoing 2025 – 2026)**

## Overview
This project distills knowledge from a CNN-based teacher agent trained on Atari environments into a smaller student agent using the `raybnn` neural network framework. The goal is to retain performance while reducing model size and inference complexity, enabling faster training and deployment.

## Methods
- Training a CNN-based teacher agent on Atari games  
- Knowledge distillation from teacher to student agent  
- Policy evaluation and performance benchmarking  
- Modular implementation with `raybnn` for neural network training and GPU acceleration  
- Monitoring convergence, reward accumulation, and stability  

## System Architecture
1. Environment setup (Atari gym environments)  
2. Teacher agent training (CNN-based)  
3. Student agent initialization using `raybnn`  
4. Policy distillation via supervised transfer of teacher action probabilities  
5. Performance evaluation and visualizations  

## Technologies
Python  
Rust (`raybnn` + `arrayfire` for GPU)  
Gym / Gymnasium  
CNNs  
Reinforcement Learning  
Policy Distillation  

## Results
- Student agent successfully learns from teacher with minimal performance loss  
- Reduced model size and inference time compared to teacher  
- Visualized training curves and policy convergence for multiple Atari games  

## Future Work
- Extend distillation to larger Atari games and multi-agent scenarios  
- Integrate attention or interpretability layers to understand policy transfer  
- Explore hybrid CNN + Transformer architectures for richer feature extraction  

## Visuals
![Teacher vs Student Reward Curve](images/atari_reward_curve.png)  
![Policy Distillation Flow](images/atari_policy_distillation.png)
