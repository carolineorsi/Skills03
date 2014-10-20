"""
call.py - Telemarketing script that displays the next name 
          and phone number of a Customer to call.

          This script is used to drive promotions for 
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

import time
import sqlite3

DB = None
CONN = None

def connect_to_db(db_name):
	global DB, CONN
	CONN = sqlite3.connect(db_name)
	DB = CONN.cursor()

def get_next_customer():
	query = """ SELECT customer_id, first, last, telephone FROM customers WHERE called = '' """
	DB.execute(query, )
	row = DB.fetchone()
	return row

def display_customer(row):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print "Name: ", row[1], row[2]
	print "Phone: ", row[3]
	print "\n"

def update_records(row):
	date = "10/19/14"
	query = """ UPDATE customers SET called = ? WHERE customer_id = ? """
	DB.execute(query, (date, row[0]))
	CONN.commit()

# def update_customer_file(filename, customer_id):
# 	lines = open(filename, 'r').readlines()

# 	for i in range(len(lines)):
# 		if lines[i].startswith(customer_id):
# 			lines[i] = lines[i][0:-1] + time.strftime('%m/%d/%Y') + '\n'

# 	out = open(filename, 'w')
# 	out.writelines(lines)

	# out.close()

def main():
	connect_to_db("melons.db")
	customer = get_next_customer()
	display_customer(customer)
	update_records(customer)

	# # Load data from our csv files
	# customers = load_customers('customers.csv')
	# orders    = load_orders('orders.csv')

	# # Loop through each order
	# for order in orders:
	# 	# Is this order over 20 watermelon?
	# 	if order.get('num_watermelons', 0) > 20:
	# 		# Has this customer not been contacted yet?
	# 		customer = customers.get(order.get('customer_id', 0), 0)
	# 		if customer.get('called', '') == '':
	# 			display_customer(customer)
	# 			update_customer_file('customers.csv', customer['customer_id'])
	# 			break

if __name__ == '__main__':
	main()