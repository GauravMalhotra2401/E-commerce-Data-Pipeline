import random

def generate_mock_data(current_date, file_name, number_of_transactions_every_day):

    data = []
    used_transaction_ids = set()

    for _ in range(number_of_transactions_every_day):
        while True:  # Keep generating IDs until a unique one is found
            transaction_id = f"TXN{random.randint(100000000, 999999999)}"
            if transaction_id not in used_transaction_ids:
                used_transaction_ids.add(transaction_id)
                break

        data.append({
            "transaction_id":transaction_id,
            "customer_id":f"C{random.randint(10000,99999)}",
            "product_id":f"P{random.randint(10000,99999)}",
            "quantity":random.randint(1,100),
            "price":round(random.uniform(1,100),2),
            "transaction_date":current_date,
            "payment_type":random.choice(['Credit Card', 'Debit Card', 'Digital Wallets', 'Cash', 'Bank Transfers']),
            "status":random.choice(['Pending', 'Completed', 'Failed', 'Cancelled', 'Refunded'])
        })

    return data