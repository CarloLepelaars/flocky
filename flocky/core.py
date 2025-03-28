"""Basic utilities"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['BASE_URL', 'get_gpu_info']

# %% ../nbs/00_core.ipynb 3
import torch
from fastcore.all import *

# %% ../nbs/00_core.ipynb 5
BASE_URL = 'https://fed-ledger-prod.flock.io/api/v1/'
BASE_URL

# %% ../nbs/00_core.ipynb 7
def get_gpu_info():
    gpu_dict = AttrDict()
    gpu_dict.cuda_available = torch.cuda.is_available()
    if gpu_dict.cuda_available:
        gpu_dict.gpu_count = torch.cuda.device_count()
        for i in range(gpu_dict.gpu_count):
            gpu_dict[f'gpu_{i}'] = AttrDict()
            gpu_dict[f'gpu_{i}'].name = torch.cuda.get_device_name(i)
            gpu_dict[f'gpu_{i}'].properties = torch.cuda.get_device_properties(i)
            gpu_dict[f'gpu_{i}'].total_memory = gpu_dict[f'gpu_{i}'].properties.total_memory / 1024**3
            gpu_dict[f'gpu_{i}'].cuda_capability = f"{gpu_dict[f'gpu_{i}'].properties.major}.{gpu_dict[f'gpu_{i}'].properties.minor}"
    else:
        gpu_dict.gpu_count = 0
    return gpu_dict
