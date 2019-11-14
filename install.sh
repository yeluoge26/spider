#!/usr/bin/env bash

ln -s /usr/bin/python3 /usr/local/bin/python
curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
chmod a+rx /usr/local/bin/youtube-dl

wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum install -y ./google-chrome-stable_current_*.rpm

wget https://chromedriver.storage.googleapis.com/78.0.3904.70/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
cp -r ./chromedriver /usr/local/bin/

rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
rpm -Uvh http://li.nux.ro/download/nux/dextop/el6/x86_64/nux-dextop-release-0-2.el6.nux.noarch.rpm
yum install ffmpeg ffmpeg-devel -y

pip3 install -r requirements.txt

LC_ALL=C.UTF-8 python -c 'print(u"\u2122");'

# build docker image
sudo docker build . -t javspider --network=host

# run shell
sudo docker run --network=host -it -v $PWD:/usr/src/app --entrypoint /bin/bash javspider