import numpy as np  # numpy数组库
import math  # 数学运算库
import matplotlib.pyplot as plt  # 画图库
import tkinter as tk  # 导入tkinter模块。为了方便后续讲解，命名为 tk。
import tkinter.messagebox  # 引入弹窗库，防止解释器弹出报错。

import torch  # torch基础库
import torchvision.datasets as dataset  # 公开数据集的下载和管理
import torchvision.transforms as transforms  # 公开数据集的预处理库,格式转换
import torchvision.utils as utils
import torch.utils.data as data_utils  # 对数据集进行分批加载的工具集
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

print("Hello World")
print(torch.__version__)
print(torch.cuda.is_available())

window = tk.Tk()
window.title('请选择')
window.geometry('300x200')
flag = True


def display_messagebox():
    tk.messagebox.askyesno(title='display_messagebox',
                           message='是否调用下载程序')  # 信息确认弹窗 是 Ture或 否 False
    if tk.messagebox.askyesno(title='display_messagebox', message='是否调用下载程序') == 1:
        os.system('python {}'.format('download.py'))
        flag = False
        # 2-1 准备数据集
        train_data = dataset.CIFAR10(root="cifar10",
                                     train=True,
                                     transform=transforms.ToTensor(),
                                     download=flag)

        # 2-1 准备数据集
        test_data = dataset.MNIST(root="cifar10",
                                  train=False,
                                  transform=transforms.ToTensor(),
                                  download=flag)

        print(train_data)
        print("size=", len(train_data))
        print("")
        print(test_data)
        print("size=", len(test_data))

        # 原图不叠加噪声
        # 获取一张图片数据
        print("原始Pytorch图片")
        image, label = train_data[2]
        print("torch image shape:", image.shape)
        print("torch image label:", label)

        print("\n通道转换后的Numpy图片")
        image = image.numpy().transpose(1, 2, 0)  # 交换维度，从GBR换成RGB
        print("numpy image shape:", image.shape)
        print("numpy image label:", label)

        plt.imshow(image)
        plt.show()

        # 批量数据读取
        train_loader = data_utils.DataLoader(dataset=train_data,
                                             batch_size=8,
                                             shuffle=True)

        test_loader = data_utils.DataLoader(dataset=test_data,
                                            batch_size=8,
                                            shuffle=True)

        print(train_loader)
        print(test_loader)
        print(len(train_data), len(train_data) / 8)
        print(len(test_data), len(test_data) / 8)

        # 显示一个batch图片
        print("获取一个batch组图片")
        imgs, labels = next(iter(train_loader))
        print(imgs.shape)
        print(labels.shape)
        print(labels.size()[0])

        print("\n合并成一张三通道灰度图片")
        images = utils.make_grid(imgs, nrow=4)
        print(images.shape)
        print(labels.shape)

        print("\n转换成imshow格式")
        images = images.numpy().transpose(1, 2, 0)
        print(images.shape)
        print(labels.shape)

        print("\n显示图片")
        plt.imshow(images)
        plt.show()

        # window.destroy()
    else:
        flag=True
        window.destroy()
        # 2-1 准备数据集
        train_data = dataset.CIFAR10(root="cifar10",
                                     train=True,
                                     transform=transforms.ToTensor(),
                                     download=flag)

        # 2-1 准备数据集
        test_data = dataset.MNIST(root="cifar10",
                                  train=False,
                                  transform=transforms.ToTensor(),
                                  download=flag)

        print(train_data)
        print("size=", len(train_data))
        print("")
        print(test_data)
        print("size=", len(test_data))

        # 原图不叠加噪声
        # 获取一张图片数据
        print("原始Pytorch图片")
        image, label = train_data[2]
        print("torch image shape:", image.shape)
        print("torch image label:", label)

        print("\n通道转换后的Numpy图片")
        image = image.numpy().transpose(1, 2, 0)  # 交换维度，从GBR换成RGB
        print("numpy image shape:", image.shape)
        print("numpy image label:", label)

        plt.imshow(image)
        plt.show()

        # 批量数据读取
        train_loader = data_utils.DataLoader(dataset=train_data,
                                             batch_size=8,
                                             shuffle=True)

        test_loader = data_utils.DataLoader(dataset=test_data,
                                            batch_size=8,
                                            shuffle=True)

        print(train_loader)
        print(test_loader)
        print(len(train_data), len(train_data) / 8)
        print(len(test_data), len(test_data) / 8)

        # 显示一个batch图片
        print("获取一个batch组图片")
        imgs, labels = next(iter(train_loader))
        print(imgs.shape)
        print(labels.shape)
        print(labels.size()[0])

        print("\n合并成一张三通道灰度图片")
        images = utils.make_grid(imgs, nrow=4)
        print(images.shape)
        print(labels.shape)

        print("\n转换成imshow格式")
        images = images.numpy().transpose(1, 2, 0)
        print(images.shape)
        print(labels.shape)

        print("\n显示图片")
        plt.imshow(images)
        plt.show()


tk.Button(window, text='是否调用下载程序', command=display_messagebox).pack()
window.mainloop()

