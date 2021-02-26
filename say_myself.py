# say_mtself.py

def say_myself(name, old, man=True):
    print("My name is %s" % name)
    print("I am %d." % old)
    if man:
        print("man")
    else:
        print("woman")

say_myself("kim", 30)  # 매게변수에 초깃값 설정시 인수를 적지 않아도 결과값 나온다.
say_myself("kim", 30, True)
say_myself("kim", 30, False)

