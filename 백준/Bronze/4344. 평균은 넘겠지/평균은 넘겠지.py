import sys

N= int(sys.stdin.readline().rstrip())

for _ in range(N):
	lst=list(map(int,sys.stdin.readline().rstrip().split()))
	n=lst.pop(0)
	avg=sum(lst)/n
	m=[i for i in lst if i>avg]
	p=len(m)/n*100
	print('{0:0.3f}%'.format(p))