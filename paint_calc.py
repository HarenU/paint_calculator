class Paint:
    def __init__(self, brand, price, capacity, colour):
        self.brand = brand
        self.colour = colour
        self.price = price
        self.capacity = capacity

    def calculatePrice(self, area, coats):
        paintReq = (area/6)*coats
        totalPrice = paintReq*self.price

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
    def calculateWindowArea(window, wall):
        height = float(input(f"Please enter the height of Window {window} on wall {wall+1}: "))
        width = float(input(f"Please enter the width of Window {window} on wall {wall+1}: "))

        return height * width

    def calculateWallArea(wall):
        height = float(input("what is the height in meters?: "))
        width = float(input("what is the width in meters?: "))
        socket = int(input("How many Sockets?: "))
        door = int(input("How many Doors?: "))
        window = int(input("How many Windows?: "))

        windowArea = 0
        if window > 0:
            for x in range(window):
                windowArea += calculateWindowArea(x+1, wall)

        wallArea = Wall(height, width, door, socket)
        wallArea.calculateArea()

        return wallArea.area - windowArea

    totalWallArea = 0.0
    wall = int(input("How many walls would you like to paint? "))

    for i in range(wall):
        print(f"===== WALL {i+1} =====")
        totalWallArea += calculateWallArea(i)

    coats = int(input("How many coats of paint would you like to apply? "))
    totalWallArea *= coats

    print(f"Total area to paint is { round(totalWallArea, 2)} m^2")



