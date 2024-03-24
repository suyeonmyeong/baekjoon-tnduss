import sys

N= int(sys.stdin.readline().rstrip())
result=0

def div(k):
	global result

	if(k==0):
		result+=1
		return
	
	if k>=1:
		div(k-1)
		 
	if k >=3:
		div(k-3)
		
	if k >= 2:
		div(k-2)
		
for _ in range(N):
	n= int(sys.stdin.readline().rstrip())
	result=0
	div(n)
	print(result)