# 04장 연습문제 Q7

with open("test.txt", 'r') as f:
    newtest = f.read()

newtest = newtest.replace("python", "java")

with open("test.txt", 'w') as f:
    f.write(newtest)