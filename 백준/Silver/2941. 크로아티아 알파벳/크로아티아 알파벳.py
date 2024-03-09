import sys

org= sys.stdin.readline().rstrip().replace('c=','A').replace('c-','A').replace('dz=','A').replace('d-','A').replace('lj','A').replace('nj','A').replace('s=','A').replace('z=','A')
print(len(org))