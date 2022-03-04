import calendar  
yy= int(input ("Please enter the Year: "))  
mm= int(input ("Please enter the month: "))
if(mm>12) or (mm<1):
    print("INVALID MONTH")
else:
    print("The Calendar of: ", calendar.month(yy,mm)) 
