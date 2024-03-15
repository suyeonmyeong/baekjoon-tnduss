import sys

n= int(sys.stdin.readline().rstrip())

list1=set(map(int,sys.stdin.readline().rstrip().split()))
m= int(sys.stdin.readline().rstrip())

list2=list(map(int,sys.stdin.readline().rstrip().split()))

for i in list2:
	if i in list1:
		print(1)
	else:
		print(0)