a,b,c=map(float,input().strip().split(" "))
cc=c**2
pi=3.14159
triangle=.5*a*c
circle=pi*cc
trap=((a+b)/2)*c
squire=b**2
rectangle=a*b

print("TRIANGULO: %.3f"%triangle)
print("CIRCULO: %.3f"%circle)
print("TRAPEZIO: %.3f"%trap)
print("QUADRADO: %.3f"%squire)
print("RETANGULO: %.3f"%rectangle)