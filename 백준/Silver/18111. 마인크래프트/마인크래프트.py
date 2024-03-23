import sys


N,M,B=map(int,sys.stdin.readline().rstrip().split())
lst=[]
for _ in range(N):
	lst.append(list(map(int,sys.stdin.readline().rstrip().split())))

best=-1
best_fl= -1
for fl in range(257):
	block=B
	result=0
	for i in range(N):
		for j in range(M):
			t=lst[i][j]
			if  t== fl:
				pass
			elif t <fl:
				result+= (fl-t)
				block-= (fl-t)
			else:
				result+= (t-fl)*2
				block+= (t-fl)
	if block<0:
		continue
	elif best==-1:
		best=result
		best_fl=fl
	elif result<=best:
		best=result
		if fl>best_fl:
			best_fl=fl
print(best,best_fl)