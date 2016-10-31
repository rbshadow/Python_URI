x,y,z = input().split()
x,y,z = int(x),int(y),float(z)

x1,y1,z1 = input().split()
x1,y1,z1 = int(x1),int(y1),float(z1)

grand = y * z
grand2 = y1 * z1

tgrand = grand + grand2
print("VALOR A PAGAR: R$ %.2f" %tgrand)
