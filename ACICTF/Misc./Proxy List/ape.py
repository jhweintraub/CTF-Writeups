#!/usr/bin/env python3

import geoip2.database
from collections import Counter


reader = geoip2.database.Reader('./database.mmdb')

file = open('ips.txt', 'r')
countries = []
for line in file:
	try:
		response = reader.country(line[:-1])
		countries.append(response.country.name)
		# print(response.country.name)
	except:
		continue
data = Counter(countries)
print(data.most_common())