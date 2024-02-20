import sys

n= list(sys.stdin.readline().rstrip())

for i in range(len(n)):
	if ord('a')<=ord(n[i]):
		n[i]=n[i].upper()
	else:
		n[i]=n[i].lower()

for i in n:
	print(i,end='')