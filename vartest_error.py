# vartest_error.py

def vartest(a):
    a = a+1


print(vartest(3))
print(a)  # 함수안에서 선언한 변수는 함수 안에서만 사용 될 뿐 함수 밖에서는 사용되지 않는다.

