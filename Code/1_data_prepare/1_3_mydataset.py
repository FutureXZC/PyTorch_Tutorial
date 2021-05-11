# coding: utf-8
from PIL import Image
from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self, txt_path, transform=None, target_transform=None):
        '''
        建立 [index, label] 的映射，初始化 transform 和 target_transform
        '''
        fh = open(txt_path, 'r')
        imgs = []
        for line in fh:
            line = line.rstrip()
            words = line.split()
            imgs.append((words[0], int(words[1])))

        self.imgs = imgs  # 最主要就是要生成这个list， 然后DataLoader中给index，通过getitem读取图片数据
        self.transform = transform
        self.target_transform = target_transform

    def __getitem__(self, index):
        '''
        读取 index 处的图片，并对其做相应的 transform
        '''
        fn, label = self.imgs[index]
        img = Image.open(fn).convert(
            'RGB')  # 像素值 0~255，在transfrom.totensor会除以255，使像素值变成 0~1

        if self.transform is not None:
            img = self.transform(img)  # 在这里做transform，转为tensor等等

        return img, label

    def __len__(self):
        '''
        数据集大小
        '''
        return len(self.imgs)