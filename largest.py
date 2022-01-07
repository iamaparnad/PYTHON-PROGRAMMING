a=int(input("enter first digit :"))
b=int(input("enter second digit :"))
c=int(input("enter third digit :"))
if (a>b)&(a>c):
    print(a,"is greater")
elif (b>c)&(b>a):
    print(b, "is greater")
else:
    print(c,"is greater")
