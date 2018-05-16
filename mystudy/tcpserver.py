import socket
import json
import random
import time

def Main():
    host = "127.0.0.1"
    port = 6000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(10)
    print("waiting connection...")
    
    
    while True:
        conn, addr = s.accept()
        print("Connection from {}".format(addr))
        m_bytes = conn.recv(1024 * 1024)

        with open("ccc.jpeg", "wb") as f:
            f.write(m_bytes)



        # data = m_bytes.decode("utf-8")
        # data = data[1:]
        data = "ok"
        if not data:
            break
        print("From connected user: " + data)

        time.sleep(5)
        addVal = random.randint(5,15)

        ddd = json.loads('{"dick": 23, "alan":34}')
        for k, v in ddd.items():
            ddd[k] = int(v) + addVal

        data = json.dumps(ddd)

        print("Sending: {}".format(data))
        conn.send(data.encode("utf-8"))
        conn.close()
    
    

if __name__ == "__main__":
    Main()