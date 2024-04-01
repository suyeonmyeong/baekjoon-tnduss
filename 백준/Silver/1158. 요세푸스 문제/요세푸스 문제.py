from collections import deque
import sys

lst=[]
n,k = map(int,sys.stdin.readline().rstrip().split())
que=deque(i for i in range(1,n+1))

while len(que)!=0:
	que.rotate(-k+1)
	lst.append(que.popleft())
	
print('<',end='')
print(*lst,sep=', ',end='')
print('>',end='')