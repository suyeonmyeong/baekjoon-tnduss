import sys
N= int(sys.stdin.readline().rstrip())
lst=[]

for i in range(N):
	lst.append(int(sys.stdin.readline()))

count=1
high=lst[-1]
for i in range(N-2,-1,-1):
	if lst[i] > high:
		high=lst[i]
		count+=1
print(count)
