from threading import*   #importing a thread packing
from time import*
class a(Thread):
	def run(self):            # run is a inbuilt in threading 
		for i in range(5):
			print("a")
			sleep(1)
class b(Thread):
	def run(self):
		for i in range(5):
			print("b")
			sleep(1)      #using sleeping method
a1=a()
b1=b()
a1.start()      #using start we call run because run is in built in start
sleep(0.5)
b1.start()

