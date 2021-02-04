from abc import ABC, abstractmethod
class a(ABC):
	def wors(self):
		print("you can ")

class b(a):
	def work(self):
		print("hoow yu can ")
b1=b()
a1=a()
b1.work(a1)