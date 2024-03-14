import sys

n= int(sys.stdin.readline().rstrip())
f= int(sys.stdin.readline().rstrip())
num=n//100*100

for i in range(num,n+100):
	if i%f==0:
		print(str(i)[-2:])
		sys.exit()