from pathlib import Path

import torch

from src.utils.logger import printlog

torch.manual_seed(42)

# file_name = Path(Path.cwd().parent.parent, 'data/raw', 'HLM_Short.txt')
file_name = Path(Path.cwd().parent.parent, 'data/raw', 'Hong_Lou_Meng.txt')
printlog(Path.cwd())
printlog(str(file_name))

# 数据预处理
with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()  # str

# 生成词表
chars = sorted(list(set(text)))
vocab_size = len(chars)

# 获取字符与数字的投影
char_to_idx = {ch: i for i, ch in enumerate(chars)}  # 符号到整数
idx_to_char = {i: ch for i, ch in enumerate(chars)}  # 整数到符号


def encode_text(_text):
    return [char_to_idx[ch] for ch in _text]


def decode_text(index_list):
    return ''.join([idx_to_char[i] for i in index_list])

# 训练、验证分组
data = torch.tensor(encode_text(text), dtype=torch.long)   # 整数表示字符
split_factor = 0.8
n = int(split_factor * len(data))   # 前 80%（比例系数）作为训练集
train_data = data[:n]
val_data = data[n:]
printlog(f"文件 {file_name} 读取完成...")

