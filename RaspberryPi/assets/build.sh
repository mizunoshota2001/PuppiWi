#!/bin/bash

sudo apt install -y git python3-pip python3-venv
mkdir app

cd /home/puppiwi/app
python3 -m venv .venv
.venv/bin/python -m pip install flask rpi.gpio

sudo touch /etc/systemd/system/puppiwi.service
sudo cp -a  assets/puppiwi.service /etc/systemd/system/puppiwi.service
sudo systemctl daemon-reload
sudo systemctl unmask puppiwi.service
sudo systemctl enable puppiwi.service

cd /home/puppiwi
git clone https://github.com/mizunoshota2001/PuppiWi.git tmp
cp -a tmp/RaspberryPi/* app
rm -rf tmp
