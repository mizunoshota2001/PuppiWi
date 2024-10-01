@echo off
ssh-keygen -R puppet.local
ssh -o StrictHostKeyChecking=no puppet@puppet.local "cd && git clone https://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@github.com/mizunoshota2001/remote-puppet.git tmp && mkdir -p remote-puppet && cp -a tmp/RaspberryPi/* remote-puppet && rm -rf tmp"
pause
