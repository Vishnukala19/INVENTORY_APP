from datetime import date
import re

class Product:
    'Python oops applied'
    def __init__(self,product_id =None,productname=None,unit_price=None,category_id=None,manufacture_date=None,is_active="Y"):
        self.__product_id = product_id
        self.__productname = productname
        self.__unit_price = unit_price
        self.__category_id = category_id
        self.__manufacture_date = manufacture_date if manufacture_date else date.today()
        self.__is_active = is_active

        #--------------
        #getters and setters
    def get_productid(self):
        return self.__product_id
    def set_product_id(self,productid):
        self.__product_id = productid

    def get_productname(self):
        return self.__productname
    def set_productname(self,productname):
        pattern = re.compile(r"^[A-Za-z_]{2,30}$")   

        while True:
            if pattern.match(productname):
                self.__productname = productname
                break
            else:

                print("\t\t Invalid product name must have only alphabets")
                productname = input("\t\t Enter product name again: ")  

    def get_unit_price(self):
        return self.__unit_price 
    def set_unit_price(self,unit_price):
        self.__unit_price = unit_price

    def get_category_id(self):
        return self.__category_id
    def set_category_id(self,categoryid):
        self.__category_id = categoryid

    def get_manufacture_date(self):
        return self._manufacture_date
    def set_manufacture_date(self,manufacturedate):
        if isinstance(manufacturedate,date):
            self._manufacture_date = manufacturedate
        else:
            raise ValueError("manufacture date must be date object")
    def get_is_active(self):
        return self.__is_active
    def set_is_active(self,is_active):
        self.__is_active=is_active

    #override __str__
    def __str__(self):
        return f"productID: {str(self.__product_id):<10},ProductName:{str(self.__productname):<20},categoryID:{str(self.__category_id):<10},UnitPrice:{str(self.__unit_price):<10},manufacturedate:{str(self.__manufacture_date):<15},isActive:{str(self.__is_active):<10} "
    
        
                                  

