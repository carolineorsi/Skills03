import sqlite3

DB = None
CONN = None

def connect_to_db(db_name):
	global DB, CONN
	CONN = sqlite3.connect(db_name)
	DB = CONN.cursor()
	return None

def process_csv(filename):
	f = open(filename)
	records = []

	for line in f:
		line_values = line.strip().split(",")
		records.append(line_values)

	return records

def insert_customers(records):
	for item in records:
		query = """INSERT INTO customers (customer_id, first, last, email, telephone, called) VALUES ?, ?, ?, ?, ?, ?"""
		db.execute(query, (item[0], item[1], item[2], item[3], item[4], item[5]))
		return None


def main():
	connect_to_db("melons.db")
	process_csv("customers.csv")

	CONN.close()


if __name__ == "__main__":
	main()