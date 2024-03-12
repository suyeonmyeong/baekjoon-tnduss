import sys

n= int(sys.stdin.readline().rstrip())

re=-1
tmp=0
for i in range(n//3):
	if (n==5):
		re=1
	if(5*i>n):
		break
	tmp=i+ (n-5*i)//3
	if (n-5*i) %3 ==0:
		if 0<tmp<re:
			re=tmp
		elif re==-1:
			re=tmp
			
print(re)