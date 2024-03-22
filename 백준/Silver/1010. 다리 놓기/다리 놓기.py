import sys

def fac(k):
	if k<=1:
		return 1
	else:
		return k*fac(k-1)

n= int(sys.stdin.readline().rstrip())


for i in range(n) :
	b,a=map(int,sys.stdin.readline().rstrip().split())
	faca=fac(a)
	facab=fac(a-b)
	facb=fac(b)
	print(int(faca/(facab*facb)))