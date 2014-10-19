import sqlite3

DB = None
CONN = None

def connect_to_db(db_name):
	global DB, CONN
	CONN = sqlite3.connect(db_name)
	DB = CONN.cursor()

def process_csv(filename):
	f = open(filename)
	records = []

	for line in f:
		line_values = line.strip().split(",")
		records.append(line_values)

	return records

# def insert_customers(records):
# 	for item in records:
# 		QUERY = """INSERT INTO customers (customer_id, first, last, email, telephone, called) VALUES ?, ?, ?, ?, ?, ?"""
# 		(table, )


def main():
	# connect_to_db("melons.db")
	process_csv("customers.csv")


if __name__ == "__main__":
	main()