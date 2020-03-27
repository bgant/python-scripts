#!/usr/bin/python3

from influxdb import InfluxDBClient

client = InfluxDBClient(host='influxdb.localdomain', port=8086)

client.switch_database('test')

#results = client.query('SELECT "x","y","z" FROM "m1" WHERE "location" = \'laundry\'')
results = client.query('SELECT * FROM "m1"')

print("Default Results:")
print(results)
print()

print("Raw JSON:")
print(results.raw)
print()

print("Loop through Results:")
points = results.get_points(measurement='m1', tags={'location':'laundry'})
for point in points:
    print("Time: %s, Y-Axis: %f" % (point['time'], point['y']))
