import sys

N= int(sys.stdin.readline().rstrip())
tmp=0
c=1
while tmp<N:
	tmp+=c
	c+=1

c-=1
div=N-tmp+c

if c %2 ==0:
	print(div,end='/')
	print(c-div+1)
else:
	print(c-div+1,end='/')
	print(div)