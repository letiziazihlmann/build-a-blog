class Rectangle:

    def __int__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def getPerimeter(self):
        return self.length * 2 + self.width * 2

    def isLarger(self, areaofotheR):
        if getArea(self) > areaofotherR:
            return "The rectangle is larger."
        else:
            return "The rectangle is smaller."

    def isSquare(self):
        if self.length == self.width:
            return "The rectangle is a square."
        else:
            return "The rectangle is not a square."


rectangle1 = Rectangle(4,5)

rectangle1.isSquare()
rectangle1.getPerimeter()
