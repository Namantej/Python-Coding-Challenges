#User's Money
balance = int(input("Enter your bank balance: "))
while balance > 0:
    if balance > 100:
        print("Give me your money")
    elif balance > 50:
        print("Buy me some coffee,you cheap!")
    elif balance <= 50:
        print("You are a poor guy, go away!")
    balance = int(input("Enter your bank balance: "))


