print("Sayı bişeycisi(her şeye birşey uydurmam 1-2 dk sürüyor vakit önemli idare et)")

a = (int(input("1.Sayı: ")))
b = (int(input("2.Sayı: ")))
c = (int(input("3.Sayı: ")))

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
elif c>a>b:
    print(f'{c}>{a}>{b}')
else:print("Geçersiz Giriş")