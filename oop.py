"""
class Patient:
	def __init__(self, name, surname, age, health): #health is a int from 1 to 100 if health <50 put into hospital 
		self.name= name
		self.surname= surname
		self.age= age
		self.health= health
		
	def get_health(self):
		return self.health


class Hospital:
	def __init__(self, name, capacity):
		self.name= name
		self.capacity= capacity
		self.patients= []
	
	def add_patient(self, patient):
		if (len(self.patients) < self.capacity):
			self.patients.append(patient)
			return True
		return False

	def getdetail(self):
		for i in self.patients:
			print(i)



p1= Patient("Taner","Paker", 19, 90)
p2= Patient("Hasan","Mezarcı", 80, 30)
p3= Patient("Tayyip","Erdoğan", 70, 1)
p4= Patient("Adolf","Hitler", 79, 10)
p5= Patient("Joseph","Stalin", 89, 31)
p6= Patient("Kim","Jongun", 34, 64)

h1= Hospital("medicalpark", 4)

#print(h1.add_patient(p1))
#print(h1.add_patient(p2))
#print(h1.add_patient(p3))
#print(h1.add_patient(p4))
#print(h1.add_patient(p5))
#print(h1.add_patient(p6))
"""
#--------------------INHERITENCE-------------------------------------------------------
"""
class Pet:
	def __init__(self, name, age):
		self.name= name
		self.age= age
	
	def show(self):
		txt= "I am {} and i am {} " 
		print(txt.format(self.name, self.age))
		
	def speak(self)
		print("I dont know what to say")
class Cat(Pet):
	
	def speak(self):
		print("Meow")	
		
class Dog(Pet):
		
	def speak(self):
		print("Bark")

p1= Cat("pasa", 4)
p2= Cat("kedi", 2)
p3= Dog("Kurt", 5)

p1.speak()
p2.speak()
p3.speak()				
		
#note that the speak method is defined both in the parent class and the child classes in that case the speak() method in the parent will be overwritten
"""
#lets say we want to add one attribute to cat the proper way to do that would be like this 
"""
class Pet:
	def __init__(self, name, age):
		self.name= name
		self.age= age
	
class Cat:
	def __init__(self, name, age, color):
		super().__init__(name, age) #this means call the __init__ method and pass name, age to that method 
		self.color= color

class Dog:
	def speak(self):
		print("Woof")
"""

#------------Class atributes----------------------------
"""
class Person:
	number_of_people= 0 #this is class attribute and its not defined inside a method so its defined inside the entire class
	
	def __init__(self, name):
		self.name= name

p1= Person("tayyip")
p1= Person("erdogan")
print(p1.number_of_people)  #outputs 0
print(Person.number_of_people) #outputs 0
Person.number_of_people= 1
print(p2.number_of_people) #outputs 1
"""

#This is usefull because we can keep track of how many instances we have created 
"""
class Person:
	number_of_people= 0
	
	def __init__(self,name):
		self.name= name
		number_of_people += 1
"""
#--------------Class Methods----------------------------	
"""
class Person:
	number_of_people= 0
	
	def __init__(self, name, age):
		self.name= name
		self.age= age
	
	
	@classmethod   #this is a decorator 
	def number_of_people_(cls):
		return cls.number_of_people	
	#class methods acts on the class itself 	
		
	@classmethod 
	def add_person(cls):
		cls.number_of_people += 1

print(Person.number_of_people_())
"""
#--------------Static Methods----------------------		
#Sometimes we want to create classes that organise functions 
"""
class Math:
	#Lets define some functions that are not specific to an instance
	
	@staticmethod
	def add5(x):
		return x+5	

print(Math.add5(5))
"""
#---------try:, except:, else:----------
"""
try: 
	X= 3+3
		
except:
	"Well that didnt work"

else:
	"That did work"
"""

