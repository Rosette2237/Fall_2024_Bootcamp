import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def load_fashion_mnist(batch_size: int = 64,
                       data_dir: str = "./data"):
    """
    Downloads FashionMNIST (if needed), applies a ToTensor() transform,
    and returns (trainloader, testloader).

    Example:
        trainloader, testloader = load_fashion_mnist()
    """
    # turn PIL images into tensors in [0,1] so plt.imshow(...squeeze()) works
    transform = transforms.Compose([
        transforms.ToTensor()
    ])

    train_ds = datasets.FashionMNIST(
        root=data_dir,
        train=True,
        download=True,
        transform=transform
    )
    test_ds = datasets.FashionMNIST(
        root=data_dir,
        train=False,
        download=True,
        transform=transform
    )

    trainloader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    testloader  = DataLoader(test_ds,  batch_size=batch_size, shuffle=False)

    return trainloader, testloader
