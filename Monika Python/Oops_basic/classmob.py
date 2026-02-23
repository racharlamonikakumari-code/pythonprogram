Class Mobile:
  def _init_(self,brand,model,price):
    self.brand=brand
    self.model=model
    self.price=price
  def show (self):
    print ("Mobile Details:")
    print ("Brand:",self.brand)
    print ("Model:",self.model)
    print ("Price:",self.price)
  def update price(self,new_price):
    self.price=new_price
    print("price updated to:",self price)
print ("enter mobile model:") 
brand=input()
print ("enter mobile model:")
model=input()
print ("enter mobile price:")
price=float(input())
m=mobile(brand,model,price)
m.show()
print (enter new price to update:")
new_price=float(input())
m.update_price(new_price)
m.show()
