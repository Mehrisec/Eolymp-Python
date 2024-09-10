#Natural eded daxil edilir. Bu ededin reqemlerin cemin ededden cixiriq. Cixdiqdan sonra yeni ededi de bu qaydada cixiriq ta ki menfi olana qeder ve bu prosesin nece defe tekrar edildiyin cixisa veriririk.
def f(x):#Burada funksiya yaradiriq bu funksiya icine gonderilen ededin reqemlerin cemin toplayir vce cagirildigi zaman cixisa verir
    c=0
    while x>0:
        c=c+(x%10)
        x=x//10
    return c#Ededin cemin yadda saxlayir
x=int(input())#Ededi daxil edirik
i=0#Burada i prosesin sayin yeni nece defe tekrar olunmasini gosterir ve sifirdan baslayir 
while x>0:
    x=x-f(x)#Burada ise eddden ededin reqemlerinin cemin cixardir funksiyani cagirir funksiya ise cemi yadda saxladigi ucun cixisa verir
    i=i+1#Burada proseslerin sayin tekrar etdikce 1 defe artirir
print(i)
