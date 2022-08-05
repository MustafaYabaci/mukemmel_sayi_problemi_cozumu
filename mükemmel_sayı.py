sayi=int(input("lütfen bir sayı giriniz"))
toplam=0
for i in range(1,sayi):
    if(sayi%i==0):
        toplam+=i
if(sayi==toplam):
    print("mükemmel sayı")
else:
    print("mükemmel sayı degildir")