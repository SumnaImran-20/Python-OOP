#Creating Base Class/Parent Class
print("---Hierarchical Inheritance---")
class Brands:
    brand_name_1= "Amazon"
    brand_name_2= "Ebay"
    brand_name_3= "OLX"

#Creating Derived Class/Child Class
class Products(Brands):
    prod_1= "Online Ecommerce Store"
    prod_2= "Online Store"
    prod_3 ="Onlie Buy Sell Store"

#Creating Derived Class/Child Class
class Popularity(Brands):
    prod_1_popularity= 100
    prod_2_popularity= 10
    prod_3_popularity = 60

class Value(Brands):
    prod_1_value = "Excellent Value"
    prod_2_value = "Better Value"
    prod_3_value = "Good Value"

#Creating Object
obj1 = Products()
obj2 = Popularity()
obj3 = Value()
print(obj1.brand_name_1 + " is an "+ obj1.prod_1)
print(obj1.brand_name_2 + " is an "+ obj1.prod_2)
print(obj1.brand_name_3 + " is an "+ obj1.prod_3)
print()
print(obj2.brand_name_1 + " has a popularity of "+ str(obj2.prod_1_popularity))
print(obj2.brand_name_2 + " has a popularity of"+ str(obj2.prod_2_popularity))
print(obj2.brand_name_3 + " has a popularity of "+ str(obj2.prod_3_popularity))
print()
print(obj3.brand_name_1 + " has an "+ obj3.prod_1_value)
print(obj3.brand_name_2 + " has a popularity of"+ obj3.prod_2_value)
print(obj3.brand_name_3 + " has a popularity of "+ obj3.prod_3_value)
