# coffee2.py
coffee = 10
while coffee > 0:
    money = int(input("돈을 넣어주세요.\n동전:"))
    if money == 300:
        print("커피 나왔습니다!")
        coffee = coffee - 1
        print("현재 커피가 %d개 남았습니다." %coffee)
    elif money > 300:
        print("거스름돈 %d원 입니다. 커피 받아가세요~!" %(money -300))
        coffee = coffee - 1
        print("현재 커피가 %d개 남았습니다." %coffee)
    else:
        print("돈이 모자라요.. 커피를 줄 수 없습니다...")
        print("현재 커피가 %d개 남았습니다." %coffee)
    if coffee == 0:
        print("sold out!")
