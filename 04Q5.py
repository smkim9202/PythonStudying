# 04장 연습문제 Q5

f1 = open("test.txt", 'w')
f1.write("Life is too short\n")
f1.close()
"""
with open("test.txt", 'w') as f1:
    f1.write("Life is too short\n")
"""

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
"""
with open("test.txt", 'r') as f2:
    print(f2.read())
"""
