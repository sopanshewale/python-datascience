# Docker Tutorial 

This is very short tutorial to get started with Docker & Start Coding for this Python Course

## What is Container? 

Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package.
By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings 
that machine might have that could differ from the machine used for writing and testing the code.


## What is Docker? 

Docker is a tool which helps:
* create
* deploy
* run applications 

by using containers. 

## How to Install Docker? 

Please refer to official Documentation - https://docs.docker.com/engine/installation/ 
For Windows - you need to download .msi file from https://docs.docker.com/docker-for-windows/. The installation is driven by easy GUI. 

You should be able to see output similar to following after successful installation: 

```
> docker --version
  Docker version 1.12.0, build 8eab29e, experimental
```


## Commands Important for our Course

###  Pull Required Container Image 

```
$docker pull sopanshewale/jupyter

```

### verify the images - following command confirms the image is in local repository

```
$ docker images
REPOSITORY                        TAG                 IMAGE ID            CREATED             SIZE
sopanshewale/jupyter              latest              cb789306bd1d        13 days ago         971.1 MB

```

### Start the instance

```
$docker run -d  -p 8888:8888 --name jupyter -v /Users/sopanshewale/datascience:/datascience -it sopanshewale/jupyter /bin/bash

```

Here "-p 8888:8888" is just forwarding 8888 port from container to 8888 port of host machine.  "/Users/sopanshewale/datascience/" directory from 
host machine is mounted on "/datascience" in container 

### Connect to Instance

```
$docker exec -it jupyter bash
# 

```
### To start Jupyter Notebook in Container 

```
# jupyter notebook --ip=0.0.0.0 --notebook-dir=/datascience

```

The output of above command looks similar to following:

```
root@bf9fe188724d:/# jupyter notebook --ip=0.0.0.0 --notebook-dir=/datasciecne
[I 14:11:03.661 NotebookApp] Serving notebooks from local directory: /datascience
[I 14:11:03.661 NotebookApp] 0 active kernels 
[I 14:11:03.661 NotebookApp] The Jupyter Notebook is running at: http://0.0.0.0:8888/?token=1c098aa05aa6f15fd263ce5efec32d8edbc0f81bc8b55b72
[I 14:11:03.662 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 14:11:03.663 NotebookApp] No web browser found: could not locate runnable browser.
[C 14:11:03.663 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://0.0.0.0:8888/?token=1c098aa05aa6f15fd263ce5efec32d8edbc0f81bc8b55b72


```


So you can access Jupyter Notebook on Host Machine at - http://localhost:8888?token=1c098aa05aa6f15fd263ce5efec32d8edbc0f81bc8b55b72


### Other Important Commands Frequently Used on Host Machine

```

$ docker ps -a
CONTAINER ID        IMAGE                  COMMAND             CREATED             STATUS              PORTS                    NAMES
bf9fe188724d        sopanshewale/jupyter   "/bin/bash"         5 minutes ago       Up 5 minutes        0.0.0.0:8888->8888/tcp   jupyter

$ docker stop jupyter
jupyter

$ docker rm jupyter
jupyter

$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

```



## References 

* [Docker Documentation Site](https://docs.docker.com/)
* [Docker Terminology](https://developers.redhat.com/blog/2016/01/13/a-practical-introduction-to-docker-container-terminology/)
* [Good Resource to Learn Docker - from Digital Ocean](https://www.digitalocean.com/community/tags/docker?type=tutorials)


