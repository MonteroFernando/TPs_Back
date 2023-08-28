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
    @classmethod
    def get_products(self,kwargs):
        if kwargs != {}:
            key=' AND '.join("{}=%s".format(key) for key in kwargs.keys())
            query=f"""SELECT * FROM products 
                      INNER JOIN categories ON products.category_id=categories.category_id
                      INNER JOIN brands ON products.brand_id=brands.brand_id
                      WHERE {key}"""
        else:
            query="""SELECT * FROM products 
                      INNER JOIN categories ON products.category_id=categories.category_id
                      INNER JOIN brands ON products.brand_id=brands.brand_id"""
        params=tuple(kwargs.values())
        response=DatabaseConnector.fetch_all(query,params)
        DatabaseConnector.close_connection()
        if response is not None:
            products=[]
            for prod in response:
                products.append(Product(
                    product_id=prod[0],
                    product_name=prod[1],
                    brand_id=prod[2],
                    category_id=prod[3],
                    model_year=prod[4],
                    list_price=prod[5],
                    brand_name=prod[7],
                    category_name=prod[9]
                    ))
        return products
    @classmethod
    def create_product(self,product):
        query="""INSERT INTO production.products (product_name, brand_id, category_id, model_year, list_price)
                VALUES(%s, %s, %s,%s,%s)"""
        params=(product.product_name, product.brand_id, product.category_id, product.model_year, product.list_price)
        DatabaseConnector.execute_query(query,params)
        DatabaseConnector.close_connection()
        return "Se cargo correctamente el Producto"
    @classmethod
    def update_product(self,product_id,kwargs):
        key=", ".join("{}=%s".format(key) for key in kwargs.keys())
        params=tuple((kwargs.values()))+(product_id,)
        query=f"UPDATE products SET {key} WHERE products.product_id=%s"
        DatabaseConnector.execute_query(query,params)
        DatabaseConnector.close_connection()
        return 'Producto actualizado'
    @classmethod
    def delete_product(self,product_id):
        query="""DELETE FROM products WHERE products.product_id=%s"""
        params=(product_id,)
        DatabaseConnector.execute_query(query,params)
        return 'Se elemino el producto con éxito'
                    


