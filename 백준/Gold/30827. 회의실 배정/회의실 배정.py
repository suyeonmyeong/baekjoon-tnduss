import sys

n,k=map(int,sys.stdin.readline().rstrip().split())

time= []
for i in range(n):
  a,b=map(int,sys.stdin.readline().rstrip().split())
  time.append((a,b))

st=sorted(time,key=lambda k: (k[1],k[0]))
fin=[-1]*k
result=0
if (n<=k):
  result=n
else:
  for i,j in st:
    fin.sort()
    for h in range(k-1,-1,-1):
      if(fin[h]<i):
        fin[h]=j
        result+=1
        break
print(result)