#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi=int(input("Lütfen test etmek istediğiniz sayıyı Girin : "))
if sayi > 1:
   
   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(" Girdiğiniz sayı asal sayı değildir.")
           break
   else:
       print(" Girdiğiniz sayı asal sayıdır.")
 
else:
   print(" Girdiğiniz sayı asal sayı değildir.")