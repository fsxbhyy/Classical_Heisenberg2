import numpy as np
import sys
import os
import math
L=16
argn=1
Sub=1
np.set_printoptions(threshold=np.nan,suppress=True)
b=np.zeros(((Sub+1)*2,L*L))
a=np.zeros((Sub+2,L*L))

for i in range(len(sys.argv)):
    print sys.argv[i]

a=np.transpose(np.loadtxt(sys.argv[argn],unpack=False))

fname=os.listdir(".")

Js=[]
Fr=[]

diff=0
NN=0
for name in fname:
    if (name[0]=="J" and name[-1]=="t" and os.path.getsize(name)):
        b=np.transpose(np.loadtxt(name,unpack=False))
        print 
	J=eval(name[1:-4])
        Js.append(J)
	for i in range (1,Sub+1):
		for k in range (0,L*L):
			if(abs(b[i*2][k])>10*b[i*2+1][k]):
				diff+=(a[i+1][k]-b[i*2][k])**2
				NN+=1
	
		print J,NN
	 #   diff=np.sqrt(np.sum((a1-b1)**2+(a2-b2)**2+(a3-b3)**2 )/16./16./3.)
     #   err=np.sqrt(np.sum( (e1)**2+(e2)**2+(e3)**2 )/16./16./3.)
        if(NN>0):
		print diff
		diff/=NN
		Fr.append(diff)
	diff=0
	NN=0

print Js[Fr.index(min(Fr))]

