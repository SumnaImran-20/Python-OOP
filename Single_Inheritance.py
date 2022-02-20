#Creating Base Class/Parent Class
print("---Single Inheritance---")
class Brands:
    brand_name_1= "Amazon"
    brand_name_2= "Ebay"
    brand_name_3= "OLX"

#Crreating Derived Class/Child Class
class Products(Brands):
    prod_1= "Online Ecommerce Store"
    prod_2= "Online Store"
    prod_3 ="Onlie Buy Sell Store"

#Creating Object
obj = Products()
print(obj.brand_name_1 + " is an "+ obj.prod_1)
print(obj.brand_name_2 + " is an "+ obj.prod_2)
print(obj.brand_name_3 + " is an "+ obj.prod_3)
