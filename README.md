# Project Title

File store service (HTTP server and a command line client)

## Description

A client-server application of a django web server for a file server and a python script for a client.

## Getting Started

### Dependencies

* Python 3.9, Django 3.2.8, djangorestframework 3.12.4, requests 2.26.0

### Installing

* For the ease of use, I have hosted the Django File Server on pythonanywhere.com thus making it possible for you to test this application without any installation required.
* For testing from the client end,
    * Please download [@sample_files](https://github.com/nrbharath97/fileserver/tree/main/sample_files) folder where sample text files are added for testing
    * Please download the [@store.py](https://github.com/nrbharath97/fileserver/blob/main/store.py) to your local computer.
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
python store.py ls -- lists the existing files present on the server
python store.py add sample_files/file1.txt -- Adds a new file file1.txt to the server
python store.py add sample_files/file1.txt sample_files/file2.txt -- Prints a message that file1.txt already exists and adds file2.txt to the server
python store.py put sample_files/file1.txt -- If the file already exists and the content is same, it prints an appropriate message; else updates the content of the new file onto the file on the server.
python store.py rm file1.txt -- Deletes file1.txt on the server
python store.py wc -- Prints the total number of words combined in all the files on the server
python store.py fw -- Prints the 10 most frequent words in all files on the server (default behavior)
python store.py fw asc -- Prints the 10 most frequent words in all files on the server
python store.py fw dsc -- Prints the 10 least frequent words in all files on the server
```
