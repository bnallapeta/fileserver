import sys
import requests
import json

print("This is an interactive python script developed to enable testing between you, the client and a File Service server \n")

# write switch conditions so that user can select CRUD operations

url = "http://nrbharath97.pythonanywhere.com/files/"
# url_local = "http://127.0.0.1:8000/api/files/"
operation = sys.argv[1]

def ls():
    res = requests.get(url)
    json_response = res.json()
    # print(json_response)
    for i in range(0, len(json_response)):
        print(json_response[i].get("fs_file").split("uploads/")[1])

def add(*args):
    for i in range(2, len(sys.argv)):
        # print(sys.argv[i])
        file_to_be_uploaded = {'fs_file' : open(sys.argv[i], 'rb')}
        res = requests.post(url, files=file_to_be_uploaded)
        print(res.json())

def remove():
    for i in range(2, len(sys.argv)):
        file_to_be_deleted = sys.argv[i]
        files = {'fs_file': file_to_be_deleted}
        # files['fs_file'] = file_to_be_deleted
        print(requests.delete(url, params=files))

def update():
    for i in range(2, len(sys.argv)):
        # print(sys.argv[i])
        file_to_be_uploaded = {'fs_file' : open(sys.argv[i], 'rb')}
        res = requests.put(url, files=file_to_be_uploaded)
        print(res.json())

def wc():
    res = requests.get(url + 'wc')
    print(res.json())

def fw():
    if len(sys.argv) > 2:
        order = sys.argv[2]
        options = {'order': order}
        res = requests.get(url + 'fw', params=options)
    else:        
        res = requests.get(url + 'fw')            
    print(res.json())
    
if operation == 'ls':
    ls()

if operation == "add":
    add()

if operation == "rm":
    remove()

if operation == 'update':
    update()

if operation == "wc":
    wc()

if operation == 'fw':
    fw()    