## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a animal
class Dog(Animal):
	def __init__(self,name):
		## Has-a name
		self.name = name

## Cat is-a animal
class Cat(Animal):
	def __init__(self,name):
		## Has-a name
		self.name = name

## Person is-a object
class Person(object):
	def __init__(self, name):
		## Has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is a Person
class Employee(Person):
	def __init__(self, name, salary):
		## Is super calling the Person class init?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## Satan is-a cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary's pet is Satan
mary.pet = satan

## Frank is an employee
frank = Employee("Frank",120000)

## Frank's pet is Rover
frank.pet = rover

## Flipper is a fish
flipper = Fish()

## crouse is-a Fish
crouse = Salmon()

## Harry is a Halibut
harry = Halibut()


	
