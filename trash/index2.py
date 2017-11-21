


from pprint import pprint
import os
import requests
#from mysql.connector import connect, Error
from bs4 import BeautifulSoup

basef = 'C:/Projects/python/crawla'


def get_map():
    url = 'http://parts.isuzu.astra.co.id/marketing/catalog/illustration.php?grpfig=10&vehicle=n-series&type=NMR71'
    #url = 'http://parts.isuzu.astra.co.id/marketing/catalog/illustration.php?grpfig=FI&vehicle=n-series&type=NMR71'
    r = requests.get(url)

    content = r.text
    sosoup = BeautifulSoup(content, 'html.parser')
    table = sosoup.find_all('table')

    main_table = table[0]

    table_body = main_table.find('tbody')
    #rows = table_body.find_all('tr')

    pprint(table_body is None)


def main():

    map = get_map()
    logFileO = open('pprint/abc.log', 'w')
    pprint(map, logFileO)
    #cleansing(map)

main()


