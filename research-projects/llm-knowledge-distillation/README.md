# RayBNN Knowledge Distillation 

## Overview
This research project explores knowledge distillation from a large language model (LLM) into RayBNN for multiple-choice reasoning on the **AI2 ARC Challenge** dataset. The goal is to transfer reasoning behavior from a teacher model into a smaller student model which will be the RayBNN. Hoping the RayBNN then learns to predict the answer distribution over choices A, B, C, and D.

## Research Objective
- Distill reasoning behavior from an LLM into RayBNN
- Evaluate RayBNN’s ability to approximate the reasoning distribution of the teacher
- Investigate whether non-transformer neural architectures can learn reasoning behaviors through distillation

## Methods
1. Load questions from the AI2 ARC Challenge dataset
2. Pass embeddings to a teacher LLM to obtain probability distributions over answers
3. Store teacher predictions as soft labels
4. Train RayBNN using the labeled dataset
5. Evaluate prediction accuracy on ARC multiple-choice reasoning tasks
6. Optimize parameters

## Dataset
- **AI2 ARC Challenge Dataset**
- Science reasoning multiple-choice questions
- Four answer choices per question

## Expected Outcome
The project investigates whether RayBNN can learn reasoning behavior through distillation from a large language model, enabling smaller biologically inspired architectures to approximate the reasoning patterns of large transformer models.
