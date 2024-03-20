import sys

n= int(sys.stdin.readline().rstrip())

for i in range(n):
	t=int(sys.stdin.readline().rstrip())
	lst=list(map(int,sys.stdin.readline().rstrip().split()))
	print(sum(lst))