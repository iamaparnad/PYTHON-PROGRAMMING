
from datetime import datetime
n=int(input("ENTER THE YEAR"))
cur=(datetime.today().year)
n=n+1
print("LEAP YEAR BETWEEN ",cur, " and " ,n-1," is ")
for i in range(cur,n):
    if(i%4==0):
        print(i)
    
