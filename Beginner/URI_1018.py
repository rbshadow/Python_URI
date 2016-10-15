a=int(input())

hun=a/100
hunfinal=a%100

fif=hunfinal/50
fiffinal=hunfinal%50

twen=fiffinal/20
twenfinal=fiffinal%20

ten=twenfinal/10
tenfinal=twenfinal%10

five=tenfinal/5
fivefinal=tenfinal%5

two=fivefinal/2
twofinal=fivefinal%2

one=twofinal/1

print("%d"%a)
print("%d nota(s) de R$ 100,00"%hun)
print("%d nota(s) de R$ 50,00"%fif)
print("%d nota(s) de R$ 20,00"%twen)
print("%d nota(s) de R$ 10,00"%ten)
print("%d nota(s) de R$ 5,00"%five)
print("%d nota(s) de R$ 2,00"%two)
print("%d nota(s) de R$ 1,00"%one)