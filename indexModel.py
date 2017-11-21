import re
from os.path import exists
import sys
from sys import exit, argv

paths = 'C:\Projects\python\crawla'
sys.path.append(paths)

from mysql_conn import *

db_1   = {
		'dbhost' : 'localhost',
		'dbuser' : 'root',
		'dbpass' : '',
		'dbname' : 'spareparts',
		'dbport' : 3306
	}
conn   = connection_mysql(db_1)


def insertCarModel(nameCar):
    cursor = conn.cursor()
    sql = """  INSERT INTO cars
                 (id,name)
                 VALUES(NULL ,'%s')
                 """ % (nameCar)

    result = manipulate_mysql(conn, cursor, sql)
    return result


def getCar(name):
    cursor = conn.cursor()
    sql = """
        SELECT id
        FROM cars
        where name = '%s'
        """ % (name)

    result = fetch_mysql(cursor, sql)
    return result


def getCategory(car_id,name):
    cursor = conn.cursor()
    sql = """
        SELECT id, name
        FROM categories
        where car_id = %i and name = '%s'
        """ % (car_id,name)

    result = fetch_mysql(cursor, sql)
    return result


def insertCategory(data):
    cursor = conn.cursor()
    sql = """  INSERT INTO categories
                 (id,car_id,name,no_fig,url)
                 VALUES(NULL , %i ,'%s','%s','%s')
                 """ % (data['car_id'],data['name'],data['no_fig'],data['url'])

    result = manipulate_mysql(conn, cursor, sql)
    return result

def insertComponent(data):
    cursor = conn.cursor()
    sql = """  INSERT INTO component
                 (id,category_id,description,model,qty,part_no)
                 VALUES(NULL , %i,'%s','%s','%s' ,'%s' )
                 """ % (data['category_id'],data['description'],data['model'],data['qty'],data['part_no'])

    result = manipulate_mysql(conn, cursor, sql)
    return result

def insertImg(data):
    cursor = conn.cursor()
    sql = """  INSERT INTO category_images
                    (id,category_id,url_file)
                    VALUES(NULL , %i,'%s')
                    """ % (data['category_id'], data['url_file'])

    result = manipulate_mysql(conn, cursor, sql)
    return result
