# multimodal-brain-database
## 一、目录结构
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
## 二、数据集

| 数据集名称                          | 简介                                                             | 数据模态                           | 链接                                                 |
|--------------------------------| ---------------------------------------------------------------- | ---------------------------------- | ---------------------------------------------------- |
| **DAIC-WOZ**                   | 抑郁症分析交互式会话数据集（Distress Analysis Interview Corpus） | 视频、语音、文本、PHQ-8标签        | [链接](https://dcapswoz.ict.usc.edu/)                   |
| **AVEC Challenges (2013-2019)** | 多年抑郁与情绪识别比赛数据，含情感语音和视频                     | 语音、视频、标签（如BDI-II）       | [链接](https://www.audio-visual-emotion-challenge.org/) |
| **DEAP**                       | 情绪分析EEG数据集，含视频诱发情绪、多通道EEG                     | EEG、视频、情绪评分                | [链接](http://www.eecs.qmul.ac.uk/mmv/datasets/deap/)   |
| **SEED / SEED-IV**             | 情绪诱发的EEG脑电数据（由SJTU发布）                              | EEG（62通道），视觉刺激            | [链接](https://bcmi.sjtu.edu.cn/~seed/)                 |
| **OpenNeuro (多个数据集)**          | 含抑郁症/健康人fMRI、DWI、EEG数据的大型平台                      | fMRI、结构像、DWI、EEG             | [链接](https://openneuro.org/)                          |
| **BCIC-IV-2a datasets**        | 脑机接口领域广泛使用的脑电数据集                                 | EEG(22通道)，运动想象              | 链接                                                 |
| **OpenBMI datasets**           | 运动图像任务的脑电图记录                                         | EEG(62通道)，运动想象              | 链接                                                 |
| **CIFAR-10 和 CIFAR-100**       | 图像在多个时间步长中重复作为输入帧                               | 包含 60，000 张 32×32 大小的图像  | 链接                                                 |
| **DVS-CIFAR10 和 DVS-Gesture**  | 以高时间分辨率捕获像素级亮度变化以生成事件流                     | 不同光照条件下执行的 11 种手势类别 | 链接                                                 |
| **BCIC-IV-2b datasets**        | 脑机接口领域广泛使用的脑电数据集                                 | EEG(22通道)，运动想象              | 链接                                                 |
| **PSYCHE-D**                   | 精神健康评估数据库，集成多模式数据                                 | 电子健康记录、可穿戴设备、神经影像 | [链接](https://psyche-d.org/)                          |
### 2.1 DAIC-WOZ

该数据库包含临床访谈，旨在支持心理困扰条件的诊断，如焦虑、抑郁和创伤后应激障碍。

这些访谈被收集起来，作为创建一个计算机代理的更大努力的一部分，该代理可以采访人们并识别精神疾病的言语和非言语指标（DeVault et al., 2014）。

收集的数据包括录音和录像以及广泛的问卷答复；语料库的这一部分包括来自《绿野仙踪》访谈的数据，由一个名为Ellie的动画虚拟采访者进行，由另一个房间的人类采访者控制。

数据已经转录和注释了各种语言和非语言特征。该下载包含189个互动会话，时长在7-33分钟之间（平均为16分钟）。每个会话包括交互记录、参与者音频文件和面部特征信息。

更多细节，请参阅（https://dcapswoz.ict.usc.edu/wp-content/uploads/2022/02/DAICWOZDepression_Documentation.pdf）。

#### 2.2 Extended DAIC Database

这是由ICT开发的抑郁症和创伤后应激障碍评估DAIC-WOZ数据库的扩展版本。这些数据用于[AVEC 2019]（https://sites.google.com/view/avec2019/home）挑战赛。

### 2.3 AVEC Challenges (2013-2019)

视听情感挑战是第九届竞赛项目，旨在比较多媒体处理和机器学习方法在自动视听健康和情绪分析方面的应用，所有参与者都在相同的条件下严格竞争。挑战的目标是为多模态信息处理提供一个共同的基准测试集，并将健康和情感识别界以及视听处理界聚集在一起，比较从现实数据中识别健康和情感的各种方法的相对优点。

### 2.4 DEAP

32名参与者在观看40段一分钟长的音乐视频片段时，记录了他们的脑电图（EEG）和周围生理信号。参与者根据兴奋程度、效价、喜欢/不喜欢程度、主导程度和熟悉程度对每个视频进行评分。32名参与者中有22人的正面脸也被录了下来。

"DEAP: A Database for Emotion Analysis using Physiological Signals (PDF)", S. Koelstra, C. Muehl, M. Soleymani, J.-S. Lee, A. Yazdani, T. Ebrahimi, T. Pun, A. Nijholt, I. Patras, EEE Transactions on Affective Computing, vol. 3, no. 1, pp. 18-31, 2012

### 2.5 SEED/SEED-IV

SEED 数据集包含 12 名受试者的脑电图和眼球运动数据以及另外 3 名受试者的脑电图数据。数据是在他们观看电影剪辑时收集的。 电影剪辑经过精心挑选，以诱发不同类型的情感，这些情感是 积极、消极和中性。

SEED-IV 是原始 SEED 数据集的演变。 情绪的类别数变为四种：快乐、悲伤、恐惧和中性。 在 SEED-IV 中，我们不仅提供脑电信号，还提供由 SMI 眼动追踪眼镜 / 这使它成为用于情感识别的格式良好的多模态数据集。 单击此处了解有关数据集的详细信息。

### 2.6 OpenNeuro

例如：depression -rest数据集包括122名受试者。544名受试者的BDI得分不稳定，因此该数据被丢弃。在剩下的121名参与者中，74名男性和47名女性。年龄范围为18至24岁。该数据集在使用脑电图信号对受试者进行连续抑郁评分方面表现良好。该数据集使用10-10系统收集患者头部64个通道的脑电图信号。

### 2.7 BCIC-IV-2a datasets

bbic - iv -2a数据集是脑机接口领域广泛使用的脑电数据集，包括9名健康参与者的脑电图记录，收集于两个独立的实验阶段。脑电信号采集采用22通道Ag/AgCl电极装置，按10-20系统放置。在250 Hz采样之前，信号在0.5和100 Hz之间进行带通滤波。在每个阶段，参与者执行四种类型的MI任务：想象左手、右手、双脚和舌头的运动。每项任务在每个受试者中重复72次，总共进行了288次试验。在我们的研究中，我们进一步应用了0.5 ~ 40 Hz的带通滤波器来降低高频噪声，并集中在每次试验开始后2 ~ 6秒的时间窗口进行特征提取和分类。

### 2.8 BCIC-IV-2b datasets

该数据集来自Lee等人先前的研究，包括9名受试者的脑电图记录。

信号采集采用三种电极配置，采样率为250 Hz，初始带通滤波器为0.5至100 Hz。每个受试者都完成了一个二元运动想象任务，想象他们左手或右手的运动。所有受试者完成了五个实验阶段：前两个阶段包括无反馈的训练（筛选阶段），而后三个阶段包括实时视觉反馈（在屏幕上显示笑脸）。每个无反馈阶段包含120个试验，而每个有反馈阶段包含160个试验。对于模型开发，前三个会话的数据形成训练集，最后两个会话保留用于测试。在预处理过程中，信号经过额外的带通滤波（0.5-40 Hz），并从试验开始后的3-7秒窗口提取数据进行分析。

### 2.9 OpenBMI datasets

OpenBMI数据集包括54名健康受试者执行左/右运动图像任务的脑电图记录。每个受试者完成两次试验，每班100次试验（200次/次），试验时间为4秒。以1000 Hz采样的62个电极的原始数据被降采样到250 Hz并带通滤波（0.5-40 Hz）。我们每次试验提取4秒的片段，并采用原始研究的20个电极配置（FC-5/3/1/2/4/6, C5/3/1/z/2/4/6, CP-5/3/1/z/2/4/6）。会话1作为训练集，会话2保留用于测试。

### 2.10 CIFAR-10 和 CIFAR-100

CIFAR-10 和 CIFAR-100 是静态数据集

对于静态数据集，图像在多个时间步长中重复作为输入帧。CIFAR-10 包含 60，000 张 32×32 大小的图像，均匀分布在 10 个类别中，每个类别有 6，000 张图像。CIFAR-100 包含 100 个类别，每个类别有 600 张图像，其中包括 500 张训练图像和 100 张测试图像。

### 2.11 DVS-CIFAR10 和 DVS-Gesture

神经形态数据的预处理遵循 MLF（Feng 等人，2022 年）中的方法，即将事件流整合为帧。DVS-CIFAR10 是从 CIFAR-10 衍生而来的基于事件的数据集，以高时间分辨率捕获像素级亮度变化以生成事件流，而非静态帧。DVS-Gesture 是一个用于手势识别的数据集，由 DVS 传感器在动态手势过程中直接记录。它包括 29 名参与者在不同光照条件下执行的 11 种手势类别（例如挥手、鼓掌、抓握）。

### 2.12 PSYCHE-D

精神健康评估数据库（PSYCHE-D）是一个综合性的纵向数据库，旨在推进精神健康诊断、个性化治疗和生物标志物发现方面的研究。它集成了来自多个医疗机构的不同队列的多模式数据，包括临床记录、数字表型、神经成像和患者报告的结果。

该数据库捕获结构化电子健康记录（EHRs），包括诊断、药物和临床医生评估；来自可穿戴设备的被动行为数据（例如，睡眠模式、活动水平）；神经影像学(MRI / fMRI);遗传标记;以及情绪和症状的实时生态瞬间评估（EMAs）。这种多维方法使研究人员能够从生物学、行为学和环境领域全面研究精神疾病。

PSYCHE-D包括来自超过15,000名同意参与者的匿名数据，涵盖情绪障碍（抑郁症，双相情感障碍），焦虑症，神经发育障碍（ADHD， ASD）和健康对照。纵向跟踪范围从6个月到5年，捕捉动态治疗反应和疾病进展。

技术架构结合了SQL（用于结构化电子病历）和NoSQL系统（用于时间序列传感器/EMA数据），由本体驱动的元数据支持，以协调术语。严格的预处理确保数据质量：符合hipaa的去识别保护隐私；单位归一化和时间对齐对多源数据进行标准化；高级imputation （MICE算法）解决了缺失值；伪迹去除技术清除传感器噪声。

该数据库支持多种研究应用：

-使用机器学习对复发风险进行预测建模。

-通过治疗笔记的自然语言处理分析治疗效果。

-将环境因素与症状严重程度联系起来的地理空间研究。

受GDPR和机构审查标准的约束，psych - d提供分层访问：开放元数据供公众使用，去识别样本供认可的研究人员使用，完整数据集供合作联盟使用。通过将高维数据与强大的预处理管道相结合，psych -d支持可重复的大规模研究，以加速精确精神病学。

## 三、预处理


| 数据类型 | 描述                    | 预处理任务                       | 工具建议               |
| -------- | ----------------------- | -------------------------------- | ---------------------- |
| EEG/MEG  | 静息态或任务态脑电信号  | 滤波、伪迹移除、频带分解         | MNE, SciPy             |
| fMRI/DWI | 静息态fMRI、结构像、DTI | 切片提取、脑区配准、标准化       | nilearn, fmriprep      |
| 语音     | 自述访谈录音、语音任务  | 噪声移除、MFCC提取、情感标签标注 | librosa, openSMILE     |
| 视频     | 面部视频、眼动跟踪      | 人脸检测、表情识别、微表情识别   | OpenCV, dlib, DeepFace |
| 文本     | 自述文本、量表问卷      | 分词、关键词提取、情感标注       | SpaCy, Transformers    |
| 临床标签 | HAMD、PHQ-9、诊断结论   | 标签归一化、匹配ID索引           | pandas, Excel utils    |
