# coffee.py
coffee = 10
while True:
    money = int(input("Please insert a coin.\ncoin: "))
    if money == 300:
        print("Here's your coffee!")
        coffee = coffee - 1
        print("%d coffees left." %coffee)
    elif money > 300:
        print("Here's your coffee and change of %dwon!" %(money - 300))
        coffee = coffee - 1
        print("%d coffees left." %coffee)
    else:
        print("short of coins...")
        print("%d coffees left..." %coffee)
    if coffee == 0:
        print("sold out!")
        break
