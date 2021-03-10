# 구구단 프로그램

def GuGu(N):
    gugudan = []
    for i in range(1, 10):
        gugudan.append(i * N)
    return gugudan

num = int(input())
print(GuGu(num))
