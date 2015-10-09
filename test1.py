"""solving a quadratic equation"""
from math import sqrt
def my_input_number():
	sign=True
	while sign:
		inum=raw_input()
		try:
			inum=float(inum)
			sign=False
		except:
			print "not a correct number ,please type in again"
	return inum
print "Quadratic term coefficient"
a=my_input_number()
while True:
	if a==0:
		print "cannot be zero,type in again"
		a=my_input_number()
	else:break
print "term coefficient"
b=my_input_number()
print "Constant term"
c=my_input_number()
if (b**2-4*a*c)>0:
	print "x1="+str(-b+sqrt(b**2-4*a*c)/(2*a))
	print "x2="+str(-b-sqrt(b**2-4*a*c)/(2*a))
elif (b**2-4*a*c)==0:
	print "x1=x2="+str(-b/(2*a))
else:
	print "this equation has no solution"
a=raw_input("press any key to continue")