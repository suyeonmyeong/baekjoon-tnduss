import sys

n= int(sys.stdin.readline().rstrip())

list1=list(map(int,sys.stdin.readline().rstrip().split()))
m= int(sys.stdin.readline().rstrip())

list2=list(map(int,sys.stdin.readline().rstrip().split()))

d={}

for i in list2:
	if i not in d:
		d[i]=0

for i in list1:
	if i in d:
		d[i]+=1

for i in list2:
	print(d[i],end=' ')