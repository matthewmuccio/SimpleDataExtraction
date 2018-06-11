#!/usr/bin/env python3


import json # Standard library import

import requests # Third-party module import


def get_price(ticker_symbol):
	endpoint = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=" + ticker_symbol
	response = json.loads(requests.get(endpoint).text)
	last_price = response["LastPrice"]
	return last_price


if __name__ == "__main__":
	print(get_price("tsla"))
