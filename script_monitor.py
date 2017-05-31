# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# while this is true (it is true by default),
while True:
    # set the url as VentureBeat,
    url = "https://sede.inap.gob.es/tai-2016-ingreso-libre"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    i = 0
    soup = BeautifulSoup(response.text, "lxml")
	
    for li in soup.find("div",{"id":"_contentviewer_WAR_alfresco_packportlet_INSTANCE_U7r2_content_text"}).find_all("li"):
        i=i+1
	
    if i <= 37:
        # wait 900 seconds,
        time.sleep(900)
        # continue with the script,
        continue

    # but if the word "Google" occurs any other number of times,
    else:
        # create an email message with just a subject line,
        msg = 'Subject: This is Antonio\'s script talking, CHECK FUCKING INAP!'
        # set the 'from' address,
        fromaddr = 'antoniohidalgo.inves@gmail.com'
        # set the 'to' addresses,
        toaddrs  = ['antoniohidalgo.inves@gmail.com']

        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        server_ssl.login("antoniohidalgo.inves@gmail.com", "(AJota9695)")  

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

		# ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
        server_ssl.sendmail(fromaddr, toaddrs, msg)
        server_ssl.quit()
        server_ssl.close()

        break
