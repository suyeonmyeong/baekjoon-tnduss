import sys

n= int(sys.stdin.readline().rstrip())
count=0
i=666
while True:
	if '666' in str(i):
		count+=1
		if count==n:
			print(i)
			sys.exit()
	i+=1