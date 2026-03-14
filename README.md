# ML / AI Research Portfolio

> A curated collection of machine-learning and AI research projects, coursework, and a personal portfolio website.

## Repository Structure

```
ML-AI-Research_Portfolio/
├── coursework-projects/          # Academic coursework and assignments
├── research-projects/            # Original and ongoing research
│   └── reinforcement-learning/   # RL agent project
│       ├── code/                 # Python source code
│       ├── notebooks/            # Jupyter exploration notebooks
│       └── results/              # Saved metrics, plots, and model checkpoints
├── portfolio-website/            # Jekyll-based portfolio site
│   ├── _config.yml
│   ├── _layouts/
│   ├── _includes/
│   ├── projects/
│   └── assets/
│       ├── css/
│       └── images/
├── assets/
│   └── images/                   # Shared images for the README / docs
└── README.md
```

## Projects

### Reinforcement Learning Agent
A from-scratch Q-learning agent that learns to navigate a grid-world environment.
See [`research-projects/reinforcement-learning/`](research-projects/reinforcement-learning/README.md).

### Portfolio Website
A Jekyll static site that showcases every project in this repository.
See [`portfolio-website/`](portfolio-website/README.md).

## Getting Started

### Prerequisites
- Python 3.9+
- Jupyter Notebook / JupyterLab
- Ruby + Bundler (for the Jekyll website)

### Python Environment
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r research-projects/reinforcement-learning/code/requirements.txt
```

### Run the RL Agent
```bash
cd research-projects/reinforcement-learning/code
python rl_agent.py
```

### Launch the Portfolio Website Locally
```bash
cd portfolio-website
bundle install
bundle exec jekyll serve
# Open http://localhost:4000
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)
