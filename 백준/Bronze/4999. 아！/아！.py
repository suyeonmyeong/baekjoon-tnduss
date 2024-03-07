import sys

ja= list(sys.stdin.readline().rstrip())
dt=list(sys.stdin.readline().rstrip())

if len(ja)>=len(dt):
	print('go')
else:
	print('no')