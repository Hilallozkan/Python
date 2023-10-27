#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
sayi = int(input("Bir Sayı Girin: "))
bolen = 2 
print(sayi, "Sayısının Asal Çarpanları:") 
while bolen <= sayi:  
    if sayi % bolen == 0: 
        print(bolen) 
        sayi //= bolen 
    else:
        bolen += 1 