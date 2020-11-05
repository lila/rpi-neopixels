FROM balenalib/raspberrypi3
LABEL maintainer='karan bhatia'
RUN apt-get update
RUN apt install python3 python3-pip python3-setuptools
COPY src/rainbow_neopixels.py /
COPY src/requirements.txt /
RUN pip3 install -r requirements.txt
CMD ["/rainbow_neopixels.py"]
