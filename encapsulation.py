a = 3
class ParentClass:
	def __init__(self):
		self._b = 5

class ChildClass(ParentClass):
	def __init__(self):
                
		print("Inside ChildClass: ",a)
		ParentClass.__init__(self)
		print("Inside ChildClass", self._b)

object1 = ChildClass()
object2 = ParentClass()

print("Outside all classes: ", a)


print("Outside all classes (Object (Parent Class)): ", object2._b)
print("Outside all classes (Object (Child Class)): ", object1._b)