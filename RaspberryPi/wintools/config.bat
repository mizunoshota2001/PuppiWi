@echo off
set USER=puppiwi
set HOST=puppiwi.local
set SSH_KEY_PATH=
set CLONE_TOKEN=

set clone="git clone https://%CLONE_TOKEN%@github.com/.../....git .tmp"
set sparse="cd && git clone https://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@github.com/mizunoshota2001/remote-puppet.git tmp && mkdir -p remote-puppet && cp -a tmp/RaspberryPi/* remote-puppet && rm -rf tmp"