# A website hosted on Docker

This is a simple website that is using containers to host the website. The website can be built on top of a container and it can be run using that container and a postgres container.


## Build

Build the container for the project:
```bash
$ docker build -t webApp .
```

## Run the website

1. Run a postgres container:
```bash
$ docker run --name online-exam-db -p 5432:5432 -e POSTGRES_DB=online-exam -e POSTGRES_PASSWORD=0NLIN3-ex4m -d postgres
```

2. Find the host, the default is __172.17.0.2__
```bash
$ docker inspect online-exam-db | grep IPAddress
```

3. Change the host address in the main.py if needed

4. Run the container for the application
```bash
$ docker run -d --name webapp --link online-exam-db:postgres --volume=/home/ahmad/webApp:/app -p 5002:5000 dockerwebapp
```

5. Open the website in ```http://localhost:5002```

