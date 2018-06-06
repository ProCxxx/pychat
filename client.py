import socket
import threading
import sys
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = input("Enter host: ")
host = str(input("Enter host: "))  # socket.gethostname()
name = str(input("Enter name: "))
port = int(input("Enter port: "))  # int(sys.argv[1])

s.connect((host, port))
os.system('clear')
print('Connected to', host)
print("Commands:\n- \"clear()\"\n- \"exit\"")
s.send(name.encode())
s.send(str("User connected: " + name).encode())


def unos():
    try:
        while True:
            inp = str(input(name + ": "))
            z = name + ": " + inp
            if (inp == "exit"):
                s.send(str("User disconnected: " + name).encode())
                s.close()
                exit(0)
            elif inp == "clear()":
                os.system("clear")
            else:
                s.send(z.encode())
    except Exception as e:
        s.send(str("User disconnected: " + name).encode())
        print(e)
        exit(0)


def read():
    while True:
        msg = str(s.recv(1024).decode())
        if len(msg):
            print("\n" + msg)


t1 = threading.Thread(target=unos)
t2 = threading.Thread(target=read)
try:
    t1.start()
    t2.start()
except Exception as e:
    print(e, end="\n\n\n\n")
    print("Bye bye ")
    exit(0)
