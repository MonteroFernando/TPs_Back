from flask import Blueprint
from ..controllers.customer_controller import CustomerController

customer_bp = Blueprint('customer_bp', __name__)
#Ejercicio 1.1
customer_bp.route('/customers/<int:customer_id>', methods=['GET'])(CustomerController.get_customer)
#Ejercicio 1.2
customer_bp.route('/customers', methods=['GET'])(CustomerController.get_customers)
#Ejercicio 1.3
customer_bp.route('/customer', methods=['POST'])(CustomerController.create_customer)
#Ejercicio 1.4
customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])(CustomerController.update_customer)
#Ejercicio 1.5
customer_bp.route('/customers/<int:customer_id>',methods=['DELETE'])(CustomerController.delete_customer)


