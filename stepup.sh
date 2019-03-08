#!/usr/bin/env bash

add-apt-repository ppa:jonathonf/ffmpeg-4
apt-get update
apt-get install ffmpeg
ffmpeg -version
pip install pydub
pip install numpy
pip install scipy
pip install internetarchive