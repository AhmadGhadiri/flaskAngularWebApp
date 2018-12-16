# this is an official Python runtime, used as the parent image
FROM alpine:3.7 


# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN apk add --no-cache libffi-dev 
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps libc-dev unixodbc-dev g++ musl-dev postgresql-dev && \
 apk add --no-cache python-dev && \
 apk add --no-cache python3-dev && \
 apk add --no-cache py-pip build-base
RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/main" > /etc/apk/repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h


RUN python --version
RUN python3 --version
RUN python3 -m pip install --trusted-host pypi.python.org -r requirements.txt  
#RUN python3 -m pip install --trusted-host pypi.python.org -r requirements.txt
RUN apk add --update postgresql-client && rm -rf /var/cache/apk/* 

# unblock port 80 for the Flask app to run on
EXPOSE 5000

# execute the Flask app
CMD ["python", "src/main.py"]
