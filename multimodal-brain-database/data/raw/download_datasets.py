import numpy as np
import argparse
import os






















if __name__ == "__main__":
    #调用argparse.ArgumentParser()创建一个ArgumentParser对象
    parser = argparse.ArgumentParser(description="Download datasets for multimodal brain database.")    #添加参数
    parser.add_argument("--data_dir", type=str, default="./data/openneuro", help="The directory to save the downloaded datasets.")
    #datasets参数 如果是openneuro则下载openneuro数据集
    parser.add_argument("--datasets", type=str, default="openneuro", choices=["openneuro", "local"], help="The datasets to download.")
    args = parser.parse_args()  #解析参数
    #如果datasets参数是openneuro则下载openneuro数据集
    if args.datasets == "openneuro":
        os.system("bush BRAIN-INSPIRED-LARGE-SCALE-MULTIMODAL-BRAIN-DATABASE/data/raw/openneuro/ds003478-1.1.0.sh --data_dir {}".format(args.data_dir))