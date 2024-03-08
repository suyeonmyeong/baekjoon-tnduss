import sys

n= int(sys.stdin.readline().rstrip())
res='WelcomeToSMUPC'

print(res[n%len(res)-1])