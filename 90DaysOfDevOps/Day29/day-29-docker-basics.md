#### Introduction to Docker



##### 1\. What is Docker?



Docker is a containerization platform that allows developers to package applications along with their dependencies into lightweight containers.



Containers ensure that applications run consistently across different environments such as development, testing, and production.



---



##### Why Do We Need Containers?



Containers solve the problem of "it works on my machine but not on yours".



Benefits of containers:



\* Consistent environments across systems

\* Lightweight compared to virtual machines

\* Faster startup time

\* Easy to deploy and scale applications

\* Isolation between applications



---



##### Containers vs Virtual Machines



Virtual Machines:



\* Run a full operating system

\* Require a hypervisor

\* Heavy and slow to start



Containers:



\* Share the host OS kernel

\* Lightweight and faster

\* Start in seconds

\* Use fewer system resources



---



##### Docker Architecture



Docker consists of several components:



Docker Client  

The command line interface used to interact with Docker.



Docker Daemon  

The background service responsible for building, running, and managing containers.



Docker Images  

Templates used to create containers.



Docker Containers  

Running instances of Docker images.



Docker Registry  

A repository where Docker images are stored (e.g., Docker Hub).



---



##### Docker Architecture Flow



Developer → Docker CLI → Docker Daemon → Docker Images → Docker Containers



Images are stored in Docker Registry (Docker Hub) and pulled when needed.



---



##### 2\. Installing Docker



Verify Docker installation:



docker --version



Start Docker service:



sudo systemctl start docker



Enable Docker at boot:



sudo systemctl enable docker



---



##### Run Hello World Container



docker run hello-world



This command:



\* Pulls the hello-world image from Docker Hub

\* Creates a container

\* Runs the container

\* Prints a success message



---

##### 3\. Running Containers



Run Nginx container:



docker run -d -p 8080:80 --name my-nginx nginx



Explanation:



\* -d → Run container in background

\* -p 8080:80 → Map port 8080 on host to port 80 inside container

\* --name → Assign a custom container name



Access in browser:



http://localhost:8080



---



Run Ubuntu container in interactive mode:



docker run -it ubuntu



Flags:



\* -i → Interactive mode

\* -t → Terminal access



---



##### 4\. Container Management Commands



List running containers:



docker ps



List all containers:



docker ps -a



Stop container:



docker stop my-nginx



Remove container:



docker rm my-nginx



---



##### 5\. Detached Mode



Run container in detached mode:



docker run -d nginx



Detached mode runs containers in the background.



---



##### 6\. Container Logs



Check container logs:



docker logs my-nginx



---



##### 7\. Execute Command Inside Container



Run a command inside running container:



docker exec -it my-nginx bash



This allows you to interact with the container shell.



---



##### Key Learnings



\* Docker containers package applications and dependencies together

\* Containers are lightweight compared to virtual machines

\* Docker images act as templates for containers

\* Docker Hub is used to store and pull images

\* Containers can run interactively or in detached mode

