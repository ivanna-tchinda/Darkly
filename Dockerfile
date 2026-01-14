FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3
RUN apt install -y python3-pip
COPY . .

RUN pip3 install -r requirements.txt

CMD ["/usr/bin/python3", "script.py"]