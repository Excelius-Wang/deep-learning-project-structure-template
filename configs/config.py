from dataclasses import dataclass


@dataclass
class Config:
    """模型配置类"""
    vocab_size: int = 50257  # 词表大小
    n_embd: int = 512  # 嵌入维度
    n_head: int = 8  # 注意力头数
    n_layer: int = 12  # Transformer层数
    block_size: int = 256  # 上下文长度
    dropout: float = 0.2  # Dropout概率
    bias: bool = True  # 是否使用偏置项
