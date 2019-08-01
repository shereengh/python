import datetime

class Employee(object):
	def __init__(self, name, age, salary, employment_date):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date
		datetime_object = datetime.datetime.now()

	def get_working_years(self):
		datetime_object = datetime.datetime.now()
		return int(datetime_object.year) - int(self.employment_date)

	def printI(self):
		print("name: "+self.name+", age: "+str(self.age)+", salary: "+str(self.salary)+", working years: "+str(self.get_working_years()))


class Manager(Employee):
	def __init__(self, name, age, salary, employment_date,bonus_percentage):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date
		self.bonus_percentage = bonus_percentage
		datetime_object = datetime.datetime.now()

	def get_working_years(self):
		datetime_object = datetime.datetime.now()
		return int(datetime_object.year) - int(self.employment_date)

	def get_bonus(self):
		return float(self.bonus_percentage) * int(self.salary)
	
	def printI(self):
		print("name: "+self.name+", age: "+str(self.age)+", salary: "+str(self.salary)+", working years: "+str(self.get_working_years())+", bonus: "+str(self.get_bonus()))


e_list = []
m_list = []

print("Welcome to HR Pro 2019")
print("Choose an action to do:")
print("  1. show employees")
print("  2. show managers")
print("  3. add an employee")
print("  4. add a manager")
print("  5. exit")
ch = input("what would you like to do?")

while int(ch) != 5:
	print("-" * 20)
	if int(ch) == 1:
		print("Employees")
		if not e_list:
			print("There are no employees added yet.")
		else:
			for i in e_list:
				i.printI()
		print("-" * 20)

	elif int(ch) == 2:
		print("Managers")
		if not m_list:
			print("There are no managers added yet.")
		else:
			for i in m_list:
				i.printI()
		print("-" * 20)

	elif int(ch) == 3:
		name=input("name: ")
		age=input("age: ")
		salary=input("salary: ")
		employment_date=input("employmement year: ")
		emp= Employee(name,age,salary,employment_date)
		e_list.append(emp)
		print("Employee added succesfully")

	elif int(ch)==4:
		name=input("name: ")
		age=input("age: ")
		salary=input("salary: ")
		employment_date=input("employmement year: ")
		bonus=input("bonus percentage: ")
		emp= Manager(name,age,salary,employment_date,bonus)
		m_list.append(emp)
		print("Employee added succesfully")
	elif int(ch)==5:
		break
	else:
		print("Invalid input.")
	ch = input("what would you like to do?")
