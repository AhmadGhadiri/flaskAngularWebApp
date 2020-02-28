# this is an official Python runtime, used as the parent image
FROM node:latest

RUN node --version

# Install the angular cli
RUN npm install -g @angular/cli@9.0.4



# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
COPY package.json /app

# execute everyone's favorite pip command, pip install -r
RUN npm install

COPY . /app

# unblock port 80 for the Flask app to run on
# EXPOSE 80

# execute the Flask app
CMD ["ng", "serve", "--host", "0.0.0.0"]
