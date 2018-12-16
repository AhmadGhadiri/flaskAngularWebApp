# this is an official Python runtime, used as the parent image
FROM node:latest

RUN node --version

# Install the angular cli
RUN npm install -g @angular/cli@7.1.2
RUN ng --version



# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN npm install

# unblock port 80 for the Flask app to run on
# EXPOSE 80

# execute the Flask app
CMD ["ng", "serve", "--host", "0.0.0.0"]
