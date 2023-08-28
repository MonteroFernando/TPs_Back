from flask import request
from ..models.product_models import Product

class ProductController:
    @classmethod
    def get_product(self,product_id):
        product=Product().get_product(product_id)
        response={'brands':{'brand_id':product.brand_id,'brand_name':product.brand_name},
                  'category':{'category_id':product.category_id,'category_name':product.category_name},
                  'list_price':product.list_price,
                  'model_year':product.model_year,
                  'product_id':product.product_id,
                  'product_name':product.product_name}
        return response,200

