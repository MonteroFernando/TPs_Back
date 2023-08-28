from ..database import DatabaseConnector

class Product:
    def __init__(self,product_id=None,product_name=None,brand_id=None,category_id=None,model_year=None,
                    list_price=None,brand_name=None,category_name=None):
        self.product_id=product_id
        self.product_name=product_name
        self.brand_id=brand_id
        self.category_id=category_id
        self.model_year=model_year
        self.list_price=list_price
        self.brand_name=brand_name
        self.category_name=category_name
    @classmethod    
    def get_product(self,product_id):
        query="""SELECT * FROM products
                 INNER JOIN brands ON products.brand_id = brands.brand_id 
                 INNER JOIN categories ON products.category_id=categories.category_id
                 WHERE products.product_id=%s"""
        params=(product_id,)
        response=DatabaseConnector.fech_one(query,params)
        DatabaseConnector.close_connection()
        if response is not None:
            return Product(
                product_id=product_id,
                product_name=response[1],
                brand_id=response[2],
                category_id=response[3],
                model_year=response[4],
                list_price=response[5],
                brand_name=response[7],
                category_name=response[9]
            )

