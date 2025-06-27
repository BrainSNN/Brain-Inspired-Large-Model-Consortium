# multimodal-brain-database
## dir
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
## dataset


| 数据集名称                            | 简介                                                             | 数据模态                       | 链接                                                 |
| ------------------------------------- | ---------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------- |
| **DAIC-WOZ**                    | 抑郁症分析交互式会话数据集（Distress Analysis Interview Corpus） | 视频、语音、文本、PHQ-8标签    | [链接](https://dcapswoz.ict.usc.edu/)                   |
| **AVEC Challenges (2013-2019)** | 多年抑郁与情绪识别比赛数据，含情感语音和视频                     | 语音、视频、标签（如BDI-II）   | [链接](https://www.audio-visual-emotion-challenge.org/) |
| **DEAP**                        | 情绪分析EEG数据集，含视频诱发情绪、多通道EEG                     | EEG、视频、情绪评分            | [链接](http://www.eecs.qmul.ac.uk/mmv/datasets/deap/)   |
| **SEED / SEED-IV**              | 情绪诱发的EEG脑电数据（由SJTU发布）                              | EEG（62通道），视觉刺激        | [链接](https://bcmi.sjtu.edu.cn/~seed/)                 |
| **OpenNeuro (多个数据集)**      | 含抑郁症/健康人fMRI、DWI、EEG数据的大型平台                      | fMRI、结构像、DWI、EEG         | [链接](https://openneuro.org/)                          |
| **TReNDs Neuroimaging Data**    | 抑郁、精神病、双相障碍患者的MRI数据                              | fMRI、DWI、结构像              | [链接](https://www.mindresearchnetwork.org/)            |
| **REST-meta-MDD**               | 超过1000名MDD患者的多站点静息态fMRI数据集                        | fMRI、临床标签                 | [链接](http://rfmri.org/REST-meta-MDD)                  |
| **MD-AD Dataset**               | 脑组织RNA表达+临床抑郁程度（适用于多模态融合）                   | RNA-seq、认知标签              | [链接](https://github.com/uci-cbcl/MD-AD)               |
| **eRisk Dataset**               | Reddit用户长时间发帖文本，标注有自杀/抑郁倾向                    | 文本（自然语言）、心理风险标签 | [链接](https://erisk.irlab.org/)                        |
| **Coswara**                     | COVID情绪语音相关数据，可用于情感识别预训练                      | 语音（咳嗽、呼吸、情绪语音）   | [链接](https://coswara.iisc.ac.in/)                     |


### DAIC-WOZ

This database contains clinical interviews designed to support the diagnosis of psychological distress conditions such as anxiety, depression, and post-traumatic stress disorder.

These interviews were collected as part of a larger effort to create a computer agent that interviews people and identifies verbal and nonverbal indicators of mental illness (DeVault et al., 2014).

Data collected include audio and video recordings and extensive questionnaire responses; this part of the corpus includes data from the Wizard-of-Oz interviews, conducted by an animated virtual interviewer called Ellie, controlled by a human interviewer in another room.

Data has been transcribed and annotated for a variety of verbal and non-verbal features. This download includes 189 sessions of interactions ranging between 7-33 minutes (average is 16 minutes). Each session includes transcripts of the interaction, participant audio files, and information about facial features. For more details please refer to the [documentation](https://dcapswoz.ict.usc.edu/wp-content/uploads/2022/02/DAICWOZDepression_Documentation.pdf).

#### Extended DAIC Database

This is the extended version of DAIC-WOZ database for depression and PTSD assessment, developed by ICT. This data was used for the [AVEC 2019](https://sites.google.com/view/avec2019/home) Challenge and is also available upon request. Detailed documentation for this dataset is currently being created. We will update this site with the new documentation once it is completed.

### **AVEC Challenges (2013-2019)**

The Audio/Visual Emotion Challenge and Workshop (AVEC 2019) "State-of-Mind, Detecting Depression with AI, and Cross-cultural Affect Recognition" is the ninth competition event aimed at the comparison of multimedia processing and machine learning methods for automatic audiovisual health and emotion analysis, with all participants competing strictly under the same conditions. The goal of the Challenge is to provide a common benchmark test set for multimodal information processing and to bring together the health and emotion recognition communities, as well as the audiovisual processing communities, to compare the relative merits of various approaches to health and emotion recognition from real-life data.

**DAIC-WOZ、**Extended-DAIC****

### DEAP

### SEED / SEED-IV

### OpenNeuro


The Dression-rest dataset included 122 subjects. The BDI scores of 544 subjects were unstable, so this data was discarded. Among the remaining 121 participants, 74 were male and 47 were female. The age range is 18 to 24 years. This dataset shows good performance in using EEG signals to continuously score subjects for depression . This dataset uses the 10-10 system to collect EEG signals of 64 channels in the patient's head.


### TReNDs Neuroimaging Data

### REST-meta-MDD

### MD-AD Dataset

### eRisk Dataset

### Coswara

## processed


| 数据类型 | 描述                    | 预处理任务                       | 工具建议               |
| -------- | ----------------------- | -------------------------------- | ---------------------- |
| EEG/MEG  | 静息态或任务态脑电信号  | 滤波、伪迹移除、频带分解         | MNE, SciPy             |
| fMRI/DWI | 静息态fMRI、结构像、DTI | 切片提取、脑区配准、标准化       | nilearn, fmriprep      |
| 语音     | 自述访谈录音、语音任务  | 噪声移除、MFCC提取、情感标签标注 | librosa, openSMILE     |
| 视频     | 面部视频、眼动跟踪      | 人脸检测、表情识别、微表情识别   | OpenCV, dlib, DeepFace |
| 文本     | 自述文本、量表问卷      | 分词、关键词提取、情感标注       | SpaCy, Transformers    |
| 临床标签 | HAMD、PHQ-9、诊断结论   | 标签归一化、匹配ID索引           | pandas, Excel utils    |
