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
		CONN.commit()
	return None

def insert_orders(records):
	for i in range(1, len(records)):
		query = """INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
		DB.execute(query, (records[i][0], records[i][1], records[i][2], 
			records[i][3], records[i][4], records[i][5], records[i][6], 
			records[i][7], records[i][8], records[i][9], records[i][10], 
			records[i][11], records[i][12], records[i][13]))
		print DB.fetchone()
		CONN.commit()

	return None	

def main():
	connect_to_db()
	record_list = process_csv("orders.csv")
	# insert_customers(record_list)
	insert_orders(record_list)


	CONN.close()


if __name__ == "__main__":
	main()