
from pprint import pprint
import os
import requests


def main():

    notAllowedName = ["FIG.NO:", "FIG.NO : "]
    badW = ["FRONT AXLE","FIG.NO:0-01 PARTIAL ENGINE","FUEL INJECTION SYSTEM","FIG.NO :0-42 FUEL PUMP AND PIPE"]

    for j in badW:
        r = checkNameComponent(j)
        pprint(r)


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

main()