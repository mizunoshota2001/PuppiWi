@echo off
set USER=puppiwi
set HOST=puppiwi.local
set SSH_KEY_PATH=
set CLONE_TOKEN=

set clone="git clone https://%CLONE_TOKEN%@github.com/.../....git .tmp"
set sparse="cd && git clone https://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@github.com/mizunoshota2001/remote-puppet.git tmp && mkdir -p remote-puppet && cp -a tmp/RaspberryPi/* remote-puppet && rm -rf tmp"