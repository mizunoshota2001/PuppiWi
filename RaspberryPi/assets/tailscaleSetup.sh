#!/bin/bash

sudo apt-get install apt-transport-https
curl -fsSL https://tailscale.com/install.sh | bash
sudo tailscale up