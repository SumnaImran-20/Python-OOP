print("---Hybrid Inheritance---")
class PC:
    def fun1(self):
        print("This is PC class")

class Laptop(PC):
    def fun2(self):
        print("This is Laptop class inheriting PC class")

class Mouse(Laptop):
    def fun3(self):
        print("This is Mouse class inheriting Laptop class")

class Student(Mouse,Laptop):
    def fun4(self):
        print("This is Student class inheriting Laptop class and Mouse Class")

obj = Student()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()
print("---------------")
obj1 = Mouse()
obj1.fun1()
obj1.fun2()
obj1.fun3()


