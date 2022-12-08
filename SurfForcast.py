# App that gathers relavent surf data based on gps coordinates.
import os
import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Globals for the purposes of initial version, using Tofino, BC here.
lat = 49.152964
long = -125.904708
laturl = str(round(lat,3))
longurl = str(round(long,3

#open chrome test software for windy at given coords
service = Service('/Users/connorcallaghan/Drivers/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
site = 'https://www.windy.com/'+laturl+'/'+longurl+'/waves?swell1,'+laturl+','+longurl
driver.get(site)

#time delay to allow webpage to load and not get error if following code runs before so.
time.sleep(4)

#grab relavent info from webpage and add them to lists
table = driver.find_element(By.ID, "detail-data-table")
str1 = table.text
list1 = str1.split('\n')
days = list1[0].split(' ')
time = list1[1].split(' ')
wind1 = list1[2:139]
waves = list1[143:237]
swell = list1[237:331]
period = list1[331].split(' ')

#scan other html classes to get wind direction
#NOT FINISHED
search = driver.find_elements(By.CLASS_NAME, "iconfront")
search = list(set(search))

for s in search:
    print(s.get_attribute("style"))
    #Use substring/index to isolate (330deg)

#Cleanup and Organize Dataset
wind =[]
for i in wind1:
    if i != '#':
        wind.append(i)

windtype = ['Speed', 'Gusts']
while len(windtype) < len(wind):
    windtype = windtype+windtype
windgroup = tuple(zip(windtype,wind))
windspeed = list(zip(windtype[::2], wind[::2]))
windgust = list(zip(windtype[1::2], wind[1::2]))

#Get a list of the dates in the surf forcast
day = str(datetime.datetime.now())
day = day.split(' ')[0]
day = day.split('-')

intday = []
for i in range(len(day)):
    intday.append(int(day[i]))

today.append(intday)
#Create a list of those days
daynum = []
for i in range(len(time)):
    if time[i].startswith('2AM'):
        today[0][2] += 1
        daynum.append(today[0][2])

day_forcast = []
for i in range(len(daynum)):
    day_forcast.append([daynum[i]])
