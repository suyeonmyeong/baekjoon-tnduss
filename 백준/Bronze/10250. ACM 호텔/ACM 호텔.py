import sys
k= int(sys.stdin.readline().rstrip())
ref=0
resnum=0
for i in range(k):
	fl,wdt,n=map(int,sys.stdin.readline().rstrip().split())
	ref=n%fl
	resnum=n//fl+1
	if n%fl ==0:
		ref=fl
		resnum=n//fl
	if fl==1:
		ref=1
		resnum=n
	if resnum<10:
		resnum='0'+str(resnum)
	print(str(ref)+str(resnum))