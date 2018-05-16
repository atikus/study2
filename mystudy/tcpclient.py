import socket
import json
import time


def Main():
    host = "127.0.0.1"
    port = 6000

    ages = {"dick": 23, "alan":34}
    message = json.dumps(ages)
    # msg = ""
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))


        with open("cat.jpeg", "rb") as f:
            filebytes = f.read()

        s.send(filebytes)
        data = s.recv(1024).decode("utf-8")
        s.close()


        resp = json.loads(data)
        print("Received from server : {}".format(resp["dick"]))
        time.sleep(0.7)
    
    

if __name__ == "__main__":
    Main()