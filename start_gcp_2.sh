#!/bin/bash


mkdir -p ./vridge
cd ./vridge

# RVC 프로젝트 클론
git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI ./RVC

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
wget 'https://drive.google.com/uc?export=download&id=1-6xE2uyrvHZfvQbe5E30pvvtBP78qnGy' -O vid1.pth
wget 'https://drive.google.com/uc?export=download&id=1-2DMgF8Iz9xByauAFHpch5sCTH7V9ppC' -O vid1.index
wget 'https://drive.google.com/uc?export=download&id=1wdpgSMq4Lu6x8LZeRniFh6EFEKP4LAr5' -O vridge-5f526-146273e2ebf7.json
mv vridge-5f526-146273e2ebf7.json ./vridge
mkdir -p vridge/test_db/uid1/vid1
mv vid1.pth vid1.index ./vridge/test_db/uid1/vid1

cd Vridge-AI
mv train.py tts_all.py tts_wav.py merge.py wraped_infer_cli.py ../vridge/
mv config.py ../vridge/RVC/configs/