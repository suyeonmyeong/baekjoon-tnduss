import sys

K,N=map(int,sys.stdin.readline().rstrip().split())
lst=[]
for _ in range(K):
	lst.append(int(sys.stdin.readline().rstrip()))

lst.sort()

summ=sum(lst)

def ispromise(lng):
	tmp=0
	for i in range(K-1,-1,-1):
		tmp+=lst[i]//lng
		if tmp>=N:
			return True
			
	return False

result=1
low= 1
high= summ//N+1

if low==high:
	if N%K==0:
		result= low // (N//K)
	else:
		result= low // (N//K+1)
	print(result)
	sys.exit()
	
while low<=high:
	mid= (low+high)//2
	if ispromise(mid):
		if result<mid:
			result= mid
		low=mid+1
	else:
		high=mid-1
print(result)