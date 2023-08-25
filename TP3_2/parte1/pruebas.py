from app.models.customers import Customer

customers=Customer().get_customers()
print(len(customers))
for customer in customers:
    dic={'customer_id':customer.customer_id,
         'firstname':customer.first_name}
    print(dic)



