import sys

n= int(sys.stdin.readline().rstrip())

def isempty(l):
	if l==0:
		return True

num=[]
for i in range(n):
	lst=list(sys.stdin.readline().rstrip().split())
	l=len(num)
	match lst[0]:
		case 'push':
			num.append(int(lst[1]))
		case 'pop':
			if isempty(l):
				print(-1)
			else:
				print(num.pop(0))
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
				print(num[0])
		case 'back':
			if isempty(l):
				print(-1)
			else:
				print(num[-1])