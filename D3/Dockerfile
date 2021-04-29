
FROM ubuntu:latest 

RUN apt-get -y update && apt-get install -y 

RUN apt-get -y install clang 

RUN apt-get install -y libnl-genl-3-dev
RUN apt-get install -y libmnl-dev
RUN apt-get -y install libmnl-dev
RUN apt-get -y install libnl-3-dev 
RUN apt-get -y install libiw-dev
RUN apt-get -y install libtool
RUN apt-get -y install libpcap-dev
RUN apt -y install libssl-dev
RUN apt-get install pthread
RUN apt-get install libpthread-stubs0-dev

FROM gcc:latest

COPY . /usr/src/c_test 

WORKDIR /usr/src/c_test 

RUN gcc -g my_scanner.c -o my_scanner -lssl -lcrypto -pthread -lmnl -lpcap -liw

CMD ["./my_scanner wlan0"]

