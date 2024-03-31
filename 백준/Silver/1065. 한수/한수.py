import sys

N= int(sys.stdin.readline().rstrip())

count=0
for i in range(1,N+1):

	if i<100:
		count+=1
				
	else:
		s=str(i)
		sub=int(s[1])-int(s[0])
		flag=True
		for i in range(2,len(s)):
			if int(s[i])-int(s[i-1]) != sub:
				flag=False
		if flag:
			count+=1
		
print(count)