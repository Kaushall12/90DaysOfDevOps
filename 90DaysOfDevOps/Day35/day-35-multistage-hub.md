#### Multi Stage Builds \& Docker Hub



##### Objective

Learn how to create optimized Docker images using multi-stage builds and push them to Docker Hub.



Single Stage Image



Dockerfile.single used Node base image.



Image Size: \~1GB



\## Multi Stage Image



Dockerfile.multistage used builder stage and minimal alpine image.



Image Size: \~120MB



\## Why Multi Stage is Smaller



Multi-stage builds remove build dependencies and keep only the final application artifact.



This reduces image size and improves security.



\## Docker Hub



Image pushed to Docker Hub:



kaushalpatel1284/multistage-app:v1



Commands used:



docker login  

docker tag node-multistage kaushalpatel1284/multistage-app:v1  

docker push kaushalpatel1284/multistage-app:v1  



\## Best Practices Applied



\- Used minimal alpine base image

\- Avoided unnecessary layers

\- Added non-root user

\- Used specific image tags

