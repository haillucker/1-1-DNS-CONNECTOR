#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# ( -- LOGO * INFO -- ) #
bugs = '''
   ____  _                 _ _       ____  _   _ ____  
  / __ \/ | __ _ _ __   __| / |     |  _ \| \ | / ___| 
 / / _` | |/ _` | '_ \ / _` | |_____| | | |  \| \___ \ 
| | (_| | | (_| | | | | (_| | |_____| |_| | |\  |___) |
 \ \__,_|_|\__,_|_| |_|\__,_|_|     |____/|_| \_|____/ 
  \____/                                               
\n[$] 1&1 DNS SEL CONNECTOR.
[$] URL = ('https://www.Brazzers.com/').
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL API SCRIPT -- ) #

print bugs
print '\n[+] 1&1 DNS SEL CONNECTOR [+]'
print ''
# ----------------------------------- ## ----------------------------------- ## ----------------------------------- #
domains_list = raw_input('[X] ENTER YOUR DOMAINS LIST X> ')
my_url = raw_input('[X] ENTER [MY] 1&1 URL WITH HTTPS X> ')
my_acc = raw_input('[X] ENTER YOUR LOGIN DATA LIKE [CUST_ID:PASSWORD] X> ')
dns_num = raw_input('[X] ENTER YOUR DNS NUM X> ')
# ----------------------------------- ## ----------------------------------- ## ----------------------------------- #
user, password = my_acc.split(":")
try:
	file = open(domains_list,'r').readlines()
except (IOError, TypeError) as e:
	print '[X] CAN NOT OPEN DOMAINS FILE PLEASE CHECK PATH NAME.'
	time.sleep(1000000) # TANY WLA RAY7 ELFAR7 ? MSTNY 7D YA NQM ?
# ----------------------------------- ## ----------------------------------- ## ----------------------------------- #
try:
	driver = webdriver.Chrome('G:\\Selenium\\Chrome\\chromedriver.exe')
	driver.get(my_url)
	print '\n[X] OPENED LOGIN URL SUCCESSFLY.'
except (IOError, TypeError) as e:
	print '\n[X] CAN NOT OPEN LOGIN URL.'
	time.sleep(1000000) # QOMBLET M3L4
# ----------------------------------- ## ----------------------------------- ## ----------------------------------- #
time.sleep(2)
# ----------------------------------- ## ----------------------------------- ## ----------------------------------- #
# LOGIN
print '[X] LOGGING IN NOW'
# https://my.1and1.co.uk/
driver.find_element_by_id('login-form-user').send_keys(user)
driver.find_element_by_id('login-form-password').send_keys(password)
driver.find_element_by_id('login-button').click()
time.sleep(3)
if 'Logout' in driver.page_source:
	print '[X] LOGGED IN SUCCESSFLY.'
	# RED TO DOMAINS PAGE
	domains_list_url = my_url + '/domains?__lf=HomeFlow'
	driver.get(domains_list_url)
	print '[X] VISITED DOMAINS LIST PAGE.'
	# ADDING DNS NOW
	for domain in file:
		domain = domain.strip()
		domain_dns_url = my_url + '/add-dns-record/' + domain + '?__lf=HomeFlow'
		driver.get(domain_dns_url)
		driver.find_element_by_id('recordHost').send_keys('@')
		driver.find_element_by_id('recordValue').send_keys(dns_num)
		driver.find_element_by_xpath('//button[@class="button-primary PfxInputSubmit"]').click()
		time.sleep(1)
		if str(dns_num) in driver.page_source:
			print '\n[X] DNS [ ' + dns_num + ' ] ADDED SUCCESSFLY ON [ ' + domain + ' ].'
			driver.get(domains_list_url)
		else:
			print '[X] UNEXPECTED ERROR PLEASE CHECK YOUR BROWSER ERROR.'
			break
else:
	print '[X] INVALID LOGIN USER || PASSWORD.'
	time.sleep(1000000) # QOMBLET M3L4