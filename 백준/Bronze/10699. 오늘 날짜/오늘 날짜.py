import datetime # datetime 모듈 import

now = datetime.datetime.now() # 현재 날짜와 시간을 구함
print(now.strftime('%Y-%m-%d')) # 현재 날짜를 YYYY-MM-DD 형식으로 출력