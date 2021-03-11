# 3과 5의 배수 합하기

n = 1
result = 0
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        result += n
    n = n + 1
print(result)


result2 = 0
for N in range(1, 1000):
    if N % 3 == 0 or N % 5 == 0:
        result2 += N
print(result2)
