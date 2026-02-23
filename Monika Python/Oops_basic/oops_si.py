class SimpleInterest:

    def __init__(self):     
        self.principal = 6000
        self.rate = 5
        self.time = 2

    def show(self):
        print("Principal =", self.principal)
        print("Rate =", self.rate)
        print("Time =", self.time)

    def calculate(self):
        si = (self.principal * self.rate * self.time) / 100
        print("Simple Interest =", si)

s = SimpleInterest()

s.show()
s.calculate()