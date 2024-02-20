import sys

n= int(sys.stdin.readline().rstrip())
for i in range(n):
	lst=list(sys.stdin.readline().rstrip())
	res=0
	cnt=1
	for i in lst:
		if i == 'O':
			res+=cnt
			cnt+=1
		else:
			cnt=1
	print(res)