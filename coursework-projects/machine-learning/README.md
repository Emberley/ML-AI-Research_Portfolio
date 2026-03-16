# A Multi-Optimization Approach to Classification of Sirtuin6 Small Molecule Inhibitors for Pre-Screening Potential Drug Candidate using Regularized Softmax Regression
**ECE 503: Optimization in Machine Learning**

## Overview
This project investigates the use of **softmax multi-classification** to classify potential small molecule inhibitors targeting the **Sirtuin6 (SIRT6)** protein. The goal is to determine whether a softmax-based classification model combined with optimization techniques can enhance performance in identify potential drug candidates.

The dataset was obtained from the **UCI Machine Learning Repository** and processed in MATLAB. Samples were labeled based on binding free energy (BFE), where high BFE values were labeled as potential inhibitors and low BFE values as non-inhibitors. The dataset was randomly shuffled to remove ordering bias and divided into **training and testing datasets**, with 80 samples used for training and 20 samples used for testing.

In addition to evaluating optimization performance, **feature reduction techniques** were applied using covariance analysis and eigenvalue decomposition. This allowed the model to retain the most informative features while significantly reducing computational complexity. The resulting simplified model achieved approximately **20× faster computation while maintaining comparable classification accuracy**.

## Methods
- Regularized softmax regression for binary classification
- Comparison of multiple optimization algorithms
- Convergence analysis of loss functions
- Data normalization using standard scaling
- Feature reduction using covariance matrix and eigenvalue analysis
- Evaluation using training/testing accuracy and confusion matrices

## System Architecture
1. Data collection from UCI Machine Learning Repository
2. Dataset labeling based on binding free energy (BFE)
3. Data shuffling and train-test split
4. Feature scaling and normalization
5. Optimization of the regularized softmax loss function
6. Comparison of optimization algorithms (CGD, BFGS, NAG)
7. Feature reduction using covariance and eigenvalue decomposition
8. Model retraining with reduced feature set
9. Performance evaluation using classification accuracy and confusion matrices

## Technologies
MATLAB  
Optimization Algorithms  
Softmax Regression  
Feature Reduction  
Statistical Data Normalization  

## Results
- Successful classification of potential **SIRT6 inhibitor candidates**
- Comparative analysis of multiple optimization algorithms
- Identification of optimal regularization parameter (μ = 0.003)
- Feature reduction significantly improved computational efficiency
- Achieved approximately **20× faster training time with comparable accuracy**

## Future Work
- Apply **Principal Component Analysis (PCA)** for automated dimensionality reduction
- Explore deep learning models for molecular feature representation
- Expand the dataset with larger biochemical screening datasets
- Investigate nonlinear dimensionality reduction techniques

## Visuals
![Optimizer Convergence](images/optimizer_convergence.png)  
![Confusion Matrix](images/confusion_matrix.png)  
![Feature Reduction Comparison](images/feature_reduction_comparison.png)
