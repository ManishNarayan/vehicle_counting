FROM tensorflow/tensorflow:latest-devel-gpu-py3

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y apt-transport-https

RUN apt-get update && apt-get install -y python3-pip

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN apt update -y && apt install -y \
python3-dev \
libsm6 \
libxext6 \
libxrender-dev \
python3-tk

RUN pip install \
scipy \
numpy \
opencv-python \
Pillow \
argparse \
flask \
pandas \
tensorflow-gpu \
matplotlib


