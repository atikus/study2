import threading, time
# import time

# tLock = threading.Lock()


# def timer(name, delay, repeat):
#     tLock.acquire()
#     print("Timer : {} started".format(name))
#     while repeat>0:
#         time.sleep(delay)
#         print("{} : {}".format(name, time.ctime(time.time())))
#         repeat -= 1
#     print("Timer {} completed".format(name))
#     tLock.release()

# def Main():
#     t1 = threading.Thread(target=timer, args=("Timer1", 1, 3))
#     t2 = threading.Thread(target=timer, args=("Timer2", 1, 5))

#     t1.start()
#     t2.start()
    
#     print("Main completed")


class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        super().__init__()
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + "\n")
        f.close()
        for i in range(5):
            print("dosya yazma işlemi devam ediyor {}".format(i))
            time.sleep(2)
        print("Finished background file write to : " + self.out)

def Main():
    message = input("Mesajınız : ")
    background = AsyncWrite(message, "out.txt")
    background.start()
    print("The program can continue while it writes in another threads")

    # background.join()
    print("wait until thread was complete")
    time.sleep(20)


if __name__ == "__main__":
    Main()
    print("end......")