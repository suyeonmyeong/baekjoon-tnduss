import sys
from collections import deque

d=deque()
r=[]
n,k=map(int,sys.stdin.readline().rstrip().split())

d=deque([i for i in range(1,n+1)])

while len(r)!=n:
	d.rotate(-(k-1))
	r.append(d.popleft())
	
print('<',end='')
for i in r[:-1]:
	print(i,end=', ')
print(r[-1],end='')
print('>')