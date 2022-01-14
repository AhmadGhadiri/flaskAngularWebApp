# A website hosted on Docker

This is a simple website that is using containers to host the website. The website can be built on top of multiple containers and it uses docker-compose to orchestrate those containers. 

## Build
Build the container for the project:
```bash
$ docker-compose build
```

## Run the website
```bash
$ docker-compose up 
```

## Open the website
```http://localhost```

## Auth0
In Auth0 website make sure that you have **Token Endpoint Authentication Method** set to _None_.
Also 
set the _Allowed Callback URLs_ and _Allowed logout URLs_ to ```http://localhost, http://localhost:4200```
and in the Advanced settings under the application, under the Grant Types tab, check ```Authorization Code```,
that way the auth0/auth0-angular will work as expected.
