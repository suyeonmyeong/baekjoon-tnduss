import sys

n= int(sys.stdin.readline().rstrip())
count=0
for i in range(1,501):
	for j in range(1,i):
		if i**2 -j**2==n:
			count+=1

print(count)