import sys
n= int(sys.stdin.readline().rstrip())
lst=list(map(int,sys.stdin.readline().rstrip().split()))
max=max(lst)
sum=0
for i in range(n):
	sum+= lst[i]/max*100
print(sum/n)