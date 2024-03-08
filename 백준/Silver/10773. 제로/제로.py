import sys

n= int(sys.stdin.readline().rstrip())
res=[]
for i in range(n):
	a= int(sys.stdin.readline().rstrip())
	
	if a == 0 :
		res.pop()
	else:
		res.append(a)
s=0
for i in res:
	s+=i
print(s)
