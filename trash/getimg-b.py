


from pprint import pprint
import os
import requests
#from mysql.connector import connect, Error
from bs4 import BeautifulSoup
import json
basef = 'C:/Projects/python/crawla'

import re


def main():

    aoish = 'http://parts.isuzu.astra.co.id/marketing/catalog/detail.php?fig=6-03&vehicle=d-max2016&type=D-MAX2016'


    r = requests.get(aoish)
    content = r.text
    sosoup = BeautifulSoup(content, 'html.parser')
    ambilVar = sosoup.find_all('script')[2]

    vah5 = ambilVar.string.split("fadeSlideShow(",1)[-1]#.rsplit('{', 1)[0]
    #data = "var alskd =  %s "%(vah5)
    # data = json.loads(data)
    data = vah5
    asif = data.replace('\r\n',' ')
    asif = asif.replace('\t',' ')
    asif = asif.replace(')','')
    sfhasvba = asif.split("imagearray",1)[1]
    # autlg = sfhasvba.split("displaymode",1)[0]
    # jfykf = autlg.split("type:{",1)
    # coais = "{ %s }"%(jfykf)
    #
    # asif = coais.replace('[','')
    # asif = asif.replace('[','')
    # asif = asif.replace(':','')
    # asif = asif.replace('\'','')
    asif = asif.split(',')
    #lasidyan = json.loads(lasidyan)
    for j in asif:
       if "print" in j:
          pprint(j)

    # k = "http://dcsd.nutrislice.com/menu/meadow-view/lunch/"
    #
    # r = requests.get(k)
    # content = r.text
    #
    # soup = BeautifulSoup(content, 'html.parser')
    # script = soup.findAll('script')[0].string
    # data = script.split("bootstrapData['menuMonthWeeks'] = ", 1)[-1].rsplit(';', 1)[0]
    # data = json.loads(data)
    #
    # pprint(data)



main()


