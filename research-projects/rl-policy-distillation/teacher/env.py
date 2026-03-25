import gymnasium as gym
import ale_py
import cv2
import numpy as np
from collections import deque


class PongWrapper:
    def __init__(self, env_name):
        self.env = gym.make(env_name)
        self.frames = deque(maxlen=4)

    def reset(self):
        obs = self.env.reset()
        if isinstance(obs, tuple):
            obs = obs[0]

        frame = self.preprocess(obs)
        for _ in range(4):
            self.frames.append(frame)

        return np.stack(self.frames, axis=0)

    def step(self, action):
        result = self.env.step(action)

        if len(result) == 5:
            obs, reward, terminated, truncated, _ = result
            done = terminated or truncated
        else:
            obs, reward, done, _ = result

        frame = self.preprocess(obs)
        self.frames.append(frame)

        return np.stack(self.frames, axis=0), reward, done, {}

    def preprocess(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = cv2.resize(frame, (84, 84))
        return frame

    def close(self):
        self.env.close()