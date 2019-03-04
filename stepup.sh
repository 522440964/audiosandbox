#!/usr/bin/env bash

add-apt-repository ppa:jonathonf/ffmpeg-4
apt-get update
apt-get install ffmpeg
ffmpeg -version
pip3 install pydub