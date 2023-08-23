import os
import shutil
import random
import torch
import torchvision
import numpy as np

from PIL import Image
from matplotlib import pyplot as plt

torch.manual_seed(0)

class_names = ['normal', 'viral', 'covid']
root_dir = 'dataset'
source_dirs = ['NORMAL', 'Viral Pneumonia', 'COVID-19']

