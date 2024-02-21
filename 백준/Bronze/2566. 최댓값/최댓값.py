import sys
arr=[]
ml=[]
for i in range(9):
	lst=list(map(int,sys.stdin.readline().rstrip().split()))
	ml.append(max(lst))
	arr.append(lst)

maxv=max(ml)
max_row= ml.index(maxv)
lst=arr[max_row]
max_column= lst.index(max(lst))
print(maxv)
print(max_row+1,max_column+1)