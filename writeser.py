#coding=gbk
import serial
ser=serial.Serial("COM7",9600)
panduan=True
myf=open('zi.txt')
lm=[]
for line in myf:
    lm.append(line)
while panduan:
    zi=raw_input("type in word:")
    bian=False
    for line in lm:
        temp=line.split()
        if zi==temp[1]:
            tsend=temp[0]
            bian=True
            break
    if bian==False:
        print "no such word"
    else:
        t=tsend.decode("hex")
        ser.write(t)
    tt=raw_input("exit?")
    if tt=="y":
        panduan=False
    else:
        panduan=True
myf.close()
pau=raw_input("press any key to continue")
