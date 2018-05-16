# bu fonk her yeni çağrılışında baştan başlıyor.
def deneme():
    for i in range(5):
        yield i*i*i

for j in deneme():
    print(j)

for j in deneme():
    print(j)

print("= "*40)

# bu bir kere kullanılıyor. ve kendini mem den siliyor.
generator = (x*x*x for x in range(5))


for j in generator:
    print(j)

for j in generator:
    print(j)

