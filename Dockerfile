FROM registry.opensource.zalan.do/stups/ubuntu:latest

RUN apt-get update && apt-get -y install python3-pip libssl-dev && pip3 install -U stups


