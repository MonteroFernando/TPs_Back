from flask import Blueprint
from ..controllers.product_controller import ProductController

product_bp=Blueprint('product_bp',__name__)

#EJERCICIO 2.1
product_bp.route('/products/<int:product_id>',methods=['GET'])(ProductController.get_product)
#EJERCICIO 2.2
product_bp.route('/products',methods=['GET'])(ProductController.get_products)
#EJERCICIO 2.3
product_bp.route('/product',methods=['POST'])(ProductController.create_product)
#EJERCICIO 2.4
product_bp.route('/products/<int:product_id>',methods=['PUT'])(ProductController.update_product)
#EJERCICIO 2.5
product_bp.route('/products/<int:product_id>',methods=['DELETE'])(ProductController.delete_product)






