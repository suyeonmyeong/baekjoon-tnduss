import sys
arr=[]
lng=[]
for i in range(5):
	lst=list(sys.stdin.readline().rstrip())
	lng.append(len(lst))
	arr.append(lst)
maxv=max(lng)
for i in range(maxv):
	for j in range(len(arr)):
		if (lng[j]>= i+1):
			print(arr[j][i],end='')