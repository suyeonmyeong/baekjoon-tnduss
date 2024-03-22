import sys

n= int(sys.stdin.readline().rstrip())
result=1

if n==1:
	print(1)
elif 2<=n<=7:
	print(2)
elif 8<=n<=13:
	print(3)
else:
	for i in range(1,n):
		if n <= result:
			print(i)
			sys.exit()
		result+=6*i