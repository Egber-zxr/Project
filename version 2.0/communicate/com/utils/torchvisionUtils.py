import os
import torchvision
os.environ['TORCH_HOME']='C:\Users\dell\Desktop\毕设\预置\cifar10'

if __name__ == '__main__':
    train_set = torchvision.datasets.CIFAR10(root="./dataset", train=True, download=False)
    print(train_set.filename)