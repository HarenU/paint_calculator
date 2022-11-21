valid = False

while not valid:
    print("""
    (1) Dulux       - coverage 18m^2/L  - £8 per L
    (2) GoodHome    - coverage 15m^2/L  - £6 per L
    (3) Leyland     - coverage 1.3m^2/L - £1.3 per L
    """)

    selectedPaint = input("Please select the paint from the above options using the number: ")
    match selectedPaint:
        case "1":
            brand = "Dulux"
            coverage = 18
            price = 8
            valid = True
        case "2":
            brand = "GoodHome"
            coverage = 15
            price = 6
            valid = True
        case "3":
            brand = "Leyland"
            coverage = 1.3
            price = 1.3
            valid = True
        case _:
            print("invalid input, please make sure the input is a number (e.g. 2)")

valid = False

while not valid:
    print("""
    (1) Red
    (2) White
    (3) Green
    (4) Orange
    (5) Blue
    """) 
    selectedColour = input("Please select the paint from the above options using the number: ")
    match selectedColour:
        case "1":
            colour = "Red"
            valid = True
        case "2":
            colour = "White"
            valid = True
        case "3":
            colour = "Green"
            valid = True
        case "4":
            colour = "Orange"
            valid = True
        case "5":
            colour = "Blue"
            valid = True
        case _:
            print("invalid input, please make sure the input is a number (e.g. 2)")

    print(brand)
    print(coverage)
    print(price)
    print(colour)