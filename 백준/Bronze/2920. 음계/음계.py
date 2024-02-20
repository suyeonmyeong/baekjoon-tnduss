import sys
lst=list(map(int,sys.stdin.readline().rstrip().split()))
asc=[1,2,3,4,5,6,7,8]
des=[8,7,6,5,4,3,2,1]
if asc==lst:
	print("ascending")
elif des==lst:
	print("descending")
else:
	print("mixed")