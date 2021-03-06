#import os
#os.environ["LD_LIBRARY_PATH"] = "C:\oracle\ora11\lib"

#print(os.environ["ORACLE_HOME"])
#os.environ["ORACLE_HOME"] = "C:\oracle\ora11"

import cx_Oracle


ip = '10.136.12.164'
port = 1521
SID = 'RAN'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
print (dsn_tns)
con = cx_Oracle.connect('CC', 'CC', dsn_tns)

#con = cx_Oracle.connect('CC/CC@10.136.12.164/RAN')
#con = cx_Oracle.connect("CC", "CC", "Violet")


connstr = 'CC/CC@10.136.12.164:1521/RAN'
con = cx_Oracle.connect(connstr)

cur = con.cursor()
cur.execute('SELECT ID, NAME, CODE, CODE2 FROM CC.DIC_VENDORS')


#
# test 1
#
# for result in cur:
#     print(result)
# cur.close()
# con.close()


# test 2

row = cur.fetchone()
while row:
    print("ID=%d, NAME=%s" % (row[0], row[1]))
    row = cur.fetchone()
con.close()