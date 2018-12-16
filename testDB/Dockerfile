# this is an official Python runtime, used as the parent image
FROM centos 

RUN yum install -y postgresql.x86_64
# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app


# execute the Flask app
# CMD ["psql", "postgresql://postgres:0NLIN3-ex4m@localhost:5432/online-exam"]
