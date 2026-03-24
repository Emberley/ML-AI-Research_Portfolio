import torch
import torch.nn as nn
import torch.nn.functional as F


class AtariCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(4, 32, 8, stride=4)
        self.conv2 = nn.Conv2d(32, 64, 4, stride=2)
        self.conv3 = nn.Conv2d(64, 64, 3, stride=1)
        self.fc = nn.Linear(64 * 7 * 7, 512)

    def forward(self, x):
        x = x.float() / 255.0
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = torch.flatten(x, 1)
        x = F.relu(self.fc(x))
        return x


class PPOTeacher(nn.Module):
    def __init__(self, num_actions):
        super().__init__()
        self.backbone = AtariCNN()
        self.policy = nn.Linear(512, num_actions)
        self.value = nn.Linear(512, 1)

    def forward(self, x):
        z = self.backbone(x)
        return self.policy(z), self.value(z)


class A2CTeacher(nn.Module):
    def __init__(self, num_actions):
        super().__init__()
        self.backbone = AtariCNN()
        self.policy = nn.Linear(512, num_actions)
        self.value = nn.Linear(512, 1)

    def forward(self, x):
        z = self.backbone(x)
        return self.policy(z), self.value(z)


class DQNTeacher(nn.Module):
    def __init__(self, num_actions):
        super().__init__()
        self.backbone = AtariCNN()
        self.q = nn.Linear(512, num_actions)

    def forward(self, x):
        z = self.backbone(x)
        return self.q(z)