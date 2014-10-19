import sqlite3

DB = None
CONN = None

def connect_to_db():
	global DB, CONN
	CONN = sqlite3.connect("melons.db")
	DB = CONN.cursor()

def process_csv(filename):
	f = open(filename)
	records = []

	for line in f:
		line_values = line.strip().split(",")
		records.append(line_values)

	return records

def insert_customers(records):
	for i in range(1, len(records)):
		query = """INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)"""
		DB.execute(query, (records[i][0], records[i][1], records[i][2], records[i][3], records[i][4], records[i][5]))
	return None

def check_records():
	query = """SELECT * FROM customers"""
	DB.execute(query, )
	print DB.fetchall()
	return None

def main():
	connect_to_db()
	record_list = process_csv("customers.csv")
	insert_customers(record_list)

	check_records()

	CONN.close()


if __name__ == "__main__":
	main()