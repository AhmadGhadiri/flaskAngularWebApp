FROM python:3.7.6-alpine3.10 as builder


RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /app
COPY requirements.txt /app


# Adding this back for the wait-for-postgres file
RUN apk add --update postgresql-client && rm -rf /var/cache/apk/*

RUN python3 -m pip install --trusted-host pypi.python.org -r requirements.txt  

COPY . /app
# execute the Flask app
CMD ["python", "src/main.py"]
