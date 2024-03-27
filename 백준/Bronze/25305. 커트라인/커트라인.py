import sys

n,k=map(int,sys.stdin.readline().rstrip().split())
lst=list(map(int,sys.stdin.readline().rstrip().split()))
lst.sort(reverse=True)
print(lst[k-1])