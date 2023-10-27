#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
a=1
b=1
n=20

fibonacci= [1,1]

for x in range(2,n):
    next = fibonacci[x-1]+fibonacci[x-2]
    fibonacci.append(next)

    print(fibonacci)
    