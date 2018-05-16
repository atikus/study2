import socket

def Main():
    host = "127.0.0.1"
    port = 7000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    with open("cat.jpeg", "rb") as f:
        data = f.read()
    
    s.send(data)
    rcv = s.recv(1024).decode("utf-8")

    print(rcv)

    s.close()

if __name__ == "__main__":
    Main()
    