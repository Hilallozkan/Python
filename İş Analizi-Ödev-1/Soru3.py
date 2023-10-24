#Soru 3:Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

Sayi1 = int(input("Lütfen birinci sayınızı giriniz:"))
Sayi2 = int(input("Lütfen ikinci sayınızı giriniz:"))
Sayi3 = int(input("Lütfen üçüncü sayınızı giriniz:"))

if Sayi1 > Sayi2 and Sayi1>Sayi3 :
   print(f"Girdiğiniz en büyük sayı:{Sayi1}")
elif Sayi2> Sayi1 and Sayi2>Sayi3 :
   print(f"Girdiğiniz en büyük sayı:{Sayi2}")
else :
   print(f"Girdiğiniz en büyük sayı:{Sayi3}")