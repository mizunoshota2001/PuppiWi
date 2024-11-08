#!/bin/bash

sudo apt install -y git python3-pip python3-venv
mkdir app
cd /home/puppiwi/app
python3 -m venv .venv
.venv/bin/python -m pip install flask rpi.gpio
cd /home/puppiwi
git clone https://github.com/mizunoshota2001/PuppiWi.git tmp
cp -a tmp/RaspberryPi/* app
rm -rf tmp
