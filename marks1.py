# marks1.py

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d 학생 합격입니다." % number)
    else:
        print("%d 학생 불합격입니다." % number)
