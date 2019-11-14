FROM jrottenberg/ffmpeg:3.4-ubuntu

ENV LC_ALL=C.UTF-8

RUN apt-get -yqq update && \
    apt-get autoremove -y && \
    apt-get clean -y

RUN apt-get install -y apt-utils

RUN apt-get install -y youtube-dl && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y wget unzip

#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
#    dpkg -i google-chrome-stable_current_amd64.deb

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable


RUN wget https://chromedriver.storage.googleapis.com/78.0.3904.70/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    cp -r ./chromedriver /usr/local/bin/


WORKDIR /usr/src/app
ADD . /usr/src/app

RUN pip3 install -r requirements.txt

CMD ["python3", "run.py", "--help"]
ENTRYPOINT [ "python3", "run.py" ]