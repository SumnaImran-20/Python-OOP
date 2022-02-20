#Creating Base Class/Parent Class
print("---Multiple Inheritance---")
class Brands:
    brand_name_1= "Amazon"
    brand_name_2= "Ebay"
    brand_name_3= "OLX"

#Creating Derived Class/Child Class
class Products:
    prod_1= "Online Ecommerce Store"
    prod_2= "Online Store"
    prod_3 ="Onlie Buy Sell Store"

#Creating Derived Class/Child Class
class Popularity(Brands,Products):
    prod_1_popularity= 100
    prod_2_popularity= 10
    prod_3_popularity = 60

#Creating Object
obj = Popularity()
print(obj.brand_name_1 + " is an "+ obj.prod_1+" and popularity is "+ str(obj.prod_1_popularity))
print(obj.brand_name_2 + " is an "+ obj.prod_2+" and popularity is "+ str(obj.prod_2_popularity))
print(obj.brand_name_3 + " is an "+ obj.prod_3+" and popularity is "+ str(obj.prod_3_popularity))