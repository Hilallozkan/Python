#Soru 1:Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

KullaniciBoy =float(input("Lütfen boyunuzu giriniz(cm):"))
KullaniciKilo = float(input("Lütfen kilonuzu giriniz(kg):"))

print("====================================================")
VKI = KullaniciKilo/(KullaniciBoy*KullaniciBoy)

print(f"Vücut kitle indeksiniz:{VKI}")

if VKI < 18.4 :
    print("Sonucunuz normal sınırın altında, sağlıklı bir şekilde kilo almaya çalışmalısınız.")
elif VKI >=18.4 and VKI<29.8:
     print("Sonucunuz normal sınırda.")
else :
     print("Sonucunuz normal sınırın üzerinde, sağlıklı bir şekilde kilo vermeye çalışmalısınız.")