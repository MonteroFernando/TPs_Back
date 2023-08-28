from flask import Blueprint
from ..controllers.product_controller import ProductController

product_bp=Blueprint('product_bp',__name__)

product_bp.route('/products/<int:product_id>',methods=['GET'])(ProductController.get_product)

