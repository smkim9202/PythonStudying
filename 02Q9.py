# 02장 연습문제 Q9

a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' 딕셔너리 키 값으로 변형 할 수 있는 값은 사용 할 수 없음으로 리스트는 키 값이 될 수 없다.
a[250] = 'python'

print(a)