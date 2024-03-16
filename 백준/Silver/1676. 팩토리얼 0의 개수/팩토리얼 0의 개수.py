import sys

n= int(sys.stdin.readline().rstrip())
fac=1
for i in range(1,n+1):
	fac*=i
s= str(fac)
c=0
for i in range(len(s)-1,-1,-1):
	if s[i] =='0':
		c+=1
	else:
		print(c)
		break