#### Docker Images \& Container Lifecycle





##### 1\. Docker Images



Docker images are read-only templates used to create containers.  

A container is a running instance of an image. Multiple containers can be created from the same image.



Pull images from Docker Hub:



```bash

docker pull nginx

docker pull ubuntu

docker pull alpine



##### 

##### 2\. Image Layers



###### Check image layer history:



docker image history nginx



###### Observation:



Each line represents a layer in the Docker image.



Some layers show a size while others show 0B.



###### Explanation:



Docker images are built using layers. Each command used when building an image creates a new layer.



###### Benefits of layers:



Faster builds due to caching



Efficient storage usage



Layers can be shared between images



Smaller updates when pushing images





##### 3\. Container Lifecycle



###### Create container without starting:



docker create --name lifecycle-demo nginx



###### Start container:



docker start lifecycle-demo



###### Pause container:



docker pause lifecycle-demo



###### Unpause container:



docker unpause lifecycle-demo



###### Stop container:



docker stop lifecycle-demo



###### Restart container:



docker restart lifecycle-demo



###### Kill container:



docker kill lifecycle-demo



###### Remove container:



docker rm lifecycle-demo



###### Check container states:



docker ps -a

