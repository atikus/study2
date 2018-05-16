import socket

def Main():
    host, port = "127.0.0.1", 7000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))

    s.listen(5)

    conn, addr = s.accept()

    pic = b''
    while True:
        data = conn.recv(7223)
        pic += data
        if len(data) < 7223: break
    
    print(len(pic))

    with open("img/c1.jpeg","wb") as f:
        f.write(pic)
    

    conn.send(("bilgi alındı - {}".format(addr)).encode())
    
    s.close()

    conn.close()

if __name__ == "__main__":
    Main()

    
    
