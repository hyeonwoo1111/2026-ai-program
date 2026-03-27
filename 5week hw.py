'''
# 1. 1부터 10까지 짝수 리스트 생성
even_list = [2, 4, 6, 8, 10]
print(even_list)

# 2. range() 함수를 이용한 짝수 리스트 생성
even_list_range = list(range(2, 11, 2))
print(even_list_range)

# 3. 나라 이름 리스트 생성
nations = ['Korea', 'China', 'India', 'Nepal']
print(nations)

# 4. 친구 이름 리스트 생성
friends = ['길동', '철수', '은지', '지은', '영민']
print(friends)

# 5. 문자열 'XYZ'를 리스트로 변환
string = list('XYZ')
print(string)
'''
'''
# 1. 2~10 사이의 소수 리스트 생성
prime_list = [2, 3, 5, 7]
print("prime_list의 첫 원소 :", prime_list[0])

# 2. prime_list의 마지막 원소 (양수 인덱스 사용)
print("prime_list의 마지막 원소 :", prime_list[3])

# 3. prime_list의 마지막 원소 (음수 인덱스 사용)
print("prime_list의 마지막 원소 :", prime_list[-1])

# 4. 나라 이름 리스트 생성
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print("nations의 첫 원소 :", nations[0])

# 5. nations 리스트의 마지막 원소 (음수 인덱스 사용)
print("nations의 마지막 원소 :", nations[-1])

# 6. nations 리스트의 마지막 원소 (len(nations)-1 인덱스 사용)
print("nations의 마지막 원소 :", nations[len(nations)-1])
'''
'''
# 1. 소수 리스트 생성 후 append()로 11 추가
prime_list = [2, 3, 5, 7]
print("소수 목록 :", prime_list)

prime_list.append(11)
print("추가 후 소수 목록 :", prime_list)

# 2. prime_list에서 3 제거
print("삭제 전 소수 목록 :", prime_list)

prime_list.remove(3)
print("삭제 후 소수 목록 :", prime_list)
'''
'''
# 3. 국가 리스트 생성 후 append()로 'Nepal' 추가
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print("국가 목록 :", nations)

nations.append('Nepal')
print("추가 후 국가 목록 :", nations)

# 4. nations 리스트에 'Japan'과 'Russia'가 있는지 검사
if 'Japan' in nations:
    print("Japan 는(은) 국가 목록에 있습니다.")
else:
    print("Japan 는(은) 국가 목록에 없습니다.")

if 'Russia' in nations:
    print("Russia 는(은) 국가 목록에 있습니다.")
else:
    print("Russia 는(은) 국가 목록에 없습니다.")
'''
'''
# 1. 1~10 사이의 소수 리스트 생성
prime_list = [2, 3, 5, 7]
print("1에서 10까지의 소수 :", prime_list)

print("최소값 :", min(prime_list))
print("최댓값 :", max(prime_list))
print("합계 :", sum(prime_list))
print("평균 :", sum(prime_list) / len(prime_list))

# 2. 국가 리스트 생성
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print("국가 목록 :", nations)

print("사전에 가장 먼저 나오는 나라 :", min(nations))
print("사전에 가장 뒤에 나오는 나라 :", max(nations))
'''
'''
# 1. append()와 extend() 차이 확인
a = [1, 2, 3]
b = [10, 20, 30]

a.append(b)
print("(1) append 결과 :", a)   # [1, 2, 3, [10, 20, 30]]

a = [1, 2, 3]
b = [10, 20, 30]

a.extend(b)
print("(2) extend 결과 :", a)   # [1, 2, 3, 10, 20, 30]

# 2. 1부터 10까지 정수 리스트 생성
nlist = list(range(1, 11))
print("nlist =", nlist)
'''
'''
# 3. insert() 메소드로 맨 앞에 0 삽입
nlist = list(range(1, 11))
nlist.insert(0, 0)
print("nlist =", nlist)

# 4. reverse() 메소드로 역순 정렬
nlist.reverse()
print("nlist =", nlist)

# 5. pop() 메소드로 마지막 원소 반환 및 삭제
last_element = nlist.pop()
print("마지막 원소 =", last_element)
print("nlist =", nlist)
'''
'''
# 1. 사용자로부터 정수 입력받아 리스트 반복
n = int(input("반복할 정수를 입력하십시오 : "))
base_list = [1, 2, 3]

result = base_list * n
print(result)
'''
# 1. range(15)으로 리스트 생성
n_list = list(range(15))
print("n_list =", n_list)

# 2. 슬라이싱 결과들
s_list1 = n_list[0:5]          # [0, 1, 2, 3, 4]
s_list2 = n_list[5:11]         #
