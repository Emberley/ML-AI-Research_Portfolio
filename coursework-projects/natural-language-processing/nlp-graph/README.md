# StackExchange Data Science Community Analysis
**CSC 501: Data Algorithms and Structures **

## Overview
This project analyzes the StackExchange Data Science community to understand user participation dynamics, reputation systems, and badge-based incentives within a question-and-answer platform. The analysis combines exploratory data analysis, relational database modeling, and graph-based modeling to investigate user interactions and how they influence community engagement.

The study explores how high-reputation users contribute to the platform, how badge systems encourage participation, and how topic popularity reflects trends in the data science community. Additionally, both relational and graph-based database models were developed and compared to evaluate performance for analyzing highly interconnected community data. 

## Methods
1. Collect StackExchange Data Science community dataset  
2. Perform exploratory data analysis to study participation trends  
3. Analyze relationships between reputation, badges, and contributions  
4. Design relational database schema and ERD model  
5. Normalize database schema to BCNF  
6. Implement graph-based data model for user interactions  
7. Execute queries on relational database (MySQL)  
8. Execute equivalent graph-based queries using Python and NetworkX  
9. Compare performance and efficiency of both data models   

## System Architecture
Relational database design including:
- Entity-Relationship Diagram (ERD) modeling  
- Relational schema design  
- Boyce-Codd Normal Form (BCNF) normalization  
- Functional dependency analysis  

Graph-based modeling of the community network using:
- Node relationships between users, posts, tags, comments, and badges  
- Graph traversal for analyzing community interactions  

## Results
The analysis revealed strong relationships between reputation, participation, and badges within the StackExchange Data Science community.

Key findings include:

- High-reputation users contribute more frequently through answers, comments, and community engagement activities.
- A strong positive correlation exists between total contribution scores and reputation points.
- Badge systems act as a motivational mechanism encouraging community participation.
- Topic analysis shows **machine learning** and **Python** as the most active subjects in the community.
- Graph-based database models significantly outperform relational databases when analyzing highly connected data.

Performance comparison experiments showed:

- Querying top users by reputation took **0.24 seconds using SQL**, compared to **28.7 milliseconds using a graph model**.
- Complex queries involving multiple joins took **1.76 seconds in relational databases**, but only **127 milliseconds in the graph-based model**.

These results demonstrate that graph-based data models are more efficient for analyzing highly relational community datasets such as StackExchange networks.


---

## Visuals
![Semantic Network Graph](images/stackexchange_network.png)  
![Cluster Analysis Visualization](images/stackexchange_clusters.png)
