import math

class Paint:
    def __init__(self, brand, pricePerL, colour, coverage):
        self.brand = brand
        self.colour = colour
        self.price = pricePerL
        self.coverage = coverage
        
    def paintReq(self, area):
        paintReq = area/self.coverage
        return paintReq

    def totalPrice(self, amount):
        totalPrice = amount * self.price
        return totalPrice


class Wall:
    def __init__(self, height, width, door, socket):
        self.initialArea = height*width
        self.door = door
        self.socket = socket
        
    def calculateArea(self):
        doorArea = 1.6*float(self.door)
        socketArea = 0.013*float(self.socket)
        self.area = round(self.initialArea - socketArea - doorArea, 2)

if __name__ == "__main__":
    # Allows the user to select the paint they want to use
    def paintSelector():
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

        return Paint(brand, price, colour, coverage)



    # Calculates area of window(s) on wall
    def calculateWindowArea(window, wall):
        valid = False
        while not valid:
            try:
                height = float(input(f"Please enter the height of Window {window} on wall {wall+1}: "))
                width = float(input(f"Please enter the width of Window {window} on wall {wall+1}: "))
                valid = True
            except ValueError:
                print("Please enter a proper number")
            

        return height * width

    # Calculates number of buckets required for certain area (outputs an array of [10L, 5L, 2.5L, 1L])
    def calculateBuckets(area):
        XLBucket = 0
        LBucket = 0
        MBucket = 0
        SBucket = 0

        if area >= 10:
            XLBucket += math.floor(area/10)
            area -= math.floor(area/10) * 10
        
        if area >= 5:
            LBucket += math.floor(area/5)
            area -= math.floor(area/5) * 5
        
        if area >= 2.5:
            MBucket += math.floor(area/2.5)
            area -= math.floor(area/2.5) * 2.5
        
        if area > 0:
            SBucket += math.ceil(area/1)
            area -= math.ceil(area/1) * 1
            
        return [XLBucket, LBucket, MBucket, SBucket]

    # Calculating total price using number of buckets and price per litres
    def calculatePrice(bucket, price): 
        totalLitre = 0
        totalLitre += bucket[0] * 10
        totalLitre += bucket[1] * 5
        totalLitre += bucket[2] * 2.5
        totalLitre += bucket[3]

        
        totalPrice = totalLitre*price

        return totalPrice

    # Calculates the area of wall minus doors, sockets, windows
    def calculateWallArea(wall):
        valid = False
        while not valid:
            try:
                height = float(input("what is the height in meters?: "))
                width = float(input("what is the width in meters?: "))
                valid = True
            except ValueError:
                print("Please enter a proper number")
        valid = False
        while not valid:
            try:
                socket = int(input("How many Sockets?: "))
                door = int(input("How many Doors?: "))
                valid = True
            except ValueError:
                print("Please enter a proper number")
        valid = False
        while not valid:
            try:
                window = int(input("How many Windows?: "))
                valid = True
            except ValueError:
                print("Please enter a proper number")
            


        windowArea = 0
        if window > 0:
            for x in range(window):
                windowArea += calculateWindowArea(x+1, wall)

        wallArea = Wall(height, width, door, socket)
        wallArea.calculateArea()

        return wallArea.area - windowArea

    totalWallArea = 0.0
    valid = False
    while not valid:
        try:
            wall = int(input("How many walls would you like to paint? "))
            valid = True
        except ValueError:
                print("Please enter a proper number")

    for i in range(wall):
        print(f"===== WALL {i+1} =====")
        totalWallArea += calculateWallArea(i)

    coats = int(input("How many coats of paint would you like to apply? "))
    totalWallArea *= coats

    paint1 = paintSelector()

    


    print(f"Total area to paint is { round(totalWallArea, 2)} m^2")

    reqPaint = paint1.paintReq(totalWallArea)
    print(f"Total paint required is {round(reqPaint, 2)}L")

    buckets = calculateBuckets(round(reqPaint, 2))
    fPrice = calculatePrice(buckets,paint1.price)
    
    print(f"""Total is £{round(fPrice, 2):.2f} for: 
    {buckets[3]} 1L bucket(s)
    {buckets[2]} 2.5L bucket(s)
    {buckets[1]} 5L bucket(s)
    {buckets[0]} 10L bucket(s)
    Order is for {paint1.brand} brand for {paint1.colour} colour""")

