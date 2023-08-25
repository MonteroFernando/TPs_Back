from ..models.customer_model import Customer
from flask import Flask
class CustomerController():
    @classmethod
    def create_customer(self):
        pass
        """customer=Customer(
            first_name=request.args.get('first_name',''),
            last_name=request.args.get('last_name',''),
            phone=request.args.get('phone',''),
            email=request.args.get('email',''),
            street=request.args.get('street',''),
            city=request.args.get('city',''),
            satate=request.args.get('state',''),
            zip_code=request.args.get('zip_code','')
            )
        Customer().create_customer(customer)
        return {'message':'Cliente creado con exito'},200"""
    @classmethod
    def get_cusomer(customer_id):
        response=Customer().get_customer(customer_id)
        if response is not None:
            cliente={'customer_id':response.customer_id,
                    'first_name':response.first_name,
                    'last_name':response.last_name,
                    'email':response.email,
                    'phone':response.phone,
                    'street':response.street,
                    'city':response.city,
                    'state':response.state,
                    'zip_code':response.zip_code}
            return cliente,200
        else:
            return {'message':'No se encontro el cliente consultado'},404
        
            