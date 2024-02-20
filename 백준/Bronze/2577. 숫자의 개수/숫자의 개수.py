import sys
cnt=[0]*10
mul=1
for i in range(3):
	n= int(sys.stdin.readline().rstrip())
	mul*=n
lst=list(str(mul))
for i in lst:
	cnt[int(i)]+=1
for i in cnt:
	print(i)