import os
import sys

if len(sys.argv)==4:
	j=int(sys.argv[1])
	Beta=float(sys.argv[2])
	step=float(sys.argv[3])
else:
	j=5
	Beta=1.0
	step=0.001

duplicate=20
Beta=Beta-j/2*step
for i in range(0,j):
	for k in range(0,duplicate):
		fname="input.%d" %(i*duplicate+k)
		fo=open(fname,"w")
		fo.write("%f\n%d" %(Beta,i*duplicate+k))	
		fo.close()
	Beta=Beta+step

