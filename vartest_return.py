# vartest_return.py

a = 1
def vartest(a):
    a = a + 1
    return a

print(a)   #함수 밖의 a변수
a = vartest(a) #매개변수 a와 함수 밖에서 선언 된 a변수는 다르다.
print(a) # a 변수에 다른 값을 대입해서 결과 값이 바뀌었다.