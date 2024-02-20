import sys
lst=[]
for i in range(9):
	lst.append(int(sys.stdin.readline().rstrip()))
st=sorted(lst)
print(st[8])
print(lst.index(st[8])+1)