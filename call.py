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
	query = """ SELECT customer_id, first, last, telephone FROM customer_orders WHERE called = '' AND watermelons >= 20 """
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
	date = time.strftime('%m/%d/%Y')
	query = """ UPDATE customers SET called = ? WHERE customer_id = ? """
	DB.execute(query, (date, row[0]))
	CONN.commit()


def main():
	connect_to_db("melons.db")
	customer = get_next_customer()
	display_customer(customer)
	update_records(customer)

if __name__ == '__main__':
	main()