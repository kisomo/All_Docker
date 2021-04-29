
FROM gcc:latest 

COPY . /usr/src/c_test 

WORKDIR /usr/src/c_test

RUN  gcc -g tcpserver.c -o tcpserver

CMD ["./tcpserver"]


