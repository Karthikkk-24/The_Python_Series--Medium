from abc import ABC, abstractmethod

class Class01(ABC):
	def __init__(self):
		pass

class Class02(Class01):
	def __init__(self):
		print("Class02")
kk = Class02()
kk.__init__()