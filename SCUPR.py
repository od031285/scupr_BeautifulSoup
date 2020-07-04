#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep

base_url = "https://osg.scot/portal/index.jsp?uprn="
full_list = []


def scupperize (inlist):
    
    for uprn in inlist:
        add_list = []
        sleep(randint(3,10))
        page = requests.get(base_url + uprn)
        soup = BeautifulSoup(page.text, 'html.parser')
        pc = soup.find(class_='panel-collapse')
        for div in pc.findAll('div', attrs={'class':'panel-body'}):
            for p in div.findAll('p'):
                s = str(p.text).replace(',', '')
                add_list.append (s)
        full_list.append(add_list)
    return full_list
    

uprn_list = ["9051138577", "151113774", "9051041862", "9051053140", "151013452"]

print (scupperize(uprn_list))


