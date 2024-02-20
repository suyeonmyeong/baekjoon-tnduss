import sys

n=int(sys.stdin.readline().rstrip())

due=[]
dl = []
for i in range(n):
  a,b=map(int,sys.stdin.readline().rstrip().split())
  due.append(a)
  dl.append(b)
sdl=sorted(dl)
si = sorted(range(len(dl)), key=lambda k: dl[k])
res= 10**9
r=0
for i in range(len(sdl)):
  r+= due[si[i]]
  if sdl[i]-r<res:
    res=sdl[i]-r
print(res)