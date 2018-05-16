# import multiprocessing
# from multiprocessing import Pool
# import time


f = [(x, y) for x in range(5) for y in range(5)]
print(f)
exit()


def spawn(num, num2):
    print("Spawned {} {}".format(num, num2))
    time.sleep(1)


if __name__ == "__main__xx":
    for i in range(10):
        p = multiprocessing.Process(target=spawn, args=(i, i+1))
        p.start()
        # p.join()

def job(num):
    return num * 2

def deneme():
    p = Pool(processes=20)
    data = p.map(job, range(15))
    p.close()
    print(data)

deneme()