#!/bin/bash

sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y python3.10
sudo apt-get install -y python3.10-distutils

sudo apt install -y python3-pip


sudo apt install -y ffmpeg

echo "alias python=python3.10" >> ~/.bashrc
echo "alias python3=python3.10" >> ~/.bashrc
echo "export PATH=\$PATH:/usr/bin/python3.10" >> ~/.bashrc
echo "export PATH=\$HOME/.local/bin:\$PATH" >> ~/.bashrc
export PATH="$PATH:/usr/bin/python3.10"
export PATH="$HOME/.local/bin:$PATH"
source ~/.bashrc