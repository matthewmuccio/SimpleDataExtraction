#!/usr/bin/env python3


import sqlite3 # Standard library import


def record_price(ticker_symbol, last_price):
	connection = sqlite3.connect("master.db", check_same_thread=False)
	cursor = connection.cursor()
	cursor.execute("INSERT INTO {0}(last_price) VALUES({1});".format(ticker_symbol, last_price))
	connection.commit()
	cursor.close()
	connection.close()
	return True


if __name__ == "__main__":
	record_price("tsla", 317.66)
