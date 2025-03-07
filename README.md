# Deep Learning Project Structure Template 🧠📂

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)]()

一个标准的深度学习项目目录结构模板，遵循模块化、可维护性和可复现性设计原则。适用于 PyTorch/TensorFlow/Keras 等框架。

---

## 目录结构说明 📚
```bash
.
├── configs/             # 配置文件 (超参/模型结构)
├── data/
│   ├── raw/             # 原始数据（禁止修改）
│   ├── processed/       # 预处理后的数据
│   └── splits/          # 数据集划分（train/val/test）
├── models/              # 模型定义与继承
├── experiments/            # 实验记录（按日期或哈希命名）
│   ├── 20230701_exp001/   # 实验目录示例
│   │   ├── checkpoints/   # 模型权重
│   │   ├── logs/          # 训练日志（TensorBoard/WandB）
│   │   └── config.yaml    # 实验完整配置备份
├── src/
│   ├── data_loader/       # 数据加载与预处理
│   ├── training/          # 训练循环逻辑
│   └── utils/             # 通用工具函数
├── requirements.txt     # 依赖清单
└── README.md            # 项目说明
```

---

## 快速使用指南 🚀

### 1. 克隆为项目模板
```bash
git clone https://github.com/Excelius-Wang/deep-learning-project-structure-template.git
cd deep-learning-project-structure-template
```

---

## 最佳实践 ✅

### 配置管理
```yaml
# configs/train/default.yaml
random_seed: 42
batch_size: 64
optimizer:
  name: "adam"
  lr: 1e-3
  weight_decay: 1e-4
```

### 数据隔离原则
- 原始数据 (`data/raw/`) 始终保持只读
- 预处理脚本应保存到 `src/data_loader/preprocess.py`

### 实验可复现性
```bash
# 每次实验自动备份配置
cp configs/ experiments/20230701_exp001/config_backup/
```

---

## 贡献与许可 📜

- ​**贡献指南**：请见 [CONTRIBUTING.md](docs/CONTRIBUTING.md)
- ​**许可证**：[MIT License](LICENSE)

---

**结构化即效率！​** 🚀