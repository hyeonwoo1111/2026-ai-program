'''
# 게임 점수 판별 프로그램
game_score = int(input("게임 점수를 입력하세요: "))

print("game_score =", game_score)

if game_score >= 1300:
    print("당신은 고수입니다")
'''
'''
# 두 값 비교 프로그램
num_a = int(input("첫 번째 숫자를 입력하세요: "))
num_b = int(input("두 번째 숫자를 입력하세요: "))

print("num_a =", num_a, ", num_b =", num_b)

if num_a == num_b:
    print("두 값이 일치합니다.")
'''
'''
# 1에서 100 사이의 정수 입력받기
n = int(input("정수를 입력하세요: "))

print("n =", n)

# 짝수 판별
if n % 2 == 0:
    print(n, "은(는) 짝수입니다.")
'''
'''
# -100에서 100 사이의 정수 입력받기
x = int(input("정수를 입력하세요: "))

print("x =", x)

# 자연수 판별
if x > 0:
    print(x, "은(는) 자연수입니다.")
'''
'''
# 게임 점수 판별 프로그램 (if-else 사용)
game_score = int(input("게임점수를 입력하시오: "))

print("game_score =", game_score)

if game_score >= 1000:
    print("고수입니다.")
else:
    print("입문자입니다.")
'''
'''
# 두 정수를 입력받아 비교하는 프로그램
num_a = int(input("한 정수를 입력하십시오: "))
num_b = int(input("다른 정수를 입력하십시오: "))

if num_a == num_b:
    print("두 값이 일치합니다.")
else:
    print("두 값이 일치하지 않습니다.")
'''
'''
# 성인 여부와 결혼 여부 판별 프로그램

adult = int(input("당신은 성인인가요(성인이면 1, 미성년이면 0): "))

if adult == 0:
    print("당신은 미성년자입니다.")
else:
    married = int(input("결혼을 하셨나요(기혼이면 1, 미혼이면 0): "))
    if married == 1:
        print("당신은 결혼한 성인입니다.")
    else:
        print("당신은 결혼하지 않은 성인입니다.")
'''
'''
num = int(input("숫자를 입력하세요.: "))
print(num > 1 and num < 10)
'''
'''
age = int(input("나이를 입력하세요: "))

if age > 10 and age < 19:
    print("청소년입니다.")
'''
# 자동차 속도 판별 프로그램
speed = int(input("자동차의 속도를 입력하세요(단위 : km/h): "))

if speed >= 100:
    print("고속")
elif speed >= 60:
    print("중속")
else:
    print("저속")
