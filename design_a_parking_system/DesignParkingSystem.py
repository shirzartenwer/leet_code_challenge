

# https://leetcode.com/problems/design-parking-system/
class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType is 1:
            if self.big > 0:
                self.big -= 1
                return True
        elif carType is 2:
            if self.medium > 0:
                self.medium -= 1
                return True
        elif carType is 3:
            if self.small > 0:
                self.small -= 1
                return True
        
        return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)