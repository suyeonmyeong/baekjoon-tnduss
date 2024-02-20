import sys

a,b=map(int,sys.stdin.readline().rstrip().split())

#lst=list(sys.stdin.readline().rstrip().upper())
if a<b:
	res='<'
elif a>b:
	res='>'
else:
	res='=='
print(res)