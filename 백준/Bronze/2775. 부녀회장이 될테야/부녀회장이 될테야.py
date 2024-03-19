import sys

n= int(sys.stdin.readline().rstrip())

for i in range(n):
	fl= int(sys.stdin.readline().rstrip())
	rn= int(sys.stdin.readline().rstrip())
	lst = [[i for i in range(1,rn+1)]]
	s=0
	
	for j in range(0,fl):
		tmp=[1]
		for k in range(1,rn):
			tmp.append(sum(lst[j][:(k+1)]))
		lst.append(tmp)

	print(lst[fl][rn-1])
	