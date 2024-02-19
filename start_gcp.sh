#!/bin/bash

sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y python3.10
sudo apt-get install -y python3.10-distutils

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.10 get-pip.py


sudo apt install -y ffmpeg

echo "alias python=python3.10" >> ~/.bashrc
echo "alias python3=python3.10" >> ~/.bashrc
export PATH="$PATH:/usr/bin/python3.10"
echo "export PATH=\$PATH:/usr/bin/python3.10" >> ~/.bashrc
source ~/.bashrc


mkdir -p ./vridge
cd ./vridge

# RVC 프로젝트 클론
git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI ./RVC

# aria2 설치
sudo apt -y install -qq aria2

# Pretrained 모델 다운로드
declare -a models=("D32k" "D40k" "G32k" "G40k" "f0D32k" "f0D40k" "f0G32k" "f0G40k" "f0Ov2Super40kD" "f0Ov2Super40kG")

for model in "${models[@]}"; do
    aria2c --console-log-level=error -c -x 16 -s 16 -k 1M "https://huggingface.co/lj1995/testc_wordvar/resolve/main/pretrained_v2/${model}.pth" -d ./assets/pretrained_v2 -o "${model}.pth"
done

# ORVC 모델은 별도의 URL에서 다운로드
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M "https://huggingface.co/ORVC/Ov2Super/resolve/main/f0Ov2Super40kD.pth" -d ./assets/pretrained_v2 -o "f0Ov2Super40kD.pth"
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M "https://huggingface.co/ORVC/Ov2Super/resolve/main/f0Ov2Super40kG.pth" -d ./assets/pretrained_v2 -o "f0Ov2Super40kG.pth"

# Python 패키지 설치
pip install -r requirements.txt
pip install mega.py gdown==4.6.0
pip install google-cloud-texttospeech

# 필요한 파일 다운로드
wget https://huggingface.co/Rejekts/project/resolve/main/app.py
wget https://huggingface.co/Rejekts/project/resolve/main/download_files.py
wget https://huggingface.co/Rejekts/project/resolve/main/a.png
wget https://huggingface.co/Rejekts/project/resolve/main/easy_sync.py


# 다운로드 스크립트 실행
python download_files.py

export GOOGLE_APPLICATION_CREDENTIALS="/home/jhko2721/vridge/vridge-5f526-146273e2ebf7.json"