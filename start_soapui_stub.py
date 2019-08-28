#####################################################
# Script to restart SOAP UI stubs using Jenkins job #
#####################################################

import paramiko
import requests
import os
import time
from scp import SCPClient


# Get string parameters from Jenkins
host = os.getenv("HOST")
login = os.getenv("SSH_LOGIN")
path = os.getenv("TARGET_PATH")
mock_port = os.getenv("MOCK_PORT")
workspace = os.getcwd().replace('/script', '')

# Debug
print("###")
print('Jenkins parameter HOST is ' + host)
print('Jenkins parameter MOCK_PORT is ' + mock_port)
print('Jenkins parameter SSH_LOGIN is ' + login)
print('Jenkins parameter TARGET_PATH is ' + path)
print('Jenkins $WORKSPACE is ' + workspace)
print("###")

# SSH connect
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, port=22, username=login)

# Copy .xml with SOAP stubs to the server
path_to_soap = '/home/' + login + '/' + path + '/soap/'
print(path_to_soap)
with SCPClient(client.get_transport()) as scp:
    scp.put(workspace + '/MOCK_FILE.xml', path_to_soap + '/MOCK_FILE.xml')
scp.close()

# Stop and start SOAP stubs
stdin, stdout, stderr = client.exec_command("cd mock/soap && "
                                            "chmod +x mock_run.sh && "
                                            "./mock_run.sh stop && "
                                            "./mock_run.sh start MOCK_PORT && "
                                            "./mock_run.sh status")
for line in stdout:
    print('... ' + line.strip('\n').encode('utf-8'))
for line in stderr:
    print('... ' + line.strip('\n').encode('utf-8'))

client.close()

# Ping stub before using
curl = ''
soap_mock = 'http://' + host + ':' + mock_port + '/MOCK_NAME'
while curl == '':
    try:
        curl = requests.get(soap_mock)
        head_response = '<Response [200]>'
        print(curl)
        if str(curl) == str(head_response):
            print("Recieved response code 200 from SOAP mock. Mock is up.")
            break
    except:
        print("Connection refused by the server..")
        time.sleep(2)
        print("Sending curl again..")
        continue
