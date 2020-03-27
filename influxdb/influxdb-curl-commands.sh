#!/bin/bash
HOST='influxdb.localdomain'
DB='test'
curl -G "http://$HOST:8086/query?pretty=true" --data-urlencode "q=SHOW DATABASES"
curl -G "http://$HOST:8086/query?pretty=true" --data-urlencode "db=$DB" --data-urlencode "q=SHOW MEASUREMENTS"
curl -G "http://$HOST:8086/query?pretty=true" --data-urlencode "db=$DB" --data-urlencode "q=SHOW TAG KEYS"
curl -G "http://$HOST:8086/query?pretty=true" --data-urlencode "db=$DB" --data-urlencode "q=SHOW FIELD KEYS"
curl -G "http://$HOST:8086/query?pretty=true" --data-urlencode "db=$DB" --data-urlencode "q=SHOW SERIES"
curl -G "http://$HOST:8086/query?pretty=true" --data-urlencode "db=$DB" --data-urlencode "q=SHOW TAG VALUES WITH KEY = \"location\""
curl -G "http://$HOST:8086/query?pretty=true" --data-urlencode "db=$DB" --data-urlencode "q=SELECT \"z\" FROM \"m1\" WHERE \"location\"='laundry' ORDER BY DESC LIMIT 3"
