import sys

n= int(sys.stdin.readline().rstrip())
lst=set(map(int,sys.stdin.readline().rstrip().split()))
m= int(sys.stdin.readline().rstrip())
cmp=list(map(int,sys.stdin.readline().rstrip().split()))


for i in cmp:
		if i in lst:
			print(1,end=' ')
		else:
			print(0,end=' ')