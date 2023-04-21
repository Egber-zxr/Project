import os
import torchvision

os.environ['TORCH_HOME']='H:/torchvisionDatas'
root = "./datas"

# TODO 正式环境中需要将值改为 True
downloadFlag = True

def dowloadDatasets(type):
    '''
    根据不同的类型在对应的数据集
        TODO 如果需要其他的数据集，可在此处自行添加
    :param type:
    :return:
    '''
    if type=='CIFAR10':
        train_set = torchvision.datasets.CIFAR10(root=root, train=True, download=downloadFlag)
    else:
        train_set = torchvision.datasets.MNIST(root=root, train=True, download=downloadFlag)
    return train_set.filename

if __name__ == '__main__':
    train_set = torchvision.datasets.CIFAR10(root="./../datas", train=True, download=False)
    print(train_set.filename)
