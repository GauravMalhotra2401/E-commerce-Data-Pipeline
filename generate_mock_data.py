import random
import string

customer_ids = ["CUST00001","CUST00002","CUST00003","CUST00004","CUST00005"]
product_ids = ["PROD00001", "PROD00002", "PROD00003", "PROD00004", "PROD00005"]

payment_types = ["Credit Card", "Debit Card", "Cash on Delivery"]

product_prices = {
    "PROD00001": 799.99,
    "PROD00002": 499.99,
    "PROD00003": 79.99,
    "PROD00004": 19.99,
    "PROD00005": 49.99,
    "PROD00006": 99.99,
    "PROD00007": 149.99,
    "PROD00008": 199.99,
    "PROD00009": 14.99,
    "PROD00010": 19.99,
}

def get_product_price(product_id):

    if product_id in product_ids:
        return product_ids[product_id]
    else:
         return 0.00
    

def generate_mock_data(current_date, number_of_transactions_every_day):

    data = []

    for _ in range(number_of_transactions_every_day):

            transaction_id = f"TXN{''.join(random.choices(string.digits, k=8))}"
            customer_id = random.choice(customer_ids)
            product_id = random.choice(product_ids)
            quantity = random.randint(1,5)
            price = get_product_price(product_id)
            transaction_date = current_date
            payment_type = random.choice(payment_types)
            status = "Completed"

            data.append({
                "transaction_id": transaction_id,
                "customer_id": customer_id,
                "product_id": product_id,
                "quantity": quantity,
                "price": price,
                "transaction_date": transaction_date,
                "payment_type": payment_type,
                "status": status
            })
    return data