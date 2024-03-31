import sys
input = sys.stdin.readline

M = int(input())
queue = set()

for _ in range(M):
		in_put = input().rstrip()
		if in_put == "all":
				queue.update([i for i in range(1,21)])
				# queue = set(i for i in range(1,21))
		elif in_put == "empty":
				queue = set()
		else:
				cmd = in_put.split()[0]	# 명령어
				number = int(in_put.split()[1])	# 숫자

				if cmd == "add":
						queue.add(number)
				elif cmd == "check":
						if number in queue:
								print(1)
						else:
								print(0)
				elif cmd == "remove":
						queue.discard(number)
				elif cmd == "toggle":
						if number in queue:
								queue.remove(number)
						else:
								queue.add(number)