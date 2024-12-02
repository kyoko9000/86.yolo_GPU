import torch

if torch.cuda.is_available():
    print("ok")
gpu_num = torch.cuda.current_device()
print(gpu_num)