import os
import torchvision
os.environ['TORCH_HOME']='H:/torchvisionDatas'

if __name__ == '__main__':
    train_set = torchvision.datasets.CIFAR10(root="./dataset", train=True, download=False)
    print(train_set.filename)