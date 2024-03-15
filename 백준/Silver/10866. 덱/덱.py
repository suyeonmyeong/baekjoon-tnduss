import sys

from collections import deque

n= int(sys.stdin.readline().rstrip())

d=deque()

def isempty(l):
	if l==0:
		return True


for i in range(n):
	lst=list(sys.stdin.readline().rstrip().split())
	l=len(d)
	match lst[0]:
		case 'push_front':
			d.appendleft(int(lst[1]))
		case 'push_back':
			d.append(int(lst[1]))
		case 'pop_front':
			if isempty(l):
				print(-1)
			else:
				print(d.popleft())
		case 'pop_back':
			if isempty(l):
				print(-1)
			else:
				print(d.pop())
		case 'size':
			print(l)
		case 'empty':
			if isempty(l):
				print(1)
			else:
				print(0)
		case 'front':
			if isempty(l):
				print(-1)
			else:
				print(d[0])
		case 'back':
			if isempty(l):
				print(-1)
			else:
				print(d[-1])