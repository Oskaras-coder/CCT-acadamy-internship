# Task

Let's dockerize your restaurants task:
1. Dockerfile:
   - Create Dockerfile.
   - For subsequent instructions create a base image that would have Python’s latest version.
   - Specify your working directory, bring all your project dependencies, and install them in your docker environment.
   - prepare a volume for your source code
2. docker-compose.yml:
   - Create a file called docker-compose.yml.
   - Make two services called: web, db.
   - web service:
     - The web service’s image should be the one defined via Dockerfile
     - The web container should listen to the default port for the Django app server (8000).
     - The web service must be dependent on db service.
     - In web service configuration specify a volume: copy all the code you have locally inside the web container. When using local development, a good practice is to set volumes in a presentation container. It allows you to restart the container and have all the code you have locally inside the container, without having to build it again. This makes development faster. But when deploying for production you would remove that part, and only keep the code inside the container image the moment you built it.
     - Each time the container is started, let every time apply all migrations and start the development server on the internal IP at the default Django port.
   - db service:
     - Specify Postgres image which is pulled from the Docker Hub registry as a based image on the db service (take the latest version of Postgres image).
     - Specify environment variables needed to execute Postgres image.
     - Add default Postgres image volumes path. Investigate where all the data will appear.
     - The db container should listen to the Postgres default port.
3. Use docker-compose commands which build, (re) create, and start containers.

# Goals
- Understand the differences between a virtual machine and Docker containers.
- Get an initial understanding of four major components of Docker:
  - Docker Client and Server
  - Docker Images
  - Docker Container
  - Docker Registry
- Learn the pros and cons of using Docker containers.
- Where and how to persist data, generated and used by Docker containers?
- Get initial understanding the main docker commands:
  - Information: `docker ps | docker ps -a | docker log [container_name] | docker inspect [container_name] | docker port [container_name] | docker images ls`.
  - Container lifecycle: `docker create [image] | docker run [image] | docker rm [container]`.
  - Image lifecycle: `docker build [url] | docker pull [image] | docker push [image] | docker rmi [image]`.
  - Start & stop: `docker start [container] | docker stop [container]`.

# Additional karma points:
- How to keep your images small? What does Alpine mean in Docker images? 
- Explore Docker environment variables behavior and find out Docker environment variables priority order. 
- Investigate what Docker system prune is. 
- Understand what Docker cache is. 
- Images scanning for security

# Material:
- https://docs.docker.com

