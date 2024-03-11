import sys

n= sys.stdin.readline().rstrip()

for i in range(1,len(n)//10+1,1):
	print(n[(i-1)*10:i*10])

if(len(n)>=10):
	print(n[i*10:])
else:
	print(n)