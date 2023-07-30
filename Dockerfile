FROM python:3.10-bullseye

RUN apt update 
RUN apt install -y gcc
RUN apt install -y vim
RUN apt install -y git
RUN apt install -y wget 

RUN apt install -y build-essential
RUN apt install -y python-dev
RUN apt install -y libopenblas-dev
RUN apt install -y libatlas-base-dev
RUN apt install -y libblas-dev
RUN apt install -y liblapack-dev
RUN apt install -y libsuitesparse-dev
ENV CPPFLAGS "-I/usr/include/suitesparse" 
RUN apt install -y libdsdp-dev
RUN apt install -y libfftw3-dev
RUN apt install -y libglpk-dev
RUN apt install -y libgsl-dev

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools

WORKDIR /workspace/cvx-opt

COPY ./ ./

RUN python3 -m pip install -r requirements.txt
