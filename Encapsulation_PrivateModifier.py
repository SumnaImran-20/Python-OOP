print("---Encapsulation Example Private Modifier---")
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

# accessing private data members
print('Salary:', emp._Employee__salary)

#accessing private data members by using name mangling
#print('Salary:', emp._Employee__salary)