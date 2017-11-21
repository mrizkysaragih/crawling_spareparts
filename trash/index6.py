


from pprint import pprint
import os
import requests
#from mysql.connector import connect, Error
from bs4 import BeautifulSoup
import json
basef = 'C:/Projects/python/crawla'

import re


def main():
    s = open("klice.js", 'r').read()

    soup = BeautifulSoup(s, "html.parser")

    pattern = re.compile(r"imagearray:\s+=\s+(\{.*?\});\n")
    script = soup.find("script", text=pattern)

    data = pattern.search(script.text).group(1)
    data = json.loads(data)
    print(data)

main()


