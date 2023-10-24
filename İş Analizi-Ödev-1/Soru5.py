#Soru 5:Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
IsPolindrom = (input("Lütfen kontrol etmek istediğiniz sayıyı giriniz:"))

TersSayi = IsPolindrom[::-1]

if IsPolindrom == TersSayi:
  print("Bu bir polindrom sayıdır")
else:
  print("Bu bir polindrom sayı değildir")

