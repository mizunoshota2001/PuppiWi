環境
raspi zero w
legacy lite OS

```bash
sudo apt install -y git python3-pip python3-venv
```

clone

```bash
cd && git clone https://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@github.com/mizunoshota2001/remote-puppet.git tmp && mkdir -p remote-puppet && cp -a tmp/RaspberryPi/* remote-puppet && rm -rf tmp

```
### pythonライブラリ
以下のpythonライブラリを使用しています
- keyboard - キーボード入力を扱うためのライブラリ

PyPlのインストール
```bash
pip install keyboard
```

# ラズパイ5用のセットアップ
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3-pip
pip3 install --upgrade pip
pip3 install keyboard
cd ~
git clone https://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@github.com/mizunoshota2001/remote-puppet.git tmp
mkdir -p remote-puppet
cp -a tmp/RaspberryPi/* remote-puppet
rm -rf tmp

```

## 一行にまとめたやつ
```bash
sudo apt update && sudo apt upgrade -y && sudo apt install -y git python3-pip && sudo apt remove python3-rpi.gpio -y && sudo pip3 install --upgrade pip --break-system-packages && sudo pip3 install keyboard --break-system-packages && sudo pip3 install rpi-lgpio --break-system-packages && cd ~ && git clone https://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@github.com/mizunoshota2001/remote-puppet.git tmp && mkdir -p remote-puppet && cp -a tmp/RaspberryPi/* remote-puppet && rm -rf tmp

```