#coding=gbk
import serial
import random
ser=serial.Serial("COM7",9600)
myf=open('zi.txt')
lm=[]
ziti=1
for line in myf:
    lm.append(line)
while True:
    zis=raw_input("enter: ")
    if zis=='exit':
        break
    elif zis=='type1':
        ziti=1
    elif zis=='type2':
        ziti=2
    elif zis=='setz':
        tsend='00'
        t=tsend.decode("hex")
        ser.write(t)
    elif zis.startswith('random'):
        tempa=zis.split()
        counta=tempa[1]
        for tempint in range(int(counta)):
            tsend=random.choice(['01','02','0f','03','0d','04','0e','05','06','07','09','0a','0b','0c'])
            t=tsend.decode("hex")
            ser.write(t)
    else:
        lent=len(zis)
        zia=[]
        for ix in range(0,lent,2):
            abcd=zis[ix]+zis[ix+1]
            zia.append(abcd)
        for zi in zia:
            bian=False
            for line in lm:
                temp=line.split()
                if zi==temp[0]:
                    tsend=temp[ziti]
                    bian=True
                    break
            if bian==False:
                print 'warning: '+zi+" is not in the library"
            else:
                t=tsend.decode("hex")
                ser.write(t)
myf.close()
pau=raw_input("press any key to continue")
