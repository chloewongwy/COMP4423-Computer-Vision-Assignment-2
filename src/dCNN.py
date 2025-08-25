"""
dCNN.py"
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.ops as ops
import torchvision.models as models

class DeformableConv2d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=3, padding=1, stride=1):
        super(DeformableConv2d, self).__init__()
        self.offset = nn.Conv2d(in_channels, 2 * kernel_size * kernel_size, kernel_size=kernel_size, padding=padding, stride=stride)

        self.deform_conv = ops.DeformConv2d(in_channels, out_channels, kernel_size=kernel_size, 
                                            padding=padding, stride=stride, bias=False)
    
    def forward(self, x):
        offsets = self.offset(x)  # calculate offset
        x = self.deform_conv(x, offsets)  # deformable cnn operation
        return x
