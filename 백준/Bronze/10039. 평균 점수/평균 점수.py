import sys

sum=0
for i in range(5):
	k=int(sys.stdin.readline().rstrip())
	if k<40:
		sum+=40
	else:
		sum+=k

print(sum//5)