FROM debian:stable

MAINTAINER Chris Kang <chris@wishbeen.com>

RUN  \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y autoremove && \
    apt-get -y install \
	libcurl4-openssl-dev \
	python-numpy \
  python-opencv \
	libimage-exiftool-perl \
	libopencv-dev \ 
	libjpeg-progs \ 
	libjpeg-dev \
	libpng-dev \ 
	libx264-dev \ 
	libass-dev \ 
	libvpx1 \ 
	libvpx-dev \ 
	libwebp-dev \
	libffi-dev \
	libssl-dev \
  python-lxml \
	webp \ 
	gifsicle \
	python-scipy \ 
	libcairo2-dev \ 
	gfortran \
	libopenblas-dev \ 
	liblapack-dev \ 
	python-pyexiv2 \ 
	git \ 
	redis-tools \
	redis-server \ 
	graphicsmagick \ 
	libgraphicsmagick++3 \ 
	libgraphicsmagick3 \
	libgraphicsmagick++1-dev \
	libgraphicsmagick1-dev \
	build-essential \
	python-pip \
	vim \
	locales \
	wget \  
	python-dev \ 
	libboost-python-dev && \
  apt-get clean

ENV HOME /root/
ENV SHELL bash
RUN localedef -i en_US -f UTF-8 en_US.UTF-8
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

WORKDIR /root
RUN pip install -U pip
RUN pip install coveralls
RUN wget http://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz -O /tmp/ffmpeg-release.tar.xz
RUN mkdir /tmp/ffmpeg-release
RUN tar -C /tmp/ffmpeg-release --strip 1 -xvf /tmp/ffmpeg-release.tar.xz
ENV PATH=/tmp/ffmpeg-release:$PATH
RUN git clone https://github.com/paranpi/thumbor.git
WORKDIR /root/thumbor
RUN make setup
VOLUME /root/thumbor
CMD ["/bin/bash"]
