print("=" * 40)
print("             TECH STORE")
print("=" * 40)

print("\nMENU STORE")
print("[K] Keyboard - 600")
print("[M] Mouse - 400")
print("[MT] Monitor - 1000")
print("[S] System Unit - 3000")

Name = input("Enter your Name: ")
Product1 = input("Enter First Product Code: ").upper()
Qty1 = int(input("Enter Quantity: "))

if Product1 == "K":
    price1 = 600
    product1 = "Keyboard"

elif Product1 == "M":
    price1 = 400
    product1 = "Mouse"

elif Product1 == "MT":
    price1 = 1000
    product1 = "Monitor"

elif Product1 == "S":
    price1 = 3000
    product1 = "System Unit"

else:
    print("INVALID PRODUCT!")
    exit()

Product2 = input("Enter Second Product Code: ").upper()

if Product2 == "K":
    price2 = 600
    product2 = "Keyboard"

elif Product2 == "M":
    price2 = 400
    product2 = "Mouse"

elif Product2 == "MT":
    price2 = 1000
    product2 = "Monitor"

elif Product2 == "S":
    price2 = 3000
    product2 = "System Unit"

else:
    price2 = 0
    product2 = "None"

Qty2 = int(input("Enter Quantity: "))

Subtotal1 = price1 * Qty1
Subtotal2 = price2 * Qty2
Subtotal = Subtotal1 + Subtotal2

if Subtotal >= 2000:

    Student = input("Are you Student? (Yes/No): ").upper()

    if Student == "YES":
        dis = 50
        print("Congrats you Receive 50% Discount!")

    elif Student == "NO":
        dis = 20
        print("Congrats you Receive 20% Discount!")

    else:
        dis = 0
        print("Invalid Answer!")

else:
    dis = 0
    print("No Discount!")

Discount_rate = dis / 100
Discount_Amount = Subtotal * Discount_rate
TotalDueAmount = Subtotal - Discount_Amount

CashP = int(input("Enter Cash Payment: "))

if CashP >= TotalDueAmount:
    change = CashP - TotalDueAmount

else:
    print("INSUFFICIENT PAYMENT!")
    exit()

print("=" * 40)
print("             RECEIPT")
print("=" * 40)

print(f"Name               : {Name}")
print(f"Product  1         : {product1}")
print(f"Quantity 1         : {Qty1}")
print(f"Product  2         : {product2}")
print(f"Quantity 2         : {Qty2}")

print("=" * 40)

print(f"Subtotal            : P{Subtotal:.2f}")
print(f"Discount Percentage : {dis}%")
print(f"Discount Amount     : P{Discount_Amount:.2f}")
print(f"Total Amount Due    : P{TotalDueAmount:.2f}")
print(f"Cash Payment        : P{CashP:.2f}")
print(f"Change              : P{change:.2f}")

print("=" * 40)
print("THANK YOU FOR PURCHASING AND GOD BLESS!!")
print("=" * 40)





















