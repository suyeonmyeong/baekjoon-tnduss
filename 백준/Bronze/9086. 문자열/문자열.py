import sys
n= int(sys.stdin.readline().rstrip())
for i in range(n):
	n= sys.stdin.readline().rstrip()
	print(n[0]+n[len(n)-1])