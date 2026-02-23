class Square:
    def __init__(self):     
        self.length = 6

    def show(self):
        print("Square length =", self.length)

    def area(self):
        print("Area of square =", self.length * self.length)

    def perimeter(self):
        return 4 * self.length

s = Square()

s.show()
s.area()
print("Perimeter of square =", s.perimeter())
