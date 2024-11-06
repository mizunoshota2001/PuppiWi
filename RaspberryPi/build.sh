#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3-pip python3-venv
sudo pip3 install flask keyboard
cd ~
git clone https://github.com/mizunoshota2001/remote-puppet.git tmp
mkdir -p remote-puppet
cp -a tmp/RaspberryPi/* remote-puppet
rm -rf tmp