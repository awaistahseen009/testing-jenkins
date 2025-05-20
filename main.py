import torch
from torch import nn

X = torch.randn((20 , 10))
w = torch.randn(10 , 10)
b  = torch.randn((1, 10))

y = X @ w + b
print(y)