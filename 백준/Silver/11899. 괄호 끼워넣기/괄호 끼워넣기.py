import sys
from collections import deque

lst= sys.stdin.readline().rstrip()
f_que=deque()
l_que=deque()
count=0

for i in lst:
	if i==')':
		if len(f_que)==0:
			count+=1
		else:
			f_que.pop()
	else:
		f_que.append('(')

count+=len(f_que)
print(count)