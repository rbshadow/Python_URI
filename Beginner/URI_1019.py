inp=int(input())

hour=inp/3600
minu=(inp%3600)/60
sec=(inp%3600)%60

print("%d:"%hour,end="")
print("%d:"%minu,end="")
print("%d"%sec)