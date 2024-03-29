import socket

HOST = '127.0.0.1' # '192.168.43.82'
PORT = 8081 # 2222
server = socket.socket()

while True:
    server.bind((HOST, PORT))
    print('[+] Server Started')
    print('[+] Listening For Client Connection ...')
    server.listen(1)
    client, client_addr = server.accept()
    print(f'[+] {client_addr} Client connected to the server')

    try:
        while True:
            command = input('Enter Command : ')
            command = command.encode()
            client.send(command)
            print('[+] Command sent')
    except:
        print('[+] Connection Closed')