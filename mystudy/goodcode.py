# 1
cities = ["Amsterdam", "Berlin", "New York", "London"] 
for x,y in enumerate(cities):
    print(x+1, y, sep=". ")

# 2 listeyi zipleme
x_list = [1,5,6]
y_list = [8,2,4,9]
for x,y in zip(x_list, y_list):
    print(x,y)

# 3 atama
n = 1
m = 7
m, n = n, m
print(n,m)

# 4 dict den değer almak yoksa default değer alınır
ages = {"dick": 23, "alan":34}
c = ages.get("ahmet", -1)
print(c)

# 5 döngülerde break
needle = "d"
haystack = ["a","b","d"]
for letter in haystack:
    if needle == letter:
        print("Found")
        break
else: # if no break occured
    print("Not Found")

i=0
while i<10:
    print(i)
    i += 1
    break
else:
    print("tamamlandı")



# 6 read lines from a file
with open("start.py") as f:
    for line in f:
        print(line)

# 7 hata olsada finally çalışır!!!!
print("Converting...")
try:
    print(int("1"))
finally:
    print("Done")


print("son")
