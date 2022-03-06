class shape:
    def __init__(self):
        self.length=int(input("enter the length "))
        self.breadth=int(input("enter the breadth "))
        self.rec=self.length*self.breadth
        print("area of rectangle=",self.rec)
    def tri(self):
        self.length=int(input("enter the length "))
        self.breadth=int(input("enter the breadth "))
        self.triangle=(1/2)*self.length*self.breadth
        print("area of triangle=",self.triangle)
    def cir(self):
        pi=3.14
        self.rad=int(input("enter the radius "))
        self.circle=2*pi*self.rad
        print("area of circle is ",self.circle)
z=shape()
z.tri()
z.cir()

        
