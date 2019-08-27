#########################################################
# Script for log files ERRORs parsing using Jenkins job #
#########################################################

from scp import SCPClient
import paramiko
import os


# Get string parameters from Jenkins
host = os.getenv("HOST")
login = os.getenv("SSH_LOGIN")
target_pach = os.getenv("TARGET_PATH")
show_warnings = os.getenv("WARNINGS")
jenkins_path = os.getcwd()

# Debug info
print("###")
print('Jenkins parameter HOST is ' + host)
print('Jenkins parameter SSH_LOGIN is ' + login)
print('Jenkins $WORKSPACE is ' + jenkins_path)
print("###")

# SSH connect
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, port=22, username=login)

# Copy log files from your system to Jenkins
logs_path = target_pach + '/logs'

with SCPClient(client.get_transport()) as scp:
    scp.get(logs_path + '/file.log', jenkins_path + '/file.log')
scp.close()


# Function to parse file for ERRORs and save it to .txt file
def parseFile(filename):
    parseWord = 'ERROR '
    dataError = []
    for line in data:
        if line.__contains__(parseWord):
            dataError.append(line)
    # Add exceptions to cut from log
    result = [i for i in dataError if not i.startswith('ERROR_EXCEPTION')]
    outFile = open(filename, "w")
    for line in result:
        outFile.write(line)
        outFile.write("\n")
    outFile.close()


# Open log file, parse it and save to parsed__errors.txt
with open(jenkins_path + '/file.log', 'rt') as file_log:
    data = file_log.readlines()
    parseFile(filename='parsed_errors.txt')
