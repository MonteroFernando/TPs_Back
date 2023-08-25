from ..database import DatabaseConnector

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
    def create_customer(self,customer):
        query="""INSERT INTO sales.customers(first_name,last_name,phone,email,street,city,state,zip_code)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        params=(customer.first_name, customer.last_name, customer.phone, customer.email, customer.street,
                customer.city, customer.state, customer.zip_code)
        DatabaseConnector.execute_query(query,params)
    @classmethod
    def get_customer(self,customer_id):
        query="""SELECT * FROM customers WHERE customer_id=%s;"""
        params=(customer_id,)
        result=DatabaseConnector.fech_one(query,params)

        if result is not None:
            return Customer(
                customer_id=customer_id,
                first_name=result[1],
                last_name=result[2],
                phone=result[3],
                email=result[4],
                street=[5],
                city=[6],
                satate=[7],
                zip_code=[8]
            )
        else:
            return None
    @classmethod
    def get_customers(self):
        query="""SELECT * FROM customers"""
        result=DatabaseConnector.fechall(query)
        if result is not None:
            customers=[]
            for customer in result:
                customers.append(Customer(
                customer_id=customer[0],
                first_name=customer[1],
                last_name=customer[2],
                email=customer[4],
                street=customer[5],
                city=customer[6],
                satate=customer[7],
                zip_code=customer[8]
            ))
        else:
            return None
        return customers
    @classmethod
    def update_customer(self,customer_id,**kwargs):
        """Metodo que modifica del customer pasado como parametro, los datos que se espcifican en el keyword 
        argument, modificando solo los valores que se ingresan"""
        #forma pythonica que toma cada una de las key de los argumentos haciendo key=%s, de esta manera
        #los que no se pasan como parametros, no se modifican. 
        set_values=", ".join([f"{key}=%s" for key in kwargs.keys()])
        #creacin del query agregando set_value como string que antes se unio con .join
        query=f"UPDATE customers SET {set_values} WHERE customer_id = %s;"
        #creacion de los parametros, tomando los valores del keyword arguments y agregando el id al final
        params=list(kwargs.values()) + [customer_id]
        DatabaseConnector.execute_query(query,params)

    
    
    
    