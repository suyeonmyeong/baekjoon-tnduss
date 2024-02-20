import sys

a,b=map(int,sys.stdin.readline().rstrip().split())
n1=list(str(a))
n2=list(str(b))

for i in range(2,-1,-1):
	if n1[i] > n2[i]:
		print(n1[2]+n1[1]+n1[0])
		break
	elif n1[i] < n2[i]:
		print(n2[2]+n2[1]+n2[0])
		break