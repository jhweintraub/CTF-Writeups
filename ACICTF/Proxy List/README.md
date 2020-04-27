Simple Challenge, the hardest part is just finding the write IP Lookup module in python. I ended up using GeoIP. I downloaded the database to use cause
the online API wasn't working and was much faster to do offline.

Just take the script and pass each line into a lookup function and then append the country code to an array
Then just use collections to find the Mode of the array

Flag - "Brazil"