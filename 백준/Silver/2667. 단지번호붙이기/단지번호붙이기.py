import sys

N = int(sys.stdin.readline())
map = []
for i in range(N):
  map.append(list(sys.stdin.readline().rstrip()))

house = []
lst = []
flag = [[0 for i in range(N)] for i in range(N)]
def search(i,j):
  global num
  
  if i != 0 and flag[i-1][j] == 0 and map[i-1][j] == '1':
    flag[i-1][j] = 1
    num+=1
    search(i-1,j)
  if i!=N-1 and flag[i+1][j] == 0 and map[i+1][j] == '1':
    flag[i+1][j] = 1
    num+=1
    search(i+1,j)
  if j != 0 and flag[i][j-1] == 0  and map[i][j-1] == '1':
    flag[i][j-1] = 1
    num+=1
    search(i,j-1)
  if j != N-1 and flag[i][j+1] == 0  and map[i][j+1] == '1':
    flag[i][j+1] = 1
    num+=1
    search(i,j+1)
    
  return num

num = 0
for i in range(N):
  for j in range(N):
    if map[i][j] == '1' and flag[i][j] == 0:
     flag[i][j] = 1
     num = 1+ search(i,j)
     lst.append(num)
     num=0
lst.sort()
print(len(lst))
print(*lst,sep='\n')
     