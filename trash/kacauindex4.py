

from pprint import pprint
import os
import requests
#from mysql.connector import connect, Error
from bs4 import BeautifulSoup

basef = 'C:/Projects/python/crawla'
MAIN_URL = 'http://parts.isuzu.astra.co.id/marketing/catalog/'

def deep1():
    url = 'http://parts.isuzu.astra.co.id/marketing/catalog/'
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content,'html.parser')
    RET  =  soup.find_all("a")
    return RET

def deep2():

    for l in deep1():
        ahskd = MAIN_URL + l.get('href')  # Veicle

        namav = l.get_text()
        namav = namav.replace(" ", "")
        namav = namav.replace("/", "_")

        r = requests.get(ahskd)
        content = r.text
        sosoup = BeautifulSoup(content, 'html.parser')

        table = sosoup.find_all('table')

        pagination = table[1]

        empgn = []  # PAGINATION
        empgn.append([0, ahskd])
        pgbody = pagination.find('table')
        acsav = pgbody.find_all('a')
        for o, jbd59 in enumerate(acsav):
            empgn.append([jbd59.get_text(), MAIN_URL + jbd59.get('href')])
    return {'ret_url':ahskd, 'pg':empgn, 'cd':namav}


def deep3():
    vliey = deep2()
    empgn = vliey['pg']
    ahskd = vliey['ret_url']



    for l, hfoa38 in enumerate(empgn):

        ahfo73 = "page-%s" % (hfoa38[0])
        curdir = vliey['cd'] + "/" +ahfo73
        pprint(hfoa38[1])
        r = requests.get(hfoa38[1])
        content = r.text
        sosoup = BeautifulSoup(content, 'html.parser')

        table = sosoup.find_all('table')

        main_table = table[0]

        empgn = []  # PAGINATION
        empgn.append([0, ahskd])
        table_body = main_table.find('tbody')
        if (table_body is None):
            continue

        rows = table_body.find_all('tr')
        component_name = rows[0]
        component_url = rows[1]
        cancm9 = component_name.find_all('td')
        TAHAP2 = []

        TAHAP2 = []
        for o, row in enumerate(component_url):
            sia = row.find('a')
            ssia = sia.get('href')
            if ssia not in TAHAP2:
                TAHAP2.append([cancm9[o].get_text(), sia.get('href')])  # collect url to

        return {'d':TAHAP2, 'cd':curdir,}

def deep4():
    s = deep3()
    tah = s['d']
    curdir = s['cd']
    for w, y in enumerate(tah):
        ioes02 = y[0].strip()
        ioes02 = checkNameComponent(ioes02)

        auchals = curdir +"/"+ ioes02
        # section DETAIL
        lach8 = MAIN_URL + y[1]  # Veicle
        jci = requests.get(lach8)
        an3agf = jci.text
        hclaisua = BeautifulSoup(an3agf, 'html.parser')
        psot49s = hclaisua.find_all('table')
        cal83 = psot49s[1]
        dpa94au = cal83.find_all('tr')

        return {'d':dpa94au,'cd':auchals}

def deep5():
    acs = deep4()
    dpa94au = acs['d']
    cd = acs['cd']

    for c, m in enumerate(dpa94au):
        sy8gs = m.find_all('td')
        ace9aijcv = {
            'part_no': sy8gs[1].get_text(),
            'desc': sy8gs[3].get_text(),
            'model': sy8gs[7].get_text()
        }
        newpath = basef + "/pprint/" + cd
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        nfile = open('%s/%i.log' % (newpath, c), 'w')
        pprint(ace9aijcv, nfile)

def checkNameComponent(k):
    aos = ""
    notAllowedName = ("FIG.NO:")
    for j in notAllowedName:
        if j in k:
            wbari = k.split(' ')
            for i, elem in enumerate(wbari):
                if (i == 0):
                    continue
                aos += " " + elem
            aos = aos.strip()
        else:
            aos = k

    return aos


deep5()