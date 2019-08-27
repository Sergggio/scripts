#########################################################
# Script to delete ElasticSearch logs using Jenkins job #
#########################################################

import paramiko
import requests
import os


# Get string parameters from Jenkins
host = os.getenv("HOST")
login = os.getenv("SSH_LOGIN")
# elastic_port = os.getenv("ELASTIC_PORT")  # No parameter
elastic_port = '9200'  # Constant! Need to be parametrized if we use another ElasticSearch port

# Debug
print("###")
print('Jenkins parameter HOST is ' + host)
print('Jenkins parameter SSH_LOGIN is ' + login)
print("###")

# SSH connect
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, port=22, username=login)

# Example: curl -XDELETE HOST:9200/YOUR_INDEX*
clean_logs = 'http://' + host + ':' + elastic_port + '/YOUR_PATH'
status_logs = 'http://' + host + ':' + elastic_port + '/_cat/indices?v'
curl = requests.delete(clean_logs)
print(curl.text)
status = requests.get(status_logs)
print(' ')
print('##############CURRENT INDEXES ARE##############')
print(' ')
print(status.text)
client.close()
