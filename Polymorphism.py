print("---Polymorphim---")
class Laptop:
    def laptop(self):
        print("a computer that is portable and suitable for use while travelling.")
        print()

class Dell(Laptop):
    def laptop(self):
        print("Dell is an American multinational computer technology company that develops.")
        print()
    
class Hp(Laptop):
    def laptop(self):
        print("The HP is applied to both desktop and laptop for the home and home office product range.")

L = Laptop()
L.laptop()
D = Dell()
D.laptop()
H = Hp()
H.laptop()

