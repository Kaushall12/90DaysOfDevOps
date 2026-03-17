#### Docker Cheat Sheet



##### Container Commands

docker run -d image → Run container in background  

docker run -it image → Run container interactively  

docker ps → List running containers  

docker ps -a → List all containers  

docker stop <id> → Stop container  

docker rm <id> → Remove container  

docker exec -it <id> bash → Access container shell  

docker logs <id> → View logs  



##### Image Commands

docker build -t name . → Build image  

docker images → List images  

docker rmi <id> → Remove image  

docker pull image → Download image  

docker push image → Upload image  

docker tag image user/repo:tag → Tag image  



##### Volume Commands

docker volume create name → Create volume  

docker volume ls → List volumes  

docker volume inspect name → Inspect volume  

docker volume rm name → Remove volume  



##### Network Commands

docker network create name → Create network  

docker network ls → List networks  

docker network inspect name → Inspect network  

docker network connect net container → Connect container  



##### Docker Compose Commands

docker compose up → Start services  

docker compose up --build → Build \& start  

docker compose down → Stop services  

docker compose down -v → Remove volumes  

docker compose ps → List services  

docker compose logs → View logs  



##### Cleanup Commands

docker system prune -f → Remove unused data  

docker container prune → Remove stopped containers  

docker image prune → Remove unused images  

docker system df → Check disk usage  



##### Dockerfile Instructions

FROM → Base image  

RUN → Execute commands  

COPY → Copy files  

WORKDIR → Set working directory  

EXPOSE → Define port  

CMD → Default command  

ENTRYPOINT → Fixed command  



