# coffee.py

coffee = 10
while True:
    money = int(input("insert coins: "))
    if money == 300:
        print("give coffee")
        coffee -= 1
    elif money > 300:
        print("give coffee. give %d coins" %(money-300))
        coffee -= 1
    else:
        print("give %d coins" %money)
    if coffee == 0:
        print("coffee sold out")
        break