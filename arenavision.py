import requests

import webbrowser
new = 2 # open in a new tab, if possible

from bs4 import BeautifulSoup

url = "http://arenavision.in/"
# set the headers like we are a browser,
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'\
    ,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'\
    ,'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3'\
    ,'Accept-Encoding': 'gzip, deflate'\
    ,'Referer': 'http://arenavision.in/'\
    ,'Cookie': '__cfduid=d73b812aa139c70f84c5d4917335291cd1481574447; beget=begetok; _ga=GA1.2.1202555729.1488306741; ads_smrt_popunder=2%7CTue%2C%2025%20Apr%202017%2018%3A58%3A47%20GMT; 141054_245550_1rhpmax=1%7CTue%2C%2025%20Apr%202017%2019%3A00%3A52%20GMT; has_js=1'\
    ,'Connection': 'keep-alive'\
    ,'Upgrade-Insecure-Requests': '1'}

response = requests.get(url +"schedule", headers=headers)

if response.status_code!=200:
    response = requests.get(url +"schedule-", headers=headers)
    
if response.status_code!=200:
    print("No se ha podido encontrar la página de eventos. Error: ", response.status_code)
    input()
    exit()
    
soup = BeautifulSoup(response.text, "lxml")
num_lin=len(soup.table.find_all('tr'))
linea=input("Hay "+str(num_lin)+" eventos. Introduce numero eventos a mostrar: ")

for row in soup.table.find_all('tr')[1:int(linea)+1]:
    if row.find_all('td')!=[]:
        for column in row.find_all('td')[:-1]:
            for string in column.stripped_strings:
                if string!=('\n'):
                    print(string,end=" ")
        for string2 in row.find_all('td')[-1].stripped_strings:
                print('\n',string2)
        print('\n')
canal=input("Introduce canal: ")


response = requests.get(url +"av"+ canal, headers=headers)
if response.status_code!=200:
    response = requests.get(url +"av"+ canal+"-", headers=headers)
    
if response.status_code!=200:
    print("No se ha podido encontrar la página. Error: ", response.status_code)
    input()
    exit()
soup = BeautifulSoup(response.text, "lxml")

webbrowser.open(soup.select('p.auto-style1')[0].a['href'],new=new)