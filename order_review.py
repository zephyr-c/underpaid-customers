order_log = open("customer-orders.txt")

melon_price = 1.00

def charge_review(order_log):
    
    for line in order_log:
        line = line.rstrip()
        line = line.split("|")
        record = line[0]
        name = line[1]
        melons_bought = int(line[2])
        amount_charged = float(line[3])
        expected_amount = float(melons_bought * melon_price)
        if expected_amount != amount_charged:
            print(f"Line {record} {name} paid ${amount_charged}, expected ${expected_amount:.2f}")

charge_review(order_log)

order_log.close()