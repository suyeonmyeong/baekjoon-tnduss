import sys

n= int(sys.stdin.readline().rstrip())

lst=[]
for i in range(n):
	a,b=sys.stdin.readline().rstrip().split()
	lst.append((int(a),b))

slst=sorted(lst,key=lambda x: x[0])

for i in slst:
	print(*i)