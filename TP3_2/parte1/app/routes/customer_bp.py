from flask import Blueprint
from ..controllers.customer_controller import CustomerController

customer_bp = Blueprint('customer_bp', __name__)

customer_bp.route('/customers/<int:customer_id>', methods=['GET'])(CustomerController.get_cusomer)

