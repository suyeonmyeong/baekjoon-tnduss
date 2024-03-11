import sys

n= int(sys.stdin.readline().rstrip())

for i in range(n):
	print(' '*i,end='')
	print('*'*(n-i))
	