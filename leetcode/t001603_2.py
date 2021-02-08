class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.mapPark = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.mapPark[carType - 1] == 0:
            return False
        else:
            self.mapPark[carType - 1] -= 1
            return True