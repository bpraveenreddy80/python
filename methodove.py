#operator overloading
class a:                               #defining class a
	def __init__(self,m1,m2):          #creating constructor
		self.m1=m1
		self.m2=m2
	def show(self):                   #user defined func
		print(self.m1,self.m2)
	def __add__(self,other):            #0verloading add func
		m1=self.m1+self.m2
		m2=other.m1+other.m2
		a3=a(m1,m2)                     #creating a3 and passing m1 and m2 var m1 and m2 will store (a1.m1+a1.m2)
		return a3	
	def __str__(self):                  #printing the values instead of address using __str__()fun
		return	self.m1,self.m2
	def __gt__(self,other):             #0verlaoding the __gt__()fun to perform on obj
		r1=self.m1+self.m2
		r2=other.m1+other.m2
		r3=a(r1,r2)
		if r1>r2:
			return 1
		else:
			return 0
a1=a(10,20)
a2=a(10,200)
a1.show()
a2.show()
a3=a1+a2

print(a1.__str__(),a2.__str__(),a3.__str__()) #printing all the values of obj 

if  a1>a2:        #comparing two obj 
	print("a1 is grater")
elif a1<a2:
	print("a2 is greater")
else:
	print("a1 and a2 are same")

