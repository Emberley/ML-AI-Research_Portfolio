# LLM Knowledge Distillation & Explainability Research  
**Independent AI Research Project (Ongoing 2025 – 2026)**

## Overview
This research investigates large language model (LLM) behavior using knowledge distillation and interpretability techniques. The focus is on understanding why certain words (e.g., "leverage") are consistently chosen and visualizing model decision processes. The project aims to enhance explainability and reduce black-box behavior in LLMs.

## Methods
- Knowledge distillation to train smaller, interpretable models from a pre-trained LLM  
- Analysis of token selection patterns and probability distributions  
- Visualization of attention weights and gradient-based importance scores  
- Modular Python code design for reproducible interpretability experiments  
- Application of explainability metrics and fairness checks  

## System Architecture
1. LLM input tokenization and embedding extraction  
2. Knowledge distillation into a smaller, interpretable model  
3. Explainability analysis (attention maps, gradients, feature importance)  
4. Visualization and plotting of model decision patterns  
5. Evaluation of interpretability and bias metrics  

## Technologies
Python  
PyTorch  
Transformers  
Matplotlib / Seaborn  
Explainable AI (XAI) Techniques  
Knowledge Distillation  

## Results
- Identified consistent token selection patterns (e.g., frequent choice of "leverage")  
- Generated visualizations showing attention distribution and token influence  
- Developed a modular Python pipeline for reproducible analysis of LLM decision-making  

## Future Work
- Extend to larger LLM architectures and cross-domain datasets  
- Integrate SHAP or LIME-based explanations for more detailed interpretability  
- Develop an interactive dashboard to visualize word selection patterns and biases  

## Visuals
![Attention Heatmap](images/attention_heatmap.png)  
![Token Probability Plot](images/token_probability_plot.png)  
