


from pprint import pprint
import os
import requests
#from mysql.connector import connect, Error
from bs4 import BeautifulSoup

basef = 'C:/Projects/python/crawla'


def get_map():
    url = 'http://parts.isuzu.astra.co.id/marketing/catalog/'
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content,'html.parser')
    vhc =  soup.find_all("a")

    for link in vhc:


        try:
            iehwgn48 = ""
            ahskd = url+link.get('href') #Veicle


            namav = link.get_text()
            namav = namav.replace(" ", "")
            namav = namav.replace("/", "_")


            r = requests.get(ahskd)
            content = r.text
            sosoup = BeautifulSoup(content, 'html.parser')

            table = sosoup.find_all('table')

            main_table = table[0]
            pagination = table[1]

            table_body = main_table.find('tbody')

            rows = table_body.find_all('tr')
            component_name = rows[0]
            component_url = rows[1]

            cancm9 = component_name.find_all('td')



            TAHAP2 = []
            for o, row in enumerate(component_url):

                sia = row.find('a')
                ssia = sia.get('href')
                if ssia not in TAHAP2:
                    TAHAP2.append([cancm9[o].get_text(),sia.get('href')])  # collect url to


            for w,y in enumerate(TAHAP2):
                ioes02 = y[0]
                #ioes02 = ioes02.replace(" ","")

            #section DETAIL
                lach8 = url + y[1]  # Veicle
                jci = requests.get(lach8)
                an3agf = jci.text
                hclaisua = BeautifulSoup(an3agf, 'html.parser')
                psot49s = hclaisua.find_all('table')
                cal83 = psot49s[1]
                dpa94au = cal83.find_all('tr')

                for c,m in enumerate(dpa94au):
                    sy8gs = m.find_all('td')

                    ace9aijcv = {
                        'part_no':sy8gs[1].get_text(),
                        'desc':sy8gs[3].get_text(),
                        'model':sy8gs[7].get_text()
                    }

                    newpath = basef+"/pprint/"+namav+"/"+ioes02
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)


                    nfile = open('%s/%i.log' %(newpath,c),  'w')
                    pprint(ace9aijcv, nfile)



            # f=0
            # for k in table:
            #     nfile = open('pprint/a%s.log' % (f), 'w')
            #     pprint(k, nfile)
            #     f+=1
            #
            #
            # oa8h = link.get_text()
            # oa8h = oa8h.replace(" ", "")
            # oa8h = oa8h.replace("/", "_")
            # nfile = open('pprint/%s.log'%(oa8h), 'w')
            # pprint(iehwgn48,nfile)


        except ValueError:
            pass


    #script = soup.find_all('script')
    #map = (script[16].string).split('var locations =')
    return vhc



def main():

    map = get_map()
    logFileO = open('pprint/abc.log', 'w')
    pprint(map, logFileO)
    #cleansing(map)

main()


