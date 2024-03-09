import sys

n= int(sys.stdin.readline().rstrip())
lst= list(sys.stdin.readline().rstrip())
r=sys.stdin.readline().rstrip()
re=0
for i in lst:
	if i==r:
		re+=1
	
print(re)