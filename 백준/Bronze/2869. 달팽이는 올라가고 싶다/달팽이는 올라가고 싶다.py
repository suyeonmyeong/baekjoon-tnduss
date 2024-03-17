import sys
import math
a,b,v=map(int,sys.stdin.readline().rstrip().split())

pre=1
d=0

if  v % (a-b) ==0:
	d+=math.ceil(v/(a-b)-b/(a-b)) 
else:
	d+=math.ceil((v-b)/(a-b))

print(d)