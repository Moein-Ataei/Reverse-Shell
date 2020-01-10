import socket
import sys

host = ''
port = 9999


def create_socket():
    try:
        global host
        global port
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print(f"Socket Creation Error: {msg}")


def socket_bind():
    try:
        global host
        global port
        global s
        s.bind((host, port))
        print(f"Binding socket to port: {port}")
        s.listen(5)
    except socket.error as msg:
        print(f"Socket Binding Error: {msg} \n Retrying...")
        socket_bind()


def socket_accept():
    conn, address = s.accept()
    print(f"Connection has been established | IP: {address[0]} | Port: {address[1]}")
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        
        if len(cmd) > 0:
            conn.send(str.encode(cmd))
            clientResponse = conn.recv(1024*4).decode()
            print(clientResponse, end='')


def main():
    create_socket()
    socket_bind()
    socket_accept()


main()