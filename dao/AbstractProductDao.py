from abc import ABC, abstractmethod
from typing import List
from models.product import Product


class ProductDaoService(ABC):
    @abstractmethod
    def display_all_products(self) -> List[Product]:
        """Fetch all products"""
        pass

    @abstractmethod
    def insert_products(self, product: Product) -> bool:
        """Insert a product into the database"""
        pass

    @abstractmethod
    def find_by_product_id(self,product_id:int)->Product:
        '''find a product by ID'''
        pass
    @abstractmethod
    def update_product(self,product:Product,product_id:int)->bool:
        '''update product in db'''
        pass

    @abstractmethod
    def disable_product(self,product_id:int)->Product:
        '''disable product in db'''
        pass
    @abstractmethod
    def apply_gst(self,product_id:int,gst_percent:float)->bool:
        '''compute the gst of the product'''
        pass
