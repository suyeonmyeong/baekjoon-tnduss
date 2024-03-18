import sys

n= int(sys.stdin.readline().rstrip())
lst=[]
d={}
min=4000
max=-4000
for i in range(n):
	t= int(sys.stdin.readline().rstrip())
	lst.append(t)
	if t in d:
		d[t]+=1
	else:
		d[t]=1
	if max<t:
		max=t
	if min>t:
		min=t

lst.sort()
print(round(sum(lst)/n))
print(lst[n//2])

d=sorted(d.items() , key= lambda x: (x[1],x[0]),reverse=True)
result=0
rsnt = d[0][1]
for i in range(1,len(d)):
	if d[i][1]==rsnt:
		result=i
	else:
		break

if result==0:
	pass
else:
	result-=1

print(d[result][0])
print(max-min)