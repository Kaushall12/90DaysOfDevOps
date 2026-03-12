#### Docker Volumes \& Networking



##### 1\. The Problem: Container Data Loss



Ran a PostgreSQL container:



docker run -d --name postgres-test -e POSTGRES\_PASSWORD=pass -p 5432:5432 postgres





##### 2\. Named Volumes



Created a Docker volume:



docker volume create postgres-data



Verified the volume:



docker volume ls



Started PostgreSQL container with volume:



docker run -d \\

--name postgres-test \\

-e POSTGRES\_PASSWORD=pass \\

-v postgres-data:/var/lib/postgresql/data \\

postgres



Added data inside the database.



##### 

##### 3\. Bind Mounts



Created a folder on the host machine:



mkdir mywebsite

cd mywebsite



Created an HTML file:



<html>

<h1>Hello from Docker Bind Mount</h1>

</html>



Started Nginx container with bind mount:



docker run -d \\

-p 8080:80 \\

-v $(pwd):/usr/share/nginx/html \\

nginx







##### 4\. Docker Networking Basics



Listed Docker networks:



docker network ls



Inspected default bridge network:



docker network inspect bridge



Ran two containers:



docker run -dit --name container1 ubuntu

docker run -dit --name container2 ubuntu



Tried ping by container name:



docker exec container1 ping container2





##### 5\. Custom Networks



Created a custom network:



docker network create my-app-net



Ran two containers on the network:



docker run -dit --name app1 --network my-app-net ubuntu

docker run -dit --name app2 --network my-app-net ubuntu



Tested connectivity:



docker exec app1 ping app2

