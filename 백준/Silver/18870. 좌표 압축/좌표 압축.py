import sys

# 입력에서 리스트 크기를 읽어들임
n = int(sys.stdin.readline().rstrip())

# 입력에서 공백으로 구분된 정수들을 읽어 리스트에 저장
lst = list(map(int, sys.stdin.readline().rstrip().split()))

# 중복 제거와 정렬을 한 번에 수행하여 정렬된 리스트를 얻음
sorted_unique_values = sorted(set(lst))

# 각 값을 키로, 해당 값의 인덱스를 값으로 하는 딕셔너리 생성
index_dict = {value: index for index, value in enumerate(sorted_unique_values)}

# 각 원소의 정렬된 리스트에서의 인덱스를 찾아 결과 리스트에 저장
result = [index_dict[element] for element in lst]

# 결과 리스트 출력
print(*result)