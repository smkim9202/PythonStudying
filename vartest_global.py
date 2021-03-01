# vartest_global.py

a = 1
def vartest():
    global a  #함수 밖의 변수 a를 직접 사용하겠다는 뜻이다.
    a = a + 1

vartest()
print(a)