import sqlanydb

#conn = sqlanydb.connect(dsn='SYBASE_IQ')
conn = sqlanydb.connect(dsn='dwhdb_eniq')
curs = conn.cursor()
curs.execute("select 'Hello, world!'")
print( "SQL Anywhere says: %s" % curs.fetchone())
curs.close()
conn.close()