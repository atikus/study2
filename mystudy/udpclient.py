import socket
import time
import argparse

def Main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-x", "--xxxx", help="x değeri girilecek", action="store_true")

    parser.add_argument("-p", "--port", help="Port Number", type=int)
    parser.add_argument("-ip", "--ipaddress", help="server Ip address")

    arg = parser.parse_args()

    if not arg.port:
        arg.port = 6001

    server = ("127.0.0.1", 6000)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", arg.port))

    message = 1000
    while message > 0:
        s.sendto(str(message).encode("utf-8"), server)
        data, addr = s.recvfrom(1024)
        data = data.decode("utf-8")
        print("Received from server : {} - address :{}".format(data, addr))
        #message = input("->")
        time.sleep(1)
        message -= 1
    
    s.close()

if __name__ == "__main__":
    Main()