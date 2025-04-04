FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    git \
    wget \
    curl \
    unzip \
    vim \
    nano \
    libleptonica-dev \
    libicu-dev \
    libpango1.0-dev \
    libcairo2-dev \
    pkg-config \
    libtesseract-dev \
    ca-certificates \
    build-essential \
    autoconf \
    automake \
    libtool \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    zlib1g-dev \
    python3-pip \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && pip install opencv-python flask pytesseract pillow \
    && rm -rf /var/lib/apt/lists/*

# Tesseract 5.5.0 설치
WORKDIR /opt
RUN git clone https://github.com/tesseract-ocr/tesseract.git && \
    cd tesseract && \
    git checkout 5.5.0 && \
    ./autogen.sh && \
    ./configure && \
    make -j$(nproc) && \
    make install && \
    ldconfig && \
    make training && \
    make training-install

# 학습용 tessdata 디렉토리 생성
RUN mkdir -p /usr/share/tesseract-ocr/5/tessdata

# python alias 설정
RUN echo "alias python='python3'" >> /root/.bashrc
RUN echo "alias pip='pip3'" >> /root/.bashrc

# 작업 디렉토리
WORKDIR /data

CMD ["/bin/bash"]
