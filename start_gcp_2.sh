#!/bin/bash

cd ./RVC

# aria2 설치
sudo apt -y install -qq aria2

# Pretrained 모델 다운로드
declare -a models=("D32k" "D40k" "G32k" "G40k" "f0D32k" "f0D40k" "f0G32k" "f0G40k")

for model in "${models[@]}"; do
    aria2c --console-log-level=error -c -x 16 -s 16 -k 1M "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/${model}.pth" -d ./assets/pretrained_v2 -o "${model}.pth"
done

# ORVC 모델은 별도의 URL에서 다운로드
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M "https://huggingface.co/ORVC/Ov2Super/resolve/main/f0Ov2Super40kD.pth" -d ./assets/pretrained_v2 -o "f0Ov2Super40kD.pth"
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M "https://huggingface.co/ORVC/Ov2Super/resolve/main/f0Ov2Super40kG.pth" -d ./assets/pretrained_v2 -o "f0Ov2Super40kG.pth"

python3.10 -m venv myprojectenv
source myprojectenv/bin/activate
# Python 패키지 설치
python3.10 -m pip install -r requirements.txt
python3.10 -m pip install mega.py gdown==4.6.0
python3.10 -m pip install google-cloud-texttospeech

# 다운로드 스크립트 실행
python download_files.py

export GOOGLE_APPLICATION_CREDENTIALS="/home/jhko2721/vridge/vridge-5f526-146273e2ebf7.json"
cd ~
wget 'https://drive.google.com/uc?export=download&id=1wdpgSMq4Lu6x8LZeRniFh6EFEKP4LAr5' -O vridge-5f526-146273e2ebf7.json

mv vridge-5f526-146273e2ebf7.json ./vridge
