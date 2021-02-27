# 04장 연습문제 Q1

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(454))
print(is_odd(3))

odd = lambda x: True if x % 2 == 1 else False

print(odd(454))
print(odd(3))

