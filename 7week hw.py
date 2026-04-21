
from datetime import datetime

# 현재 날짜와 시간 가져오기
now = datetime.now()

# 날짜 출력
print(f"오늘의 날짜 : {now.year}년 {now.month}월 {now.day}일")

# 시간 변환 (오전/오후)
hour = now.hour
minute = now.minute
second = now.second

if hour < 12:
    period = "오전"
    display_hour = hour if hour != 0 else 12
else:
    period = "오후"
    display_hour = hour - 12 if hour > 12 else 12

print(f"현재시간 : {period} {display_hour}시 {minute}분 {second}초")


from datetime import datetime

# 오늘 날짜와 시간
now = datetime.now()

print(f"오늘은 {now.year}년 {now.month}월 {now.day}일입니다")

# 1. 2025년 크리스마스까지 남은 날짜와 시간
christmas = datetime(year=2025, month=12, day=25)
remaining_christmas = christmas - now
days_christmas = remaining_christmas.days
hours_christmas = remaining_christmas.seconds // 3600
print(f"2025년 크리스마스까지는 {days_christmas}일 {hours_christmas}시간 남았습니다.")

# 2. 2036년 새해까지 남은 날짜와 시간
new_year = datetime(year=2036, month=1, day=1)
remaining_new_year = new_year - now
days_new_year = remaining_new_year.days
hours_new_year = remaining_new_year.seconds // 3600
print(f"2036년 새해까지는 {days_new_year}일 {hours_new_year}시간 남았습니다.")

# 3. 현우님의 생일(2월 25일)까지 남은 날짜와 시간
birthday = datetime(year=now.year, month=2, day=25)

# 올해 생일이 이미 지났으면 내년으로 계산
if birthday < now:
    birthday = datetime(year=now.year + 1, month=2, day=25)

remaining_birthday = birthday - now
days_birthday = remaining_birthday.days
hours_birthday = remaining_birthday.seconds // 3600
print(f"{birthday.year}년 생일까지는 {days_birthday}일 {hours_birthday}시간 남았습니다.")

from datetime import datetime, timedelta

# 오늘 날짜
now = datetime.now()
print(f"오늘은 {now.year}년 {now.month}월 {now.day}일입니다")

# 1. 오늘로부터 1000일 후의 날짜 계산
after_1000 = now + timedelta(days=1000)
print(f"오늘로부터 1000일 후의 날짜는 {after_1000.year}년 {after_1000.month}월 {after_1000.day}일입니다")

from datetime import datetime, timedelta

# 처음 만난 날짜 (2023년 2월 9일)
first_day = datetime(year=2023, month=2, day=9)

# 100일 기념일
hundred_day = first_day + timedelta(days=100)

print(f"처음 만난 날은 {first_day.year}년 {first_day.month}월 {first_day.day}일입니다")
print(f"100일 기념일은 : {hundred_day.year}년 {hundred_day.month}월 {hundred_day.day}일입니다")

import math

# 1. 4의 2승부터 10승까지 출력
print("=== 4의 거듭제곱 ===")
for i in range(2, 11):
    print(f"4**{i} = {float(4**i)}")

# 2. 0도에서 180도까지 10도 단위로, 라디안 값 출력
print("\n=== 각도 -> 라디안 변환 ===")
for degree in range(0, 181, 10):
    radian = math.radians(degree)
    print(f"{degree} degree = {radian:.3f} radian")

# 3. 0도에서 180도까지 10도 단위로, sin 값 출력
print("\n=== sin 값 출력 ===")
for degree in range(0, 181, 10):
    radian = math.radians(degree)
    sin_value = math.sin(radian)
    print(f"sin({degree:3}) = {sin_value:.2f}")

import turtle

t = turtle.Turtle()

# 1. 한 변의 길이가 100 픽셀인 삼각형
for _ in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(-150, 0)  # 위치 이동
t.pendown()

# 2. 한 변의 길이가 200 픽셀인 삼각형
for _ in range(3):
    t.forward(200)
    t.left(120)

t.penup()
t.goto(150, 0)  # 위치 이동
t.pendown()

# 3. 이중 for문으로 삼각형 패턴 (100, 200, 300)
lengths = [100, 200, 300]
for length in lengths:
    for _ in range(3):
        t.forward(length)
        t.left(120)
    t.penup()
    t.forward(50)  # 삼각형 간격
    t.pendown()

t.penup()
t.goto(0, -200)  # 위치 이동
t.pendown()

# 4. 한 변의 길이가 100 픽셀인 정사각형
for _ in range(4):
    t.forward(100)
    t.left(90)

turtle.done()

a = [10, 20, 30]
a[3]
#리스트의 인덱스 범위를 벗어났을 때 발생하는 오류이다.

n = int('20%')
#숫자로 변환할 수 없는 문자열을 int()로 변환하려고 할 때 발생한다.

a = 100 + '200'
#정수와 문자열을 더하려고 할 때 발생하는 타입 오류이다.
# 1. ZeroDivisionError 처리
try:
    result = 10 * (30 / 0)
except ZeroDivisionError as e:
    print("예외 발생:", e)

# 2. ValueError 처리
try:
    x = int(input("정수 x를 입력하세요: "))
except ValueError as e:
    print("예외 발생:", e)

# 3. FileNotFoundError 처리
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
except FileNotFoundError as e:
    print("예외 발생:", e)
a = [1, 2, 3, 4, 5]

try:
    index = int(input("a의 요소를 하나 선택하시오 : "))
    print(f"{index} 은(는) {index}번째 요소입니다.")
except Exception as e:
    print("예외 발생:", e)
    a = [1, 2, 3, 4, 5]

try:
    index = int(input("a의 요소를 하나 선택하시오 : "))
    print(f"{index} 은(는) {index}번째 요소입니다.")
except ValueError:
    print("오류 : 입력 값이 정수나 실수가 아님")


