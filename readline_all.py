# readline_all.py

f = open('new.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line, end='')
f.closer()