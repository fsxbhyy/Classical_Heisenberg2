import numpy as np
import sys
import os

L=16
argn=1
Copy=20
size=32
Sub=1
np.set_printoptions(threshold=np.nan,suppress=True)
a=np.zeros((Sub*2+2,L*L))
fname=os.listdir(".")
NN=np.zeros(size)
Q=np.zeros((size,Sub,L*L))
Error=np.zeros((size,Sub,L*L))
for name in fname:
	if (name[0]=="A" and name[-1]=="t" and os.path.getsize(name)):
		a=np.transpose(np.loadtxt(name,dtype='float',unpack=False))
		J=int(eval(name[4:-4]))
		NN[J//Copy]+=1
		for k in range(0,Sub):
			for i in range(0,L*L):
				Q[J//Copy][k][i]+=a[(k+1)*2][i]

for l in range (0,size):
	for i in range (0,L*L):
		for j in range (0,Sub):
			if(NN[l]!=0):
				Q[l][j][i]/=NN[l]
				

for l in range (0,size):
	print Q[l][0][1]

for name in fname:
        if (name[0]=="A" and name[-1]=="t" and os.path.getsize(name)):
                a=np.transpose(np.loadtxt(name,dtype='float',unpack=False))	
		J=int(eval(name[4:-4]))
		for k in range(0,Sub):
			for i in range(0,L*L):
				Error[J//Copy][k][i]+=(Q[J//Copy][k][i]-a[(k+1)*2][i])**2

for l in range (0,size):
        for i in range (0,L*L):
                for j in range (0,Sub):
			if(NN[l]!=0):
				Error[l][j][i]/=NN[l]*NN[l]

Error=np.sqrt(Error)




for l in range (0,size):
	filename="J%d.txt" % (l)
	fq=open(filename,"w")
	for i in range (0,L):
		for j in range(0,L):	
			fq.write(("%d\t%d\t") % (i,j))
			for k in range (0,Sub):
				fq.write(("%f\t%f") % (Q[l][k][i*L+j],Error[l][k][i*L+j]))
				if(k==Sub-1):
					fq.write("\n")
				else: 
					fq.write("\t")
	fq.close()
 	


