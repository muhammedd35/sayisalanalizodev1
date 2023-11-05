import math
x=math.pi/5
n=int(input("Bir sayi giriniz:"))
top=0
sign=1
for i in range(n):
    top =top+sign*(x**(2*i))/math.factorial(2*i)
    sign=(-1)*sign


gercek=math.cos(x)
print("yaklasık deger:",top)
print("cos(x)in gercek degeri:",gercek)
kesmehatasi=(gercek-top)
print("kesmehatasi:",kesmehatasi)

