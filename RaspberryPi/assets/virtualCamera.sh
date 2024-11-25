#!/bin/bash

v4l2-ctl -v width=176,height=144,pixelformat=MJPG
sudo modprobe v4l2loopback -r
sudo modprobe v4l2loopback video_nr=2 card_label=VirtualCam exclusive_caps=1 max_buffers=2
ffmpeg -f v4l2 -i /dev/video0 -vf format=yuv420p -f v4l2 -r 5 /dev/video2
