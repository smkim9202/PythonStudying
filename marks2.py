# marks2.py

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60: continue
    print("%d 학생 축하합니다. 합격입니다." % number)