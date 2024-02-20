import sys
lst=list(map(int,sys.stdin.readline().rstrip().split()))
thr=False
same=0
if lst[0]==lst[1]:
	same=lst[0]
	if lst[1]== lst[2]:
		thr=True
elif lst[0]==lst[2]:
	same=lst[0]
elif lst[1]== lst[2]:
	same=lst[1]
if same==0:
	print(max(lst)*100)
elif thr:
	print(10000+same*1000)
else:
	print(same*100+1000)