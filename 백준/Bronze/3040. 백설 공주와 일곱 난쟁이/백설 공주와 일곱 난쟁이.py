import sys
lst=[]

for i in range(9):
	n= int(sys.stdin.readline().rstrip())
	lst.append(n)
	
for i in range(9):
	for j in range(i+1,9):
		sumv= sum(lst[:i])+sum(lst[i+1:j])+sum(lst[j+1:])
		if sumv==100:
			lst.pop(j)
			lst.pop(i)
			for k in lst:	
				print(k)
			sys.exit()