import sys

a,b=map(int,sys.stdin.readline().rstrip().split())
lst=[]


for i in range(1,b+1):
	tmp = str(i*a)[::-1]
	lst.append(int(tmp))

print(max(lst))