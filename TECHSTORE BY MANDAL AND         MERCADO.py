print("GROUP BY : KEVIN MANDAL AND MERCADO EXECLE")
print("=" * 40)
print("               TECH STORE")
print("=" * 40)

print("\nMENU STORE")
print("[K]  Keyboard    - 600")
print("[M]  Mouse       - 400")
print("[MT] Monitor     - 1000")
print("[S]  System Unit - 3000")
print("[H]  Headset     - 300")
print("[MP] Mouse Pad   - 100")
print("=" * 40)
print("NOTE: STUDENT HAS 30% AND ADULT HAS 10%!")

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

elif Product1 == "H":
    price1 = 300
    product1 = "Headset"

elif Product1 == "MP":
    price1 = 100
    product1 = "MousePad"

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

elif Product2 == "H":
    price2 = 300
    product2 = "Headset"

elif Product2 == "MP":
    price2 = 100
    product2 = "MousePad"

else:
    price2 = 0
    product2 = "None"

Qty2 = int(input("Enter Quantity: "))

Product3 = input("Enter Third Product Code: ").upper()

if Product3 == "K":
    price3 = 600
    product3 = "Keyboard"

elif Product3 == "M":
    price3 = 400
    product3 = "Mouse"

elif Product3 == "MT":
    price3 = 1000
    product3 = "Monitor"

elif Product3 == "S":
    price3 = 3000
    product3 = "System Unit"

elif Product3 == "H":
    price3 = 300
    product3  = "Headset"

elif Product3 == "MP":
    price3 = 100
    product3 = "MousePad"

else:
    price3 = 0
    product3 = "None"

Qty3 = int(input("Enter Quantity :"))

Subtotal1 = price1 * Qty1
Subtotal2 = price2 * Qty2
Subtotal3 = price3 * Qty3
Subtotal = Subtotal1 + Subtotal2 + Subtotal3

if Subtotal >= 2000:

    Student = input("Are you Student? (Yes/No): ").upper()

    if Student == "YES":
        dis = 30
        print("Congrats you Received 30% Discount!")

    elif Student == "NO":
        dis = 10
        print("Congrats you Received 10% Discount!")

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
print(f"Product  3         : {product3}")
print(f"Quantity 3         : {Qty3}")

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