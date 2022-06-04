#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import read_write_txt_file as rwt
import input_variables as ipv
import smtplib
import ssl
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM


def start_driver(head):
    # start webdriver as driver
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    if head=="no":
        options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def log_in(driver, login_link, user, pwl):
    try:
        driver.get(login_link)
        driver.implicitly_wait(60)
        time.sleep(3)
        print("open: "+login_link)
        # log in
        driver.find_element_by_id("username").send_keys(user)
        time.sleep(2)
        driver.find_element_by_id("password").send_keys(pwl)
        time.sleep(2)
        driver.find_element_by_id("loginbtn").click()
        time.sleep(3)
        return True
    except Exception as e:
        print(e)
        return False

def load_extract_compare(driver, key_el):
    driver.get(ipv.links_dict[key_el])
    driver.implicitly_wait(60)
    time.sleep(2)
    # fetch links from page
    kurse = []
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        #print(elem.get_attribute("href"))
        if ipv.aufgaben in elem.get_attribute("href"):
            print(elem.get_attribute("href"))
            kurse.append(elem.get_attribute("href"))
    print(kurse)
    # check for new links since last time
    vg = rwt.VergleichAufgaben()
    compare_items = vg.compare_it(key_el, kurse)
    if len(compare_items) == 0:
        print("no new element")
        return "keine neuen Aufgaben gefunden"
    else:
        print(compare_items)
        # update list with new results for next run
        write_items = vg.write_new_list(key_el, kurse)
        return str(compare_items)

def send_mail(sender, receiver, pw, mail_text, mail_subject):
    #create MIMEMultipart Object
    msg = MM()
    msg["Subject"] = mail_subject
    msg["From"] = sender
    msg["To"] = receiver
    #create MIMEText Object
    MTObj = MT(mail_text, "plain")
    msg.attach(MTObj)

    #create SSL connect object
    SSL_context = ssl.create_default_context()
    #create a secure SMTP connection
    server = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465, context=SSL_context)
    #login to email account
    server.login(sender, pw)
    #send email
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
    print("E_mail to "+receiver+" sent out.")
    return


# set var
mail_subject = ipv.mail_subject
mail_text = ipv.mail_text 
key_elements = list(ipv.links_dict.keys())

# start webdriver as driver
driver = start_driver(head="no")

# login to page
log_in_page = log_in(driver, ipv.login_link, ipv.user, ipv.pwl)

# loop through all relevant pages
for i in key_elements:
    # load relevant page in login area
    result = load_extract_compare(driver, i)
    print(i+": "+str(result))
    # update text object for mail
    mail_text = mail_text + i + "\n" + str(result) + "\n\n"

# send mail
send_mail(ipv.sender, ipv.receiver, ipv.pw, mail_text, mail_subject)

driver.close()
exit()


