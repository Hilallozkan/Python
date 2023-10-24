#Soru 4:Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

import math #pi sayısını kullanabilmek için math kütüphanesini koda import ile ekledim

YariCap = float(input("Lütfen hesaplamak istediğiniz dairenin yarıçapını giriniz:"))
PiSayisi = 3.14
Alan =  math.pi * (YariCap*YariCap)
Cevre = (2 * math.pi * YariCap)

print(f"Dairenin alanı:{Alan}")
print(f"Dairenin çevresi:{Cevre}")