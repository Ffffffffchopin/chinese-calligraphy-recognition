import yaml
import torch
import torch.nn.functional as F

import torch.nn.Module as Module

import torch.nn as nn


config_path = 'config.yaml'
with open(config_path) as file:
    config = yaml.safe_load(file)


class CRmodel(Module):
    def __init__(self,num_class):
        super(CRmodel, self).__init__()
        self.num_class=num_class

        self.data_augmentation=nn.Sequential()