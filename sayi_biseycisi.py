print("Sayı karşılaştırıcısı")

a = (int(input("1.Sayi: ")))
b = (int(input("2.Sayi: ")))
c = (int(input("3.Sayi: ")))

if a>b>c:
    print(f'{a}>{b}>{c}')
elif a>c>b:
    print(f'{a}>{c}>{b}')
elif b>c>a:
    print(f'{b}>{c}>{a}')
elif b>a>c:
    print(f'{b}>{a}>{c}')
elif c>b>a:
    print(f'{c}>{b}>{a}')
elif c > a > b:
    print(f'{c}>{a}>{b}')
else:print("Geçersiz Giriş")
#kendimi kandırıyormuş gibi hissediyorum bunun başka bir yolu olmalı değil mi?
