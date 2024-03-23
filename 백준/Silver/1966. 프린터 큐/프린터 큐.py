import sys
from collections import deque

N= int(sys.stdin.readline().rstrip())

for _ in range(N):
	n,idx =map(int,sys.stdin.readline().rstrip().split())
	lst=list(map(int,sys.stdin.readline().rstrip().split()))
	que=deque(enumerate(lst))
	flag=False
	result=0
	tmp=0
	while not flag :
		mx=max(que, key=lambda x: x[1])[1]
		for _ in range(len(que)):
			if que[0][1] != mx:
				que.append(que.popleft())
			else:
				result+=1
				if que[0][0] == idx:
					flag=True
				que.popleft()
				break
				
	print(result)