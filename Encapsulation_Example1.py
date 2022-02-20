print("---Encapsulation Example---")
class Mobile:
    #data Members
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model= model
        self.price = price

    #Methods
    # to display employee's details
    def call(self,number):
        # accessing public data member
        print("Calling to "+ str(number))
    
    #Methods
    def main(self):
        return self.brand+" "+str(self.price)

obj = Mobile("Cell",1100,25000)
obj.call(123456789)
# calling public method of the class
print(obj.main())