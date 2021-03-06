# coding: utf-8

import math
import torch
from torch import nn

from .pretrained import vgg16
from .BasicModule import BasicModule


class ShallowNet(BasicModule):
    def __init__(self, num_classes):
        super(ShallowNet, self).__init__()

        self.features = nn.Sequential(*list(vgg16.features)[:16])

        self.classifier = nn.Linear(in_features=200704, out_features=num_classes, bias=True)

    def forward(self, x):
        features = self.features(x)
        features = features.view(features.size(0), -1)
        out = self.classifier(features)
        return out


class Customed_ShallowNet(BasicModule):
    def __init__(self, num_classes, init_weights=True):
        super(Customed_ShallowNet, self).__init__()

        # 将Vgg16前5层的channel数除以16
        # conv1 = [nn.Conv2d(1, 4, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(4, 4, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # conv2 = [nn.Conv2d(4, 8, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(8, 8, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # conv3 = [nn.Conv2d(8, 16, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(16, 16, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(16, 16, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # conv4 = [nn.Conv2d(16, 32, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(32, 32, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(32, 32, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # conv5 = [nn.Conv2d(32, 32, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(32, 32, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(32, 32, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # self.features = nn.Sequential(*(conv1 + conv2 + conv3 + conv4 + conv5))
        #
        # self.classifier = nn.Linear(in_features=288, out_features=num_classes)

        # 将Vgg16前4层的channel数除以8
        # conv1 = [nn.Conv2d(1, 8, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(8, 8, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # conv2 = [nn.Conv2d(8, 16, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(16, 16, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # conv3 = [nn.Conv2d(16, 32, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(32, 32, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(32, 32, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # conv4 = [nn.Conv2d(32, 64, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(64, 64, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(64, 64, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # self.features = nn.Sequential(*(conv1 + conv2 + conv3 + conv4))
        #
        # self.classifier = nn.Linear(in_features=12544, out_features=num_classes)
        #
        # self.GAP = nn.AvgPool2d(kernel_size=14)
        # self.relu = nn.ReLU(inplace=True)

        # 将Vgg16前4层的channel数除以16
        conv1 = [nn.Conv2d(1, 4, kernel_size=3, padding=1),
                 nn.ReLU(inplace=True),
                 nn.Conv2d(4, 4, kernel_size=3, padding=1),
                 nn.ReLU(inplace=True),
                 nn.MaxPool2d(kernel_size=2, stride=2)]

        conv2 = [nn.Conv2d(4, 8, kernel_size=3, padding=1),
                 nn.ReLU(inplace=True),
                 nn.Conv2d(8, 8, kernel_size=3, padding=1),
                 nn.ReLU(inplace=True),
                 nn.MaxPool2d(kernel_size=2, stride=2)]

        conv3 = [nn.Conv2d(8, 16, kernel_size=3, padding=1),
                 nn.ReLU(inplace=True),
                 nn.Conv2d(16, 16, kernel_size=3, padding=1),
                 nn.ReLU(inplace=True),
                 nn.Conv2d(16, 16, kernel_size=3, padding=1),
                 nn.ReLU(inplace=True),
                 nn.MaxPool2d(kernel_size=2, stride=2)]

        conv4 = [nn.Conv2d(16, 32, kernel_size=3, padding=1),
                 nn.ReLU(inplace=True),
                 nn.Conv2d(32, 32, kernel_size=3, padding=1),
                 nn.ReLU(inplace=True),
                 nn.Conv2d(32, 32, kernel_size=3, padding=1),
                 nn.ReLU(inplace=True),
                 nn.MaxPool2d(kernel_size=2, stride=2)]

        self.features = nn.Sequential(*(conv1 + conv2 + conv3 + conv4))

        self.classifier = nn.Linear(in_features=6272, out_features=num_classes)

        # 将Vgg16前三层的channel数除以16（Baseline）
        # conv1 = [nn.Conv2d(1, 4, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(4, 4, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # conv2 = [nn.Conv2d(4, 8, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(8, 8, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # conv3 = [nn.Conv2d(8, 16, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(16, 16, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.Conv2d(16, 16, kernel_size=3, padding=1),
        #          nn.ReLU(inplace=True),
        #          nn.MaxPool2d(kernel_size=2, stride=2)]
        #
        # self.features = nn.Sequential(*(conv1 + conv2 + conv3))
        #
        # self.classifier = nn.Linear(in_features=3136, out_features=num_classes)

        if init_weights:
            self._initialize_weights()

    def forward(self, x):
        features = self.features(x)
        features = features.view(features.size(0), -1)
        out = self.classifier(features)
        return out

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
                if m.bias is not None:
                    m.bias.data.zero_()
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
                m.weight.data.normal_(0, 0.01)
                m.bias.data.zero_()

