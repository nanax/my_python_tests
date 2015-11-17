#coding=gbk
import serial
ser=serial.Serial("COM7",9600)
myf=open('zi.txt')
lm=[]
for line in myf:
    lm.append(line)
while True:
    zis=raw_input("type in word or exit: ")
    if zis=='exit':
        break
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
                if zi==temp[1]:
                    tsend=temp[0]
                    bian=True
                    break
            if bian==False:
                print 'warning: '+zi+" is not in the library"
            else:
                t=tsend.decode("hex")
                ser.write(t)
myf.close()
pau=raw_input("press any key to continue")
