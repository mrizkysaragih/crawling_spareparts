


from pprint import pprint
import os
import requests
#from mysql.connector import connect, Error
from bs4 import BeautifulSoup

basef = 'C:/Projects/python/crawla'


def burn():
    url = 'http://parts.isuzu.astra.co.id/marketing/catalog/'
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content,'html.parser')
    vhc =  soup.find_all("a")

    for link in vhc:
        try:
            ahskd = url+link.get('href') #Veicle


            namav = link.get_text()
            namav = namav.replace(" ", "")
            namav = namav.replace("/", "_")


            # if(namav == "NMR_NLR" or namav == "NQR2012" or namav == "ELF" or namav == "GIGAFVR"):
            #      continue
            # if(namav != "PICKUP(TBR54)"):
            #      continue


            r = requests.get(ahskd)
            content = r.text
            sosoup = BeautifulSoup(content, 'html.parser')

            table = sosoup.find_all('table')

            if(len(table)==1):
                continue # no Data

            pagination = table[1]

            empgn = [] #PAGINATION
            empgn.append([0,ahskd])
            pgbody = pagination.find('table')

            if(pgbody is None):
                continue


            acsav = pgbody.find_all('a')
            try:

                for o, jbd59 in enumerate(acsav):
                    empgn.append([jbd59.get_text(),url + jbd59.get('href')])

                for l, hfoa38 in enumerate(empgn):


                    klna = int(l)

                    ahfo73 = "page-%s"%(hfoa38[0])

                    if(klna < 10): #assign page
                        continue

                    pprint(hfoa38[1])

                    r = requests.get(hfoa38[1])
                    content = r.text
                    sosoup = BeautifulSoup(content, 'html.parser')

                    table = sosoup.find_all('table')

                    main_table = table[0]

                    empgn = [] #PAGINATION
                    empgn.append([0,ahskd])
                    table_body = main_table.find('tbody')
                    if(table_body is None):
                        continue


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
                        ioes02 = y[0].strip()
                        ioes02 = checkNameComponent(ioes02)

                        auchals = namav + "/" + ahfo73 + "/" +ioes02
                        pprint(auchals)  # pprint sampe mana


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
                            newpath = basef+"/pprint/"+namav+"/"+ahfo73+"/"+ioes02
                            if not os.path.exists(newpath):
                                os.makedirs(newpath)
                            nfile = open('%s/%i.log' %(newpath,c),  'w')
                            pprint(ace9aijcv, nfile)
                        #exit()
            except ValueError:
                pass


        except ValueError:
            pass

    return vhc

def checkNameComponent(k):
    notAllowedName = ["FIG.NO:","FIG.NO :"]
    for h,j in enumerate(notAllowedName):
        if j in k:
            if(h==0):
                k = pnaleka0(k)
            elif(h==1):
                k = pnaleka1(k)

    return k

def pnaleka0(k):
    aos = ""
    wbari = k.split(' ')
    for i, elem in enumerate(wbari):
        if (i == 0):
            continue
        aos += " " + elem
    aos = aos.strip()
    return aos


def pnaleka1(k):
    aos = ""
    wbari = k.split(' ')
    for i, elem in enumerate(wbari):
        if (i <= 1):
            continue
        aos += " " + elem
    aos = aos.strip()
    return aos


def main():

    burn()
    #cleansing(map)

main()


