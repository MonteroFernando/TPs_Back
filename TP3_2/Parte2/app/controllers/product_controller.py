from flask import request
from ..models.product_models import Product

class ProductController:
    @classmethod
    def get_product(self,product_id):
        product=Product().get_product(product_id)
        response=self.class_to_dict(product)
        return response,200
    @classmethod
    def get_products(self):
        kwargs=self.args_to_dict()
        products=Product().get_products(kwargs)
        if len(products) >1:
            list_products=[self.class_to_dict(prod) for prod in products]
            return {'products':list_products,'total':len(list_products)},200
    @classmethod
    def create_product(self):
        product_name=request.args.get('product_name','')
        brand_id=request.args.get('brand_id','')
        category_id=request.args.get('category_id','')
        model_year=request.args.get('model_year','')
        list_price=request.args.get('list_price','')
        product=Product(
            product_name=product_name,
            brand_id=brand_id,
            category_id=category_id,
            model_year=model_year,
            list_price=list_price
            )
        Product().create_product(product)
        return { },201
    @classmethod
    def update_product(self,product_id):
        kwargs=self.args_to_dict()
        Product.update_product(product_id,kwargs)
        return { }, 200
    @classmethod
    def delete_product(self,product_id):
        Product().delete_product(product_id)
        return { },200

    @staticmethod
    def class_to_dict(product):
        """Metodo que prepara en diccionario los datos devueltos en la clase Product"""
        response={'brands':{'brand_id':product.brand_id,'brand_name':product.brand_name},
                  'category':{'category_id':product.category_id,'category_name':product.category_name},
                  'list_price':product.list_price,
                  'model_year':product.model_year,
                  'product_id':product.product_id,
                  'product_name':product.product_name}  
        return response
    @staticmethod 
    def args_to_dict():
        kwargs={
            'products.brand_id':request.args.get('brand_id',''),
            'products.category_id':request.args.get('category_id',''),
            #agrego estos datos solo para el caso de update
            'products.product_name':request.args.get('product_name'),
            'products.model_year':request.args.get('model_year',''),
            'products.list_price':request.args.get('list_price','')

        }
        kwargs={key:value for key,value in kwargs.items() if value != ''}
        return kwargs