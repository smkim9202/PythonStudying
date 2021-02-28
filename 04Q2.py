# 04장 연습문제 Q2

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)


print(avg_numbers(4,3,2,1))

print(avg_numbers(10,20,50))