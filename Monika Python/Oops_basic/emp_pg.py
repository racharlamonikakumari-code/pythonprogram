class Employee:
  def __init__(self,emp_id,name,basic):
    self.emp_id= emp_id
    self.name=name
    self.basic= basic
    self.da=0.10*basic
    self.hra=0.20*basic

  def show(self):
    print("Employee ID=",self,emp_id)
    print("Employee Name=",self.name) 
    print("Basic Salary=",self.basic)
    print("Da=",self.da)
    print("HRA=",self.hra)

  def total_salary(self):
    return self.basic + self.da + self.hra  

print("enter how many employee:")
L=[]
s=int(input())   

for i in range(s):
	print("\nEnter Employee", i+1, "details")

	emp_id = input("Enter Employee ID: ")  
	name = input("Enter Employee Name: ")
	basic = float(input("Enter Basic Salary: "))

	e = Employee(emp_id, name, basic)
	L.append(e)

for i in L:
	i.show()
	print("Total Salary =", i.total_salary())
	print("-" * 40) 