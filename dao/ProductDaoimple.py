from typing import List

import pymysql
from dao.AbstractProductDao import ProductDaoService
from db.db_connection import DBConnection
from models.product import Product


class ProductDaoImplementation(ProductDaoService):
    'implementation for abstract class ProductDaoService'
    #SQL queries
    DISPLAY_ALL = "SELECT * FROM PRODUCTS"
    INSERT_PRODUCT = " INSERT INTO products(productname,unit_price,categoryid,manufacturedate,isActive) VALUES (%s ,%s ,%s ,%s ,%s)"
    FIND_BY_ID = "SELECT * from products WHERE productid=%s"
    UPDATE_PRODUCT = "UPDATE products set productname=%s, unit_price=%s WHERE productid=%s"
    DISABLE_PRODUCT=" UPDATE products SET isActive='N' where productid=%s"
    APPLY_GST = "CALL apply_gst_to_product(%s,%s)"
    def __init__(self):
        self.conn = DBConnection().get_connection()
        
    def insert_products(self,product:Product)->bool:
        try:
            cursor = self.conn.cursor() #create a cursor object
            cursor.execute(self.INSERT_PRODUCT, (
                                    product.get_productname(),
                                    product.get_unit_price(),
                                    product.get_category_id(),
                                    product.get_manufacture_date(),
                                    product.get_is_active()
                                    ))

            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting product:",e)
            return False
        finally:
            cursor.close()
    def display_all_products(self)->List[Product]:
        products=[]
        cursor = None
        try:
            cursor= self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(self.DISPLAY_ALL)
            rows = cursor.fetchall()
            for row in rows:
                products.append(Product(product_id=row["productid"],
                                        productname=row["productname"],
                                        unit_price=row["unit_price"],
                                        category_id=row["categoryid"],
                                        manufacture_date=row["manufacturedate"],
                                        is_active=row["isActive"]))       
        except Exception as e:
            print("Error fetching products:",e)
        finally:
            if cursor:
               cursor.close()
        return products
    
    def find_by_product_id(self,productid:int):
        products = None
        cursor = None
        try:
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(self.FIND_BY_ID,(productid,))
            row = cursor.fetchone()
            if row:
               products = Product(
                    product_id=row["productid"],
                    productname=row["productname"],
                    unit_price=row["unit_price"],
                    category_id=row["categoryid"],
                    manufacture_date=row["manufacturedate"],
                    is_active=row["isActive"])
        except Exception as e:
            print("Error fetching products:",e)
        finally:
            if cursor:
               cursor.close()
        return products  

    def update_product(self, products:Product, product_id:int)->bool:
        try:
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(self.UPDATE_PRODUCT,
                          (products.get_productname(),
                           products.get_unit_price(),
                           product_id))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error updating product",e)
        finally:
            if cursor:
               cursor.close()
        return products
    
    def disable_product(self, productid:int)->bool:
        products = None
        cursor = None
        try:
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(self.DISABLE_PRODUCT,(productid,))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print(f"error in diable product:{e}")
        finally:
            if cursor:
                cursor.close()

    def apply_gst(self, productid:int, gst_percent:float)->bool:
        cursor= None
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.APPLY_GST,(productid,gst_percent))
            self.conn.commit()
            return cursor.rowcount >=0 #since sp returns 0 if already applied
        except Exception as e:
            print("Error Applying GST:",e)
            return False
        finally:
            if cursor:
                cursor.close()




                     
                 

               


            

