@echo off
setlocal enabledelayedexpansion

:: Chocolatey를 사용하여 필요한 도구들 설치
choco install git -y
choco install aria2 -y
choco install wget -y
choco install python -y

:: 리포지토리 복제
git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI ./RVC

:: 필요한 파일들을 다운로드합니다. 현재 폴더의 RVC/assets/pretrained_v2로 저장
if not exist ".\RVC\assets\pretrained_v2" mkdir ".\RVC\assets\pretrained_v2"

aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D32k.pth -d .\RVC\assets\pretrained_v2 -o D32k.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/D40k.pth -d .\RVC\assets\pretrained_v2 -o D40k.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G32k.pth -d .\RVC\assets\pretrained_v2 -o G32k.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/G40k.pth -d .\RVC\assets\pretrained_v2 -o G40k.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D32k.pth -d .\RVC\assets\pretrained_v2 -o f0D32k.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0D40k.pth -d .\RVC\assets\pretrained_v2 -o f0D40k.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G32k.pth -d .\RVC\assets\pretrained_v2 -o f0G32k.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/pretrained_v2/f0G40k.pth -d .\RVC\assets\pretrained_v2 -o f0G40k.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ORVC/Ov2Super/resolve/main/f0Ov2Super40kD.pth -d .\RVC\assets\pretrained_v2 -o f0Ov2Super40kD.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/ORVC/Ov2Super/resolve/main/f0Ov2Super40kG.pth -d .\RVC\assets\pretrained_v2 -o f0Ov2Super40kG.pth

:: 데이터셋 폴더 생성
if not exist ".\dataset" mkdir ".\dataset"

:: RVC 폴더로 이동
cd RVC

:: Python 패키지 설치
pip install -r requirements.txt
pip install mega.py
pip install gdown==4.6.0

:: wget을 사용하여 추가 파일 다운로드
wget https://huggingface.co/Rejekts/project/resolve/main/app.py -O app.py
wget https://huggingface.co/Rejekts/project/resolve/main/download_files.py -O download_files.py
wget https://huggingface.co/Rejekts/project/resolve/main/a.png -O a.png
wget https://huggingface.co/Rejekts/project/resolve/main/easy_sync.py -O easy_sync.py

:: 다운로드된 스크립트 실행
python download_files.py