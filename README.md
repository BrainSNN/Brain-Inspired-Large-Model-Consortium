## 一、仓库组织与权限

1. **创建 GitHub Organization**

   - 名称示例：`Brain-Inspired Large Model Consortium`
   - 添加成员并按角色（Owner、Admin、Maintainer、Collaborator）分配权限。

2. **仓库列表与命名**

   ```
   Brain-Inspired Large Model Consortium/
   ├── 01-multimodal-brain-database
   ├── 02-depression-algorithms
   └── 03-brain-machine-interface
   ```

3. **统一模板**（可用 GitHub Template 仓库）

   - `README.md`（☑ 项目介绍、模块目标、安装运行指南）
   - `LICENSE`（推荐 MIT/Apache 2.0）
   - `.github/`
     - `PULL_REQUEST_TEMPLATE.md`
   - `CONTRIBUTING.md`（分支策略、提交规范、Review 流程）
   - `CI/`（GitHub Actions 配置：lint、单元测试、数据完整性检测）

------

## 二、模块一：多模态脑数据库（01-multimodal-database）

### 目录结构

```
01-multimodal-brain-database/
├── data/                         # 原始 & 处理后数据
│   ├── raw/                      # 下载脚本 + 链接
│   │   └── download_datasets.py
│   └── processed/                # 清洗、对齐后的多模态数据
│       ├── audio/                
│       ├── video/                
│       └── eeg/                  
├── scripts/                      # 数据预处理 & 特征提取
│   ├── preprocess_audio.py       
│   ├── preprocess_video.py       
│   └── preprocess_eeg.py         
├── notebooks/                    # 可复现的 EDA & 演示笔记本
│   └── exploratory_analysis.ipynb
├── docs/                         # 数据集说明 & 使用手册
│   └── README.md                 
└── tests/                        # 单元测试：校验数据完整性
    └── test_data_integrity.py
```

### 核心内容

- **数据集链接汇总**（README 中按语音、视频、EEG 分类附上公开数据集和内部采集数据的下载/访问说明）。
- **下载脚本**：一键拉取公开数据、权限验证；支持断点续传。
- **预处理流水线**：统一采样率、时序对齐、多模态同步工具。
- **EDA 笔记本**：统计各模态样本量、分布、缺失率、可视化示例。

------

## 三、模块二：抑郁相关算法仓库（02-depression-algorithms）

### 目录结构

```
02-depression-algorithms/
├── mechanism-models/         # 机制
│   ├── paper_2023_Li_SNN_theta/         # [Li et al., 2023] θ 波前移 SNN 仿真实验
│   ├── code/                        # 复现论文中的 SNN 模型代码
│   │   ├── model.py
│   │   └── train.py
│   ├── data/                        # 论文使用的仿真参数 & 输入文件
│   ├── notebooks/                   # 复现关键图/分析步骤
│   │   └── reproduce_fig3.ipynb
│   └── docs/
├── diagnosis-models/		  # 诊断
│   ├── paper_2022_Zhou_multimodal/      # [Zhou et al., 2022] 语音+面部表情+EEG 诊断模型
│   ├── src/                         # 训练/评估/推理脚本
│   │   ├── train_zdl.py
│   │   └── eval_zdl.py
│   ├── configs/                     # 对应论文中使用的超参文件
│   │   └── zdl_config.yaml
│   ├── experiments/                 # 复现实验日志与结果截图
│   ├── notebooks/                   # 结果分析与 ROC 曲线复现
│   └── docs/                        # 论文核心方法说明 & 链接
├── intervention-models/      #干预
│   ├── paper_2024_Yang_textsentiment/   # [Yang et al., 2024] 抑郁干预
│   ├── ...
│   └── docs/
├── .github/
│   ├── ISSUE_TEMPLATE.md
│   └── PULL_REQUEST_TEMPLATE.md
├── README.md                 # 总体说明 + 各子模块快速导航
└── requirements.txt          # 所有依赖（建议拆分为 mechanism/diagnosis/intervention 的 extras）
```

### 核心内容

**1**.**按论文拆分子模块**

- 每篇发表成果对应一个子文件夹，内含完整复现代码、输入数据（或下载脚本）、结果 notebook、简要方法文档（含 DOI）

**2**.**复现 & 可扩展**

- `code/` 下提供一键复现实验的脚本（如 `python train.py --config config.yaml`）
- `notebooks/` 演示重现主要 Figure（如 θ 波功率谱变化、连通矩阵热图）

------

## 四、模块三：脑机接口（03-brain-machine-interface）

### 目录结构

```
03-brain-machine-interface/
├── hardware_drivers/         # 与 BCI 设备通信的底层驱动与接口
│   └── setup_instructions.md
├── signal_processing/        # EEG 信号滤波、特征提取脚本
│   ├── filters.py
│   └── feature_extraction.py
├── model_integration/        # 将信号输入大模型的桥接层
│   ├── adapter.py
│   └── demo/                 # 演示端到端流程的 Jupyter Notebook
├── experiments/
│   ├── published_results.md  # 已发表实验的硬件型号、协议和性能指标
│   └── reproductions/        # 团队内部复现记录与数据
├── docs/
│   └── BCI_GUIDE.md          # 设备接入教程、安全注意事项
├── Dockerfile                # 部署实验环境
└── README.md                 # 模块概览 + 快速启动指南

```

### 核心内容

- **结合实验室成果**：
  - `published_results.md` 列出每篇 BCI 相关论文的关键参数（采样率、通道数、算法性能），并指向对应的代码实现。
  - 提供 Docker 容器，搭建信号采集→预处理→模型推理的完整流水线。
