#!/usr/bin/python3

from influxdb import InfluxDBClient
import random

# Connect to InfluxDB HTTP/HTTPS service:
client = InfluxDBClient(host='influxdb.localdomain', port=8086)
#client = InfluxDBClient(host='127.0.0.1', port=8086, username='admin', password='password', ssl=False, verify_ssl=False)
#client = InfluxDBClient(host='127.0.0.1', port=9999, username='admin', password='password', ssl=True, verify_ssl=True)

# Create database:
db_name= 'test'
db_list = client.get_list_database()
if {'name': db_name} not in db_list:
    print('creating', db_name)
    client.create_database(db_name)

# Measurement Name and Tags:
measurement_name = 'm1'
location = 'laundry'
clientid = '123456789'

# List of Line Data to add to database (timestamp added by influxdb):
data = []
data.append("{measurement},clientid={clientid},location={location} x={x},y={y},z={z}"
            .format(measurement=measurement_name,
                    clientid=clientid,
                    location=location,
                    x=round(random.random(),4),
                    y=round(random.random(),4),
                    z=random.randint(0,50)))

# Write data list to influxdb:
print(data)
client.write_points(data, database=db_name, time_precision='ms', protocol='line')

