# Project Title

File store service (HTTP server and a command line client)

## Description

A client-server application of a django web server for a file server and a python script for a client.
A containerized form of the Django server can be created from this source code and deployed in Kubernetes.

## Getting Started

The project is structured under 3 folders:
* server : Contains source code for the Django File server application that acts as a Web API server.
* client : A python script and a sample_files folder containing few sample text files.
* kubernetes : Contains source code for Dockerfile as well as Kubernetes resources i.e., Deployment and Service.

### Dependencies

* Python 3.9, Django 3.2.8, djangorestframework 3.12.4, requests 2.26.0
* Kubernetes 1.19, Docker 19.03.11

### Installation

* For the ease of usability, I have hosted the Django File Server at http://nrbharath97.pythonanywhere.com/api/files/ thus making it possible for you to test this application without any manual steps/installation required with respect to server end.

* For deploying this application in kubernetes environment, please follow the below steps:
    * Create a Docker Image
    On a machine with Docker installed, go to the path /kubernetes and run the below command:
    ```
    docker build -t django-docker .
    ```
    * Create a kubernetes deployment
    On a kubernetes cluster which also has the above generated docker image, run the below comnmand:
    ```
    kubectl apply -f deploy_django.yaml
    ```
    * Create a kubernetes service
    Run the below command to expose the deployment so that we can connect to it from outside the cluster
    ```
    kubectl apply -f service_django.yaml
    ```
    * Post these steps, you can verify that everything is good by running these commands:
    ```
    kubectl get pods
    kubectl get services
    ```
    * Tunnel a port from localhost:8000 to the NodePort assigned by kubernetes (can be obtained from  'kubectl get services')
    * Open localhost:8000/api/files in a browser.

* For testing from the client end,
    * Please download [@sample_files](https://github.com/nrbharath97/fileserver/tree/main/client/sample_files) folder where sample text files are added for testing
    * Please download the [@store.py](https://github.com/nrbharath97/fileserver/blob/main/client/store.py) to your local computer.
    * Local environment should have python and requests library installed
    * Instructions for installing python here - [@Install Python](https://www.python.org/downloads/)
    * Instructions for installing requests here - [@Install Requests](https://pypi.org/project/requests/)
    ```
    pip install requests:2.26.0
    ```

### Executing program

```
python store.py <cmd>
```

<cmd> can be one of the following values defined under Documentation


## Documentation

The list of supported api calls are listed below
```
#Lists the existing files present on the server
python store.py ls 

#Adds a new file file1.txt to the server
python store.py add sample_files/file1.txt

#Prints a message that file1.txt already exists and adds file2.txt to the server
python store.py add sample_files/file1.txt sample_files/file2.txt

#If the file already exists and the content is same, it prints an appropriate message; else updates the content of the new file onto the file on the server
python store.py put sample_files/file1.txt

#Deletes file1.txt on the server
python store.py rm file1.txt

#Prints the total number of words combined in all the files on the server
python store.py wc

#Prints the 10 most frequent words in all files on the server (default behavior)
python store.py fw

#Prints the 10 most frequent words in all files on the server
python store.py fw asc

#Prints the 10 least frequent words in all files on the server
python store.py fw dsc

```
