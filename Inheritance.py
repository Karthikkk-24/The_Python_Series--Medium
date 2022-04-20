class Animal:
	def speak(self):
		print("Animal Speaking")
class Dog(Animal):
	def bark(self):
		print("Dog Barking")

d = Dog()
d.bark()
d.speak()
# code from javatpoint "https://www.javatpoint.com/inheritance-in-python"