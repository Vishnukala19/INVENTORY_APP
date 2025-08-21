from datetime import datetime
from dao.ProductDaoimple import ProductDaoImplementation
from dao.AbstractProductDao import ProductDaoService
from models.product import Product



class ProductManagementLib:
    'handles crud logic'
    dao_service: ProductDaoService = ProductDaoImplementation()


    @staticmethod
    def display_all():
        products = ProductManagementLib.dao_service.display_all_products()
        for product in products:
            print(product)
    
    @staticmethod
    def add_product():
        product = Product()
        productname=input("Enter the product name")
        product.set_productname(productname)
        unitprice=float(input("Enter the unit price:"))
        product.set_unit_price(unitprice)
        categoryid=int(input("Enter the categoryid:"))
        product.set_category_id(categoryid)
        m_date=input("Enter Manufacture DAte(dd/mm/yyyy):")
        util_date=datetime.strptime(m_date,"%d/%m/%Y")
        conv_m_date=util_date.date()
        product.set_manufacture_date(conv_m_date)
        product.set_is_active(is_active="Y")

        if ProductManagementLib.dao_service.insert_products(product):
            print("inserted successfully")
        else:
            print("something went wrong")

    @staticmethod
    def update_product():
        searchid = int(input("Enetr the Productid:"))
        products= ProductManagementLib.dao_service.find_by_product_id(searchid)
        if not products:
            print("product not found")
            return
        print(products)
        confirm = input("Do you want to edit this data?(y/n)")
        if confirm.lower()=='y':
            products.set_productname(input("Enter new product name:"))
            products.set_unit_price(float(input("Enter the unit price")))
            if ProductManagementLib.dao_service.update_product(products,searchid):
                print("updated successfully")
            else:
                print("something went wrong")

                
    @staticmethod
    def search_product():
        searchid = int(input("Enter the product id:")) 
        products= ProductManagementLib.dao_service.find_by_product_id(searchid)
        if not products:
            print("product not found")
        else:
            print(products)   



    @staticmethod
    def disable_product():
        searchid = int(input("Enter the product id:")) 
        products= ProductManagementLib.dao_service.find_by_product_id(searchid)
        if not products:
            print("Product not found")
        confirm = input("Do yo want to diable the data?(y/n)")
        if confirm.lower()=='y':
            
            if ProductManagementLib.dao_service.disable_product(searchid):
                print("Disabled successfully")
            else:
                print("Error in disabling..")                  

    @staticmethod
    def apply_gst_to_product():
        productid=int(input("Enter the productid to apply gst"))
        gst_percent=int(input("Enter GST Percentage to apply"))
        if ProductManagementLib.dao_service.apply_gst(productid,gst_percent):
            print(f"GST of {gst_percent}% applied successfully to product ID {productid}")
        else:
            print("failed to apply GST")







        

