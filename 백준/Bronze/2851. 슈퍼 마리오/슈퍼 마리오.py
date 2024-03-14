import sys
lst=[]

for i in range(10):
	n= int(sys.stdin.readline().rstrip())
	lst.append(n)
result=0
sub=100
for i in range(len(lst)+1):
	tmp=sum(lst[:i])
	if abs(tmp-100) <=sub:
		sub=abs(tmp -100)
		result=tmp

print(result)