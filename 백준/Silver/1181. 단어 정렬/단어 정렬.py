import sys

lst=[]
n= int(sys.stdin.readline().rstrip())
for i in range(n):
	lst.append(sys.stdin.readline().rstrip())
lst=set(lst)
lst=list(lst)
lst.sort()
slst= sorted(lst,key= lambda x : len(x),)


for i in slst:
	print(i)