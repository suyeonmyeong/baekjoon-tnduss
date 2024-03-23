import sys

N= int(sys.stdin.readline().rstrip())
lst = [[1, 0], [0, 1]]
lst.extend([[0,0] for _ in range(39)])

for _ in range(N):
	n= int(sys.stdin.readline().rstrip())
	for i in range(2,n+1):
		lst[i][0] = lst[i-1][0] + lst[i-2][0]
		lst[i][1] = lst[i-1][1] + lst[i-2][1]
		
	flag=n
	print(*lst[n])