#### Docker Compose: Multi-Container Basics



##### 1\. Verify Docker Compose



Checked Docker Compose installation:



```bash

docker compose version



Docker Compose allows running multiple containers using a single configuration file called docker-compose.yml.



##### 2\. First Docker Compose File



Created folder:



mkdir compose-basics

cd compose-basics



Created docker-compose.yml:



version: "3"



services:

&nbsp; web:

&nbsp;   image: nginx

&nbsp;   ports:

&nbsp;     - "8080:80"



Start container:



docker compose up -d



Access in browser:



http://localhost:8080



Stop containers:



docker compose down



Observation:



Docker Compose created the container automatically using the configuration file.



##### 3\. Two-Container Setup (WordPress + MySQL)



Created docker-compose.yml:



version: "3"



services:

&nbsp; db:

&nbsp;   image: mysql:5.7

&nbsp;   restart: always

&nbsp;   environment:

&nbsp;     MYSQL\_ROOT\_PASSWORD: example

&nbsp;     MYSQL\_DATABASE: wordpress

&nbsp;     MYSQL\_USER: wordpress

&nbsp;     MYSQL\_PASSWORD: wordpress

&nbsp;   volumes:

&nbsp;     - db\_data:/var/lib/mysql



&nbsp; wordpress:

&nbsp;   image: wordpress:latest

&nbsp;   restart: always

&nbsp;   ports:

&nbsp;     - "8000:80"

&nbsp;   environment:

&nbsp;     WORDPRESS\_DB\_HOST: db

&nbsp;     WORDPRESS\_DB\_USER: wordpress

&nbsp;     WORDPRESS\_DB\_PASSWORD: wordpress

&nbsp;     WORDPRESS\_DB\_NAME: wordpress

&nbsp;   depends\_on:

&nbsp;     - db



volumes:

&nbsp; db\_data:



Start services:



docker compose up -d



Open WordPress in browser:



http://localhost:8000



Observation:



WordPress automatically connected to the MySQL container using the service name db.



Stopped and restarted:



docker compose down

docker compose up -d



Result:



WordPress data remained because of the named volume db\_data.



##### 4\. Docker Compose Commands



Start services in detached mode:



docker compose up -d



View running services:



docker compose ps



View logs of all services:



docker compose logs



Follow logs in real time:



docker compose logs -f



View logs of specific service:



docker compose logs wordpress



Stop services without removing:



docker compose stop



Remove containers, networks, and volumes:



docker compose down



Rebuild services:



docker compose up --build

