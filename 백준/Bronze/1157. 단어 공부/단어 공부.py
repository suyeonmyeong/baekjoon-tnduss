import sys

lst=list(sys.stdin.readline().rstrip().upper())
find=[]
cnt=[0]*26
index=0
for i in lst:
	if i not in find:
		find.append(i)
		cnt[index]=1
		index+=1
	else:
		cnt[find.index(i)]+=1

maxv=0
res=''
for i in range(len(cnt)):	
	if cnt[i]> maxv:
		maxv=cnt[i]
		res=find[i]
	elif cnt[i] == maxv:
		res='?'
	elif cnt[i]==0:
		break

print(res)