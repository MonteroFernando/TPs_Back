from app.models.customers import Customer

customers=Customer().get_customers()
"""print(len(customers))
for customer in customers:
    dic={'customer_id':customer.customer_id,
         'first_name':customer.first_name,
         'last_name':customer.last_name}
    
    print(dic)"""

Customer().update_customer(1445,first_name="Ester", city="San Lorenzo")


