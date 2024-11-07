import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
lst = {}
l = []
for _ in range(N):
	n = int(sys.stdin.readline().rstrip())
	l.append(n)
	# if n not in lst:
	# 	lst[n] = 1
	# else: 
	# 	lst[n] += 1
l.sort()
result = Counter(l).most_common()

# lst = sorted(lst, key= lambda x : (-x[1], x[0]))
print(result[0][0]) 