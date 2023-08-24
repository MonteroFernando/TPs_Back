from database import DatabaseConnector

class Customer():
    def __init__(self,customer_id=None,first_name=None,last_name=None,phone=None,email=None,street=None,
                 city=None,satate=None,zip_code=None):
        self.customer_id=customer_id
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.street=street
        self.city=city
        self.state=satate
        self.zip_code=zip_code
    @classmethod
    def get_customer(customer):
        query="""SELECT * FROM customers WHERE customers_id=%s;"""
        params=(customer.customer_id)
        result=DatabaseConnector.get_connection(query,params)
        if result is not None:
            return Customer(
                customer_id=customer.customer_id

            )#falta terminar de generar

