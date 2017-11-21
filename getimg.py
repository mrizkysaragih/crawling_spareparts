


from pprint import pprint
import os
import requests
#from mysql.connector import connect, Error
from bs4 import BeautifulSoup
import json
basef = 'C:/Projects/python/crawla'

import re


def main(aoish):

    #aoish = 'http://parts.isuzu.astra.co.id/marketing/catalog/detail.php?fig=5-10&vehicle=panther&type=PANTHER'
    maural = "http://parts.isuzu.astra.co.id/marketing/catalog/"

    r = requests.get(aoish)
    content = r.text
    sosoup = BeautifulSoup(content, 'html.parser')
    ambilVar = sosoup.find_all('script')[2]

    asif = ambilVar.string.split(',')
    for j in asif:
       if "print" in j:
          j = j.replace('"','').strip()
          o = j.split('/')
          n = o[-1]
          c = o[1]
          hc = maural+'/'+j
          oauce = "images/%s"%(c)


          if not os.path.exists(oauce):
             os.makedirs(oauce)

          img_data = requests.get(hc).content
          with open('%s/%s'%(oauce,n), 'wb') as handler:
             handler.write(img_data)




