import sys
flag=True
n= int(sys.stdin.readline().rstrip())
for i in range(n):
	s=str(i)
	tmp=i
	for j in s:
		tmp+= int(j)
	if tmp==n:
		print(i)
		sys.exit()

print(0)