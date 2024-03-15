import sys

n= int(sys.stdin.readline().rstrip())
from collections import deque

lst=[i for i in range(1,n+1)]
d=deque(lst)
if n==1:
	print(1)
else:
	while True:
		d.popleft()
		if len(d)==1:
			print(d[0])
			sys.exit()
		else:
			d.append(d.popleft())