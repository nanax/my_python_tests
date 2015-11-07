import re
s=0
myf=open('1.txt')
for line in myf:
	y=re.findall('[0-9]+',line)
	if y !=[]:
		for i in y:
			s+=eval(i)
print s
myf.close()
fi=raw_input("press any key to continue")

