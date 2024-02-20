import sys
n= int(sys.stdin.readline().rstrip())
lst=[]
cnt=[1]*n
for i in range(n):
	a,b=map(int,sys.stdin.readline().rstrip().split())
	lst.append((a,b))
for i in range(n):
	for j in range(n):
		if i==j:
			continue
		elif lst[i][1]<lst[j][1] and lst[i][0]<lst[j][0]:
			cnt[i]+=1


print(*cnt)
	