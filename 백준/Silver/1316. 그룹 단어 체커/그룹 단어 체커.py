import sys
n= int(sys.stdin.readline().rstrip())
c=0
for i in range(n):
	str=sys.stdin.readline().rstrip()
	before='1'
	re=True
	appear=[]
	for j in str:
		if before!=j:
			if j in appear:
				re=False
				break
			appear.append(before)
		before=j
	if re or len(str)==1:
		c+=1
print(c)
		