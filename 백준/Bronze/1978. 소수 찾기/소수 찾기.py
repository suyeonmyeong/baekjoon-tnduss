import sys

n= int(sys.stdin.readline().rstrip())
lst=list(map(int,sys.stdin.readline().rstrip().split()))
res=0
for i in lst:
	f=True
	if i==1:
		continue
	for j in range(2,i):
		if i %j==0 :
			f=False
			break
	if f:
		res+=1
print(res)