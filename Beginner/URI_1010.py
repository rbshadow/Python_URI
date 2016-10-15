code,item,price= map(int,(input().split(" ")),int(input().split(" ")),float(input().split(" ")))

code1,item1,price1=map(int(input().split(" ")),int(input().split(" ")),float(input().split(" ")))

grand=item*price
grand2=item1*price1

tgrand=grand+grand2
print("VALOR A PAGAR: R$ %.2f"%tgrand)
