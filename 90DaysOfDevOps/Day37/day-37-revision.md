#### Docker Revision



##### Self Assessment



Run container → ✅  

Manage containers/images → ✅  

Image layers \& caching → ✅  

Dockerfile writing → ✅  

CMD vs ENTRYPOINT → ⚠️ Shaky  

Volumes → ✅  

Networks → ✅  

Docker Compose → ✅  

Environment variables → ✅  

Multi-stage builds → ✅  

Docker Hub → ✅  

Healthchecks → ⚠️ Shaky  



\---



##### Quick Fire Answers



1\. Image vs Container  

Image is a blueprint. Container is a running instance.



2\. Data inside container  

It is lost when container is removed unless stored in volume.



3\. Container communication  

Containers communicate using service names on the same network.



4\. docker compose down -v  

Removes containers + volumes (data also deleted).



5\. Multi-stage builds  

Reduce image size by keeping only final artifacts.



6\. COPY vs ADD  

COPY copies files. ADD can also download and extract.



7\. -p 8080:80  

Maps host port 8080 to container port 80.



8\. Check Docker disk usage  

docker system df  



\---



##### Weak Areas



1\. CMD vs ENTRYPOINT  

CMD can be overridden, ENTRYPOINT cannot.



2\. Healthchecks  

Used to check if service is ready before starting dependent services.



\---



##### What I Learned



Docker concepts are now clearer including containers, images, networking, and multi-container applications.



Hands-on practice with Docker Compose and multi-stage builds helped me understand real-world DevOps workflows.

