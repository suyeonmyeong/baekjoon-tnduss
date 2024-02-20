import sys

a,b=map(int,sys.stdin.readline().rstrip().split())
b-=45
if (b<0):
	b+=60
	a-=1
if a<0:
	a=23
print(a,b)