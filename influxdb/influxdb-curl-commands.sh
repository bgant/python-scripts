#!/bin/bash
curl -G "http://localhost:8086/query?pretty=true" --data-urlencode "q=SHOW DATABASES"
curl -G "http://localhost:8086/query?pretty=true" --data-urlencode "db=writetest" --data-urlencode "q=SHOW MEASUREMENTS"
curl -G "http://localhost:8086/query?pretty=true" --data-urlencode "db=writetest" --data-urlencode "q=SHOW TAG KEYS"
curl -G "http://localhost:8086/query?pretty=true" --data-urlencode "db=writetest" --data-urlencode "q=SHOW FIELD KEYS"
curl -G "http://localhost:8086/query?pretty=true" --data-urlencode "db=writetest" --data-urlencode "q=SHOW SERIES"
curl -G "http://localhost:8086/query?pretty=true" --data-urlencode "db=writetest" --data-urlencode "q=SHOW TAG VALUES WITH KEY = \"location\""
curl -G "http://localhost:8086/query?pretty=true" --data-urlencode "db=writetest" --data-urlencode "q=SELECT \"z\" FROM \"m1\" WHERE \"location\"='laundry' ORDER BY DESC LIMIT 3"
