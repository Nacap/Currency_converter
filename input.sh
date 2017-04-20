#!/bin/bash

echo "Starting import"
python step_1.py
echo "Python data fetched"
mysqlimport -umonty -h127.0.0.1 -P22222 -pwinter  --ignore-lines=1 --fields-terminated-by=',' --fields-enclosed-by='"' --lines-terminated-by='\n' --local naca currency_converter.csv
echo "Import done"

