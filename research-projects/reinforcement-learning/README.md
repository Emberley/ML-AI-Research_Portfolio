# Reinforcement Learning Agent

A tabular Q-learning agent that learns to navigate a customisable grid-world environment from scratch using only NumPy.

## Folder Structure

```
reinforcement-learning/
├── code/
│   ├── rl_agent.py          # Q-learning agent + GridWorld environment
│   └── requirements.txt     # Python dependencies
├── notebooks/
│   └── rl_exploration.ipynb # Interactive training and visualisation
├── results/                 # Saved metrics, plots, and model checkpoints
└── README.md
```

## Quick Start

```bash
# Install dependencies
pip install -r code/requirements.txt

# Train the agent (500 episodes by default)
python code/rl_agent.py

# Results are saved to results/
```

## Algorithm

| Parameter       | Default |
|-----------------|---------|
| Learning rate α | 0.1     |
| Discount γ      | 0.99    |
| Exploration ε   | 1.0 → 0.01 (decay) |
| Episodes        | 500     |

## Results

After training, the following files are written to `results/`:

- `rewards.npy` – per-episode total reward array
- `q_table.npy` – final Q-table
- `training_curve.png` – reward curve plot
