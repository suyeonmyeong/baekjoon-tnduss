import sys


lst=[]
a=sys.stdin.readline().rstrip()
b=sys.stdin.readline().rstrip()
result=[]
for i in range(len(a)):
	result.append(a[i])
	result.append(b[i])

tmp=[]
while len(result)!=2:
	tmp=[]
	for i in range(len(result)-1):
		tmp.append((int(result[i])+int(result[i+1]))%10)
	result=tmp[:]	
	
print(str(result[0])+str(result[1]))