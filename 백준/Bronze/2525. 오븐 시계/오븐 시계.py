import sys
a,b=map(int,sys.stdin.readline().rstrip().split())
n= int(sys.stdin.readline().rstrip())
if b+n>=60:
	a+=(b+n)//60
	b=(b+n)%60
	
else:
	b+=n
if a>=24:
	a=a%24
print(a,b)