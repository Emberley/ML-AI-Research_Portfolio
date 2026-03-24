ENV_NAME = "ALE/Pong-v5"

DEVICE = "cpu"  

NUM_ACTIONS = 6
INPUT_SHAPE = (4, 84, 84)

PPO_SAVE = "ppo_teacher.pt"
A2C_SAVE = "a2c_teacher.pt"
DQN_SAVE = "dqn_teacher.pt"

TOTAL_EPISODES = 100
EVAL_EPISODES = 10

GAMMA = 0.99
LR = 1e-4