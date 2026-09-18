class ParkingSystem:

    def __init__(self, big, medium, small):
        self.spaces = [0, big, medium, small]

    def addCar(self, carType):
        if self.spaces[carType] > 0:
            self.spaces[carType] -= 1
            return True
        return False