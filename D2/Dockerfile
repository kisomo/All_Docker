
FROM ubuntu:latest 

RUN apt-get -y update && apt-get install -y 

RUN apt-get -y install clang 

COPY . /usr/src/c_test 

WORKDIR /usr/src/c_test 

RUN clang++ -o intro2 intro2.c 

CMD ["./intro2"]

