inp=int(input())


year=inp/365
month=(inp%365)/30
day=(inp%365)%30

print("%d ano(s)"%year)
print("%d mes(es)"%month)
print("%d dia(s)"%day)