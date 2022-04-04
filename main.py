# Importing Modules
import os
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.chrome.options import Options  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
from fl import keep_alive

keep_alive()

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--headless")

browser = webdriver.Chrome(options=chrome_options)


ps = os.environ['ps']
email = os.environ['email']

gmail_user = email
gmail_password = ps

sent_from = gmail_user
to = 'Your destination email'
subject = '{your cat name} Vaccine is available'
body = 'Vaccine is available be fast and reserve it'

email_text = """\
From: %s
To: %s
Subject: %s

%s""" % (sent_from, to, subject, body)

url = 'https://torontohumanesocietypublicservices.as.me/schedule.php?appointmentType=17808862#'

while True:
    browser.get(url)
    sleep(10)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    if not soup.find_all("div", class_="no-dates-available"):
        print("There is an available date mannnnnnnnnn")
        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user, gmail_password)
            smtp_server.sendmail(sent_from, to, email_text)
            smtp_server.close()
            print ("Email sent successfully!")
        except Exception as ex:
            print ("Something went wrong….",ex)
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user, gmail_password)
            smtp_server.sendmail(sent_from, to, email_text)
            smtp_server.close()
            print ("Email sent successfully! however at first there was an error")
    else:
        print("There is no available date, Please wait!")
    sleep(10)