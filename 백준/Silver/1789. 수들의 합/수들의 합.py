import sys
input = sys.stdin.readline

s=0
count=0
i=1

n=int(input())
while True:
	if n<2*i+1+s:
		s+=i
		count+=1
		break
	s+=i
	i+=1
	count+=1
print(count)