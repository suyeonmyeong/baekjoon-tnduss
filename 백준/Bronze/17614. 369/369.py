import sys

n= int(sys.stdin.readline().rstrip())
clap=['3','6','9']
count=0
for i in range(1,n+1):
	s=list(str(i))
	for j in s:
		if j in clap:
			count+=1

print(count)