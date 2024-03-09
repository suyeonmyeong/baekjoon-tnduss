import sys

str= sys.stdin.readline().rstrip()

lst=list(str)
lst.reverse()
re=''.join(lst)

if str==re:
	print(1)
else:
	print(0)