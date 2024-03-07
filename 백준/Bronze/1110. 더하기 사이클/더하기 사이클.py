import sys

n= int(sys.stdin.readline().rstrip())
tmp='-1'
res=0
lst=['-1','-1']
if (n<10):
	lst[0]='0'
	lst[1]=str(n)
else:
	lst=list(str(n))
	
while(n != int(tmp)):
	res+=1
	tmp1=(int(lst[0])+int(lst[1]))%10
	tmp= lst[1]+str(tmp1)
	lst=list(str(tmp))
print(res)