#!/usr/bin/env python3


import sqlite3


def create_table(ticker_symbol):
	connection = sqlite3.connect("master.db", check_same_thread=False)
	cursor = connection.cursor()
	cursor.execute("CREATE TABLE {0}(pk INTEGER PRIMARY KEY AUTOINCREMENT, last_price FLOAT);".format(ticker_symbol))
	cursor.close()
	connection.close()
	return True


if __name__ == "__main__":
	create_table("nke")
