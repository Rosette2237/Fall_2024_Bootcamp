import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models

class MyBasicModel(nn.Module):
    """
    LeNet-style CNN for FashionMNIST:
      conv1 → pool → conv2 → pool → fc1 → fc2 → out
    """

    def __init__(self):
        super().__init__()
        # 28×28 → conv1(5×5) → 6×24×24
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)
        # 6×12×12 → conv2(5×5) → 12×8×8
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=12, kernel_size=5)

        # after two 2×2 pools: 12×4×4 = 192 features
        self.fc1 = nn.Linear(in_features=192, out_features=120)
        self.fc2 = nn.Linear(in_features=120, out_features=60)
        self.out = nn.Linear(in_features=60, out_features=10)

    def forward(self, x):
        # conv1 + relu + pool
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, kernel_size=2, stride=2)

        # conv2 + relu + pool
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, kernel_size=2, stride=2)

        # flatten (batch_size × 192)
        x = x.view(x.size(0), -1)

        # fully connected layers
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.out(x)
        return x


class FashionResNet50(nn.Module):
    """
    ResNet‑50 adapted for FashionMNIST:
     - conv1 takes 1 input channel instead of 3
     - final fc layer outputs 10 classes instead of 1000
    """

    def __init__(self, pretrained: bool = False):
        super().__init__()
        # load standard ResNet-50
        self.model = models.resnet50(pretrained=pretrained)

        # replace first conv to accept grayscale (1 channel)
        # original: Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.model.conv1 = nn.Conv2d(
            in_channels=1,
            out_channels=64,
            kernel_size=7,
            stride=2,
            padding=3,
            bias=False
        )

        # replace the final fully‑connected layer to output 10 classes
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 10)

    def forward(self, x):
        return self.model(x)
