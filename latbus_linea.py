# Import requests (to download the page)
import requests

import time

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

def has_value(tag):
	if tag.has_attr('value'):
		return tag['value']!= ''
	else:
		return 0
			
while True:
    t1 = time.time()
    # set the url as VentureBeat,
    url = "http://latbus.com/"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url +"linyhora_directo.asp", headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    for linea in soup.find_all(has_value):
        str = list(linea.strings)
        print(str[0]+str[1])
    t2 = time.time()
    print("time: ",(t2-t1),' s')
    print("size: ",(len(response.content)/1024),' kB')
    linea=input("Introduce la línea: ")
    t3 = time.time()
    # download the homepage
    response = requests.get(url +"linea.asp?requiredlin="+ linea, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    paradas=soup.table.find_all("tr")[1].find_all("tr")[3].td.table.find_all("tr",recursive=False)
    t5 = time.time()
    for x in range(2,len(paradas)-1):
        print(paradas[x].find_all("td")[0].b.string + paradas[x].find_all("td")[2].string)
        dic_paradas={paradas[x].find_all("td")[2].a.get('href'), paradas[x].find_all("td")[2].string}
    t4 = time.time()
    print("time:  ",(t4-t3),' s')
    print("time:  ",(t4-t5),' s')
    print("size: ",(len(response.content)/1024),' kB')
    input("")
        