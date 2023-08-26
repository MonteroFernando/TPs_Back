from ..models.customer_model import Customer
from flask import request
class CustomerController():
    @classmethod
    def create_customer(self):
        first_name=request.args.get('first_name','')
        last_name=request.args.get('last_name','')
        email=request.args.get('email','')
        if first_name=='' or last_name=='' or email=='':
            return {'error':'Faltan algunos de los campos obligatorios'},400
        else:
            customer=Customer(
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
            return { },201
    @classmethod
    def get_customer(self,customer_id):
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
    @classmethod
    def get_customers(slef):
        response=Customer().get_customers()
        customers=[]
        if response is not None:
            for customer in response:
                cliente={'customer_id':customer.customer_id,
                    'first_name':customer.first_name,
                    'last_name':customer.last_name,
                    'email':customer.email,
                    'phone':customer.phone,
                    'street':customer.street,
                    'city':customer.city,
                    'state':customer.state,
                    'zip_code':customer.zip_code}
                customers.append(cliente)
            return {'customers':customers,
                    'total':len(customers)},200
        else:
            return {'customers':customers,
                    'total':0},200
    @classmethod
    def update_customer(self,customer_id):
        kwargs={}
        kwargs['fist_name']=request.args.get('fist_name','')
        kwargs['last_name']=request.args.get('last_name','')
        kwargs['phone']=request.args.get('phone','')
        kwargs['email']=request.args.get('email','')
        kwargs['street']=request.args.get('street','')
        kwargs['city']=request.args.get('city','')
        kwargs['state']=request.args.get('state','')
        kwargs['last_name']=request.args.get('last_name','')

        #Filtro los valores del diccionario dejando solo los que tengan datos
        kwargs={key:val for key,val in kwargs.items() if val !=""}
        
        estado=Customer().update_customer(customer_id,kwargs)
        if estado is not None:
            return{ },200
        else:
            return {'message':'No se encontro el cliente'},404
        

           
        

        
            