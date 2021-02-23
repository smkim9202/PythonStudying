# 02장 연습문제 Q12

def namecapy(a,b):
    if id(a) == id(b):
        return 'a is b'
    else:
        return 'a is not b'

A = B = [1, 2, 3]
A[1] = 4
print(namecapy(A,B))