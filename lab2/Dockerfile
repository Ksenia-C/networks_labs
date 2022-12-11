FROM ubuntu:20.04

WORKDIR /networks/tool
COPY . .
RUN apt-get update && apt-get install -y python3-pip iputils-ping


RUN pip install icmplib
RUN pip install validators

ENTRYPOINT ["python3", "mtu_searcher.py"]
