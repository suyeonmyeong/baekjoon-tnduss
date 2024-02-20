import sys

lst=[]
for i in range(1,31,1):
	lst.append(i)

for i in range(28):
	n= int(sys.stdin.readline().rstrip())
	k=lst.index(n)
	lst.pop(k)
for i in lst:
	print(i)