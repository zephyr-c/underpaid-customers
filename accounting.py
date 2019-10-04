melon_cost = 1.00 #sets melon cost as constant. If melon cost changes will only have to update in one place.

def charge_review(filename):
  """ Prints out data for new customers who have underpaid on their melons. Shows line in log file as well as name.

  Takes a file name as an argument and handles the file inside the function, so can be used with any future order log files.
  Splits each line of file into a list based on the '|' character
  Stores items in new list as variables for manipulation
  Calculates expected charge based on number of melons bought and melon cost
  Compares amount expected to what was actually paid, if not match assigns a variable whether under or overpaid
  Prints out line in file where discrepancy occurred and amounts
  Prints new line with customer name and whether they have over or underpaid.
  """
  order_log = open(filename)
  for line in order_log:
        line = line.rstrip()
        line = line.split("|")
        record = line[0]
        name = line[1]
        melons_bought = int(line[2])
        amount_charged = float(line[3])
        expected_amount = float(melons_bought * melon_cost)
        if expected_amount != amount_charged:
            if expected_amount > amount_charged:
              difference = "underpaid"
            elif expected_amount < amount_charged:
              difference = "overpaid"
            print(f"Line {record}: received ${amount_charged}, expected ${expected_amount:.2f}.\n {name} has {difference} for their melons")
  order_log.close()

charge_review("customer-orders.txt")

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
