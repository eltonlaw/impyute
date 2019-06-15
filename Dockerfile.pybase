FROM ubuntu:16.04

RUN apk add make automake gcc g++ subversion python3-dev

RUN apt-get update && \
    apt-get -y install software-properties-common \
                       python-software-properties && \
    add-apt-repository -y ppa:deadsnakes/ppa && apt-get update && \
    apt-get autoclean

RUN apt-get -y install \
    python2.7 python2.7-dev \
    python3.5 python3.5-dev \
    python3.6 python3.6-dev \
    python3.7 python3.7-dev && \
    apt-get autoclean

RUN apt-get install wget && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python2.7 get-pip.py && \
    python3.5 get-pip.py && \
    python3.6 get-pip.py && \
    python3.7 get-pip.py && \
    rm get-pip.py && \
    apt-get autoclean

RUN python2.7 -m pip install --upgrade pip && \
    python3.5 -m pip install --upgrade pip && \
    python3.6 -m pip install --upgrade pip && \
    python3.7 -m pip install --upgrade pip
