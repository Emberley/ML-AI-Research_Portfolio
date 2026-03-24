from teacher.train_ppo import train_ppo
from teacher.train_a2c import train_a2c
from teacher.train_dqn import train_dqn
from teacher.evaluate import evaluate_all


def main():
    print("Start Training.....")
    train_ppo()
    train_a2c()
    train_dqn()
    print("Training Completed. Start Evaluation.....")
    evaluate_all()


if __name__ == "__main__":
    main()