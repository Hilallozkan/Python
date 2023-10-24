#Soru 2:Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

EskiMaas = float(input("Lütfen maaşınızı giriniz:"))
ZamOrani = float(input("Lütfen zam oranınızı giriniz(%):"))

YeniMaas = ((EskiMaas * ZamOrani)/100) + EskiMaas

print(f"Yeni maaş miktarınız:{YeniMaas}")