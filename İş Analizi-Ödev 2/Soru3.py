#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

import math

sayi1= int(input("Lütfen birinci sayıyı giriniz."))
sayi2=int(input("Lütfen ikinci sayıyı giriniz."))

EBOB = math.gcd(sayi1,sayi2)
EKOK = (sayi1*sayi2)/EBOB

print("Girdiğiniz sayıların ebobu:", EBOB)
print("Girdiğiniz sayıların ekoku:", EKOK)