s=input("ENTER ANY STRING :")
str=""
for i in range (len(s)):
    if s[i].isupper():
        str+=s[i].lower()
    elif s[i].islower():
        str+=s[i].upper()
    else:
        str+=s[i]
print(str)
        
