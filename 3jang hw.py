'''
for _ in range(5):
    print("Hello, Python!")
'''
'''
for i in range(5):
    print(i)
'''
'''
numbers = list(range(1, 101))
print(numbers)
'''
'''
total = 0
for i in range(1, 101):
    total += i
print("1부터 100까지의 합:", total)
'''
'''
even_sum = 0
for i in range(0, 101, 2):
    even_sum += i
print("1부터 100까지 짝수의 합:", even_sum)
'''
'''
odd_sum = 0
for i in range(1, 101, 2):
    odd_sum += i
print("1부터 100까지 홀수의 합:", odd_sum)
'''
n = 7

for i in range(n):          # i는 0~6
    st = ''
    for j in range(n - i - 1):  # 공백 개수는 (n - i - 1)
        st = st + ' '
    print(st + '#')
