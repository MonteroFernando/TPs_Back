from ..database import DatabaseConnector

class Customer():
    def __init__(self,customer_id=None,first_name=None,last_name=None,phone=None,email=None,street=None,
                 city=None,state=None,zip_code=None):
        """Metodo constructor"""
        self.customer_id=customer_id
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.street=street
        self.city=city
        self.state=state
        self.zip_code=zip_code
    @classmethod
    def create_customer(self,customer):
        """Metodo de Clase que ingresa los datos de un cliente"""
        query="""INSERT INTO sales.customers(first_name,last_name,phone,email,street,city,state,zip_code)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        params=(customer.first_name, customer.last_name, customer.phone, customer.email, customer.street,
                customer.city, customer.state, customer.zip_code)
        DatabaseConnector.execute_query(query,params)
        DatabaseConnector.close_connection()
    @classmethod
    def get_customer(seld,customer_id):
        """Metodo de clase que retorna los datos del id customer recibido como parametro,
        devulelve un objeto customer"""
        query="""SELECT * FROM customers WHERE customer_id=%s;"""
        params=(customer_id,)
        result=DatabaseConnector.fech_one(query,params)
        DatabaseConnector.close_connection()
        if result is not None:
            return Customer(
                customer_id=customer_id,
                first_name=result[1],
                last_name=result[2],
                phone=result[3],
                email=result[4],
                street=result[5],
                city=result[6],
                state=result[7],
                zip_code=result[8]
            )
        else:
            return None
    @classmethod
    def get_customers(self,kwargs):
        """Metodo que retorna una lista de customers"""
        if kwargs == {}:
            query="""SELECT * FROM customers"""
            result=DatabaseConnector.fechall(query)
        else:
            #Creacion de un string usando las key de los parametros recibidos con el formato key1=%s, key2=%s,..
            if len(kwargs) > 1:
                keys=" AND ".join("{}=%s".format(key) for key in kwargs.keys())
            else:
                keys=", ".join("{}=%s".format(key) for key in kwargs.keys())
            params=tuple(kwargs.values())
            query=f"SELECT * FROM customers WHERE {keys}"""
            result=DatabaseConnector.fechall(query,params)
        DatabaseConnector.close_connection()
        if result is not None:
            customers=[]
            for customer in result:
                customers.append(Customer(
                customer_id=customer[0],
                first_name=customer[1],
                last_name=customer[2],
                phone=customer[3],
                email=customer[4],
                street=customer[5],
                city=customer[6],
                state=customer[7],
                zip_code=customer[8]
            ))
        else:
            return None
        return customers
    @classmethod
    def update_customer(self,customer_id,kwargs):
        """Parametro que actulaiza el customer del id recibido como parametro, con las actualizaciones
        recibidas de kwargs como un diccionario, con las key del nombre de la columna a modificar"""
        cliente=self.get_customer(customer_id)
        if cliente is not None:
            #Creacion de un string usando las key de los parametros recibidos con el formato key1=%s, key2=%s,..
            keys=", ".join("{}=%s".format(key) for key in kwargs.keys())
            params=tuple(kwargs.values())+(customer_id,)
            query=f"UPDATE customers SET {keys} WHERE customers.customer_id=%s"
            DatabaseConnector.execute_query(query,params)
            DatabaseConnector.close_connection()
            return "Cliente actualizado"
        else:
            
            return None
    @classmethod
    def delete_customer(self,customer_id):
        """metodo que elimina el customer con el id pasado como parametro"""
        query= "DELETE FROM customers WHERE customer_id = %s"
        params=(customer_id,)
        cliente=self.get_customer(customer_id)
        if cliente is not None:
            DatabaseConnector.execute_query(query,params)
            DatabaseConnector.close_connection()
            return None
        else:
            return 'No existe el cliente solicitado'
        



