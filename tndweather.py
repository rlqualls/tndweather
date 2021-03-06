#!/usr/bin/env python

'''
Title: tndweather
Author: Robert Qualls<robert@robertqualls.com>

This is my first web scraping mini project.  It pulls the weather
for a city from www.timeanddate.com and prints it to STDOUT. If no 
country is specified, America is used.  If no city is specified, a 
list of cities in that country are printed out, along with their local
times and conditions.

dependencies: 
  requests (1.2.0) : python-requests.org  
  beautifulsoup4 (4.1.3) : crummy.com/software/BeautifulSoup

tested: python2.7.4, python3.3

usage: tndweather.py -c <city> [-C <country>] [flags]
'''

import sys
import re
import argparse

#import 3rd party dependencies
try:
  import requests
except ImportError:
  print("The requests package is not installed.")
  print("If you have pip, it can be installed with 'pip install requests'")
  exit(1)

try:
  from bs4 import BeautifulSoup
except ImportError:
  print("The beautifulsoup4 package is not installed.")
  print("If you have pip, it can be installed with 'pip install beautifulsoup4'")
  exit(1)


DEFAULT_COUNTRY = "usa"
BASE_URL = "http://www.timeanddate.com/weather/"

#command line options
parser = argparse.ArgumentParser(prog='parser')
parser.add_argument('-c', '--city', help='city name')
parser.add_argument('-C', '--country', default=DEFAULT_COUNTRY, help='country name')
parser.add_argument('-t', '--temp', action='store_true', help='output temperature')
parser.add_argument('-l', '--location', action='store_true', help='output location')
parser.add_argument('-p', '--pressure', action='store_true', help='output pressure')
parser.add_argument('-H', '--humidity', action='store_true', help='output humidity')
parser.add_argument('-v', '--visibility', action='store_true', help='output visibility')
args = parser.parse_args()

city = args.city
country = args.country
t_flag = args.temp
l_flag = args.location
p_flag = args.pressure
h_flag = args.humidity
v_flag = args.visibility
  
#scrape section
if city:
  #--city mode--
  r = requests.get(BASE_URL + country + "/" + city)
  soup = BeautifulSoup(r.text)
  if soup.select(".rpad") == []:
    print("Your city did not return any results")
    exit(1)
  conditions = soup.select(".tophead")[0].text
  table = soup.select(".rpad")[0].select("tr td")
  location = table[1].text
  temp = table[3].text
  comfort = table[5].text
  dew = table[7].text
  pressure = table[9].text
  humidity = table[11].text
  visibility = table[13].text
  last_update = table[17].text if 17 < len(table) else 'N/A'

  #city output
  if (t_flag):
    print(temp)
  elif (l_flag):
    print(location)
  elif (p_flag):
    print(pressure)
  elif (v_flag):
    print(visibility)
  elif (h_flag):
    print(humidity)
  else:
    print("Weather for " + city + ":")
    print("----------\n")
    print("Location   : " + location)
    print("Conditions : " + conditions)
    print("Temperature: " + temp)
    print("Comfort    : " + comfort)
    print("Dew Point  : " + dew)
    print("Pressure   : " + pressure)
    print("Humidity   : " + humidity)
    print("Visibility : " + visibility)
    print("Last Update: " + last_update)
else:
  #--country mode--
  r = requests.get(BASE_URL + country)
  soup = BeautifulSoup(r.text)
  cities = soup.find_all("a", href=re.compile("weather/" + country))
  del cities[0] # remove header because it isn't a city
  conditions = soup.select('.r')
  temps = soup.select('.rbi')
  for i in range(0, len(cities)):
    #add city name and local time
    out_str = cities[i].text + ": " + soup.select('.r')[i*2].text
    
    #add condition description only if it exists
    if soup.select('.r')[i+1].img:
      out_str += " " + soup.select('.r')[i+1].img['alt'] 
    
    #add local temperature
    out_str += " " + temps[i].text
    
    print(out_str)
    
