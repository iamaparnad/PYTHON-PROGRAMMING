arsq = lambda side : side * side
arrec = lambda length,width : length * width
artri =  lambda s,a,b,c : (s*(s-a)*(s-b)*(s-c)) ** 0.5

a=5
b=10
c=15
s = (a + b + c) / 2

print("AREA OF SQUARE IS",arsq(a))
print("AREA OF RECTANGLE IS",arrec(a,b))
print("AREA OF TRIANGLE IS",artri(s,a,b,c))
