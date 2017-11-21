import pymysql

def connection_mysql(data):
	conn = pymysql.connect(host = data["dbhost"],
			user = data["dbuser"],
			password = data["dbpass"],
			database = data["dbname"],
			port = data["dbport"])
	return conn

def manipulate_mysql(conn,cursor,sql):
	try:
		cursor.execute(sql)
		conn.commit()
		cursor.close()
		return 'OK'
	except conn.Error as err:
		return format(err)

def fetch_mysql(cursor,sql):
    rs = None

    try:
    	cursor.execute(sql)
    	rs = cursor.fetchall()

    except:
    	rs = None
    	# logging("%s: Data Not Found" % (botName), folder_debug, MYMOD)
    	#print "data not found"
    cursor.close()
    return rs


def fetchone(cursor,sql):
    rs = None

    try:
    	cursor.execute(sql)
    	rs = cursor.fetchone()

    except:
    	rs = None
    	# logging("%s: Data Not Found" % (botName), folder_debug, MYMOD)
    	#print "data not found"
    cursor.close()
    return rs