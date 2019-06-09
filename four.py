num=input("enter string of number")
num = num.split()
num = [int(y) for y in num]
s=0
for i in num:
    s=s+i
print("Sum is",int(s))
    