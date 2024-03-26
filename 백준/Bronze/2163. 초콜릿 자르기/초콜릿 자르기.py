import sys

a,b=map(int,sys.stdin.readline().rstrip().split())
result=0
tmp=0

def divv(n,m):

	if n ==1 and m==1:
		return
	global result
	if n>m:
		result+=1
		if n%2==0:	
			divv(n//2,m)
			divv(n//2,m)
		else:
			divv(n//2+1,m)
			divv(n//2,m)
	else:
		result+=1
		if m%2==0:	
			divv(n,m//2)
			divv(n,m//2)
		else:
			divv(n,m//2+1)
			divv(n,m//2)

divv(a,b)
print(result)