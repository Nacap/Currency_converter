 mysqlimport \
 	-umonty 
 	-h127.0.0.1 \
 	-P22222 -pwinter  \
 	--ignore-lines=1 \
 	--fields-terminated-by=',' \
 	--fields-enclosed-by='"' \
 	--lines-terminated-by='\n' \
 	--local naca currency_converter.csv

 # where naca is database name
 # name of csv file must match the table name in db naca
