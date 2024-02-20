import sys

lst= []
for i in range(10):
	n= int(sys.stdin.readline().rstrip())
	lst.append(n%42)
tmp=set(lst)
res=list(tmp)
print(len(res))