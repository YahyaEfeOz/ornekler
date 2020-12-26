sayı = int(input("Faktariyeli Alınacak Sayıyı Giriniz:"))
deger = 1
for n in range (sayı):
        deger *= n+1

if sayı <= 0:
        print("1")
elif sayı > 170:
        print ("∞")
else:
        print(deger)
#git degisiklik deneme