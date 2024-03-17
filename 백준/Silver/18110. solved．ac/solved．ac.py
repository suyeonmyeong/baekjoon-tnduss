import sys
import math

n= int(sys.stdin.readline().rstrip())
lst=[]

for i in range(n):
	lst.append(int(sys.stdin.readline().rstrip()))

if n*0.15 %1 >=0.5:
	t= math.ceil(n*0.15)
else:
	t= math.floor(n*0.15)
lst.sort()

if n==0:
	print(0)
	sys.exit()
elif t==0 or n<=2 :
	s=sum(lst)
	result=s/n

else:
	s=sum(lst[t:-(t)])
	result=s/(n-2*t)
	

if result %1 >=0.5:
	result= math.ceil(result)
else:
	result= math.floor(result)

print(result)
