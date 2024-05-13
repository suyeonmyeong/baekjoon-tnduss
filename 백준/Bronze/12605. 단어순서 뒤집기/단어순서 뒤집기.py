import sys
N= int(sys.stdin.readline().rstrip())
for i in range(N):
	lst=list(sys.stdin.readline().rstrip().split(' '))
	lst.reverse()
	print('Case #{0}: '.format(i+1),end='')
	print(*lst,sep=' ')
