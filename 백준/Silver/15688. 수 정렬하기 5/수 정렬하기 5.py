import sys

N = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(N):
	lst.append(int(sys.stdin.readline().rstrip()))

lst = sorted(lst)
print(*lst, sep='\n')