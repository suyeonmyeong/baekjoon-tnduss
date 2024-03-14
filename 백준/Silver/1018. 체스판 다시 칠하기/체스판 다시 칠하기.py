import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[]
for i in range(n):
	s= sys.stdin.readline().rstrip()
	arr.append(s)
result=n*m

for k in range(n):
	for h in range(m):
		count=0
		count1=0
		if(n<k+8) or m<h+8:
			break
		for i in range(k,k+8):
			for j in range(h,h+8):
				if i%2==0 and j%2==0 :
					if arr[i][j] !='B':
						count+=1
					else:
						count1+=1
				elif i%2==1 and j%2==1:
					if arr[i][j] !='B':
						count+=1
					else:
						count1+=1
				elif i%2==0 and j%2==1 :
					if arr[i][j] !='W':
						count+=1
					else:
						count1+=1
				elif i%2==1 and j%2==0:
					if arr[i][j] !='W':
						count+=1
					else:
						count1+=1
		if result>count:
			result=count
		if result> count1:
			result=count1

print(result)