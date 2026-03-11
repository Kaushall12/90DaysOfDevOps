#### Dockerfile: Build Your Own Images



##### 1\. Your First Dockerfile



Created a folder called `my-first-image`.



Dockerfile:



```dockerfile

FROM ubuntu:latest



RUN apt-get update \&\& apt-get install -y curl



CMD \["echo", "Hello from my custom image!"]



Build the image:



docker build -t my-ubuntu:v1 .



Run the container:



docker run my-ubuntu:v1



Output:



Hello from my custom image!



Observation:



The container runs the default command defined in CMD and prints the message.



##### 2\. Dockerfile Instructions



Example Dockerfile using common instructions:



FROM ubuntu:latest



RUN apt-get update \&\& apt-get install -y curl



WORKDIR /app



COPY hello.txt .



EXPOSE 8080



CMD \["cat", "hello.txt"]



###### Explanation of instructions:



FROM → Defines the base image.

RUN → Executes commands during image build.

COPY → Copies files from host system into the container image.

WORKDIR → Sets the working directory inside the container.

EXPOSE → Documents the port the container will use.

CMD → Default command executed when the container starts.

