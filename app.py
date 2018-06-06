import socket
import threading
# import sys
import time
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print("Host: " + str(host))
port = 8080  # int(sys.argv[1])
s.bind((host, port))

s.listen(10)
users = []
print("Server initialised on port " + str(port))
print("Waiting for connections...")


def accConns(s):
    while True:
        c, addr = s.accept()
        name = str(c.recv(1024).decode())
        toadd = {'s': c, 'name': name, 'id': round(time.time() * random.randint(1000, 9999))}
        users.append(toadd)
        print('Got connection from', addr)
        t = threading.Thread(target=unos, args=(c, toadd['id'], name))
        t.start()


def unos(c, index, name):
    while True:
        novo = str(c.recv(1024).decode())
        if novo == '':
            novo = "User disconnected: "
        print(novo)
        broad(novo, index)
        if novo[:19] == "User disconnected: ":
            for i in range(len(users)):
                if index == users[i]['id']:
                    users[i]['s'].close()
                    del users[i]
                    break
            return


def broad(msg, fake):
    for i in range(len(users)):
        if users[i]['id'] != fake:
            users[i]['s'].send(msg.encode())


try:
    accConns(s)
except KeyboardInterrupt:
    s.shutdown(1)
    s.detach()
    s.close()
    print("Bye bye")
    exit(0)
finally:
    exit(0)
