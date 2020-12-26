def toplama(x,y):
    return x+y
def çıkartma(x,y):
    return x-y
def bölme(x,y):
    return x/y
def çarpma(x,y):
    return x*y

print("↓Yapılacak işlemi seçiniz↓")
print("1.Toplama")
print("2.Çıkartma")
print("3.Bölme")
print("4.Çarpma")
secim = (int(input("Seçim Yapınız (1/2/3/4):")))

if secim>4 or secim<1:
    print("Geçersiz Giriş")

else:
    sayı1 = (int(input("1.Sayı: ")))
    sayı2 = (int(input("2.Sayı: ")))

    if secim == 1:
        print(sayı1,"+",sayı2,"=", toplama(sayı1,sayı2))

    elif secim == 2:
        print(sayı1,"-",sayı2,"=", çıkartma(sayı1,sayı2))

    elif secim == 3:
        print(sayı1,"/",sayı2,"=", bölme(sayı1,sayı2))

    elif secim == 4:
        print(sayı1,"*",sayı2,"=",çarpma(sayı1,sayı2))

