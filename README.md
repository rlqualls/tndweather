TNDWEATHER.py
=============

tndweather.py is a weather scraping tool that pulls data from timeanddate.com.
It can be used for general info, widget data, or entertainment if you are weird.

### requirements:

1. python 2.7.4 / python 3.3 (others probably work but are untested)
2. requests 1.2.0 - HTTP request library
3. beautifulsoup4 4.1.3 - HTML parser

    pip install requests
    pip install beautifulsoup4

### usage: 

    [python/python2] tndweather.py [-c <city>] [-C <country>] [-tlhv]

if no country is specified, 'Murica is used.

    tndweather.py -c pensacola

outputs something like: 

    Weather for pensacola:

    Location   : Pensacola Regional Airport  
    Conditions : Sunny. Warm.  
    Temperature: 79 °F  
    Comfort    : 81 °F  
    Dew Point  : 67 °F  
    Pressure   : 30.11 "Hg  
    Humidity   : 67%  
    Visibility : 10 mi  
    Last Update: Tue 3:53 PM CDT  

if no city is specified, a list of cities and their conditions is output.

    tndweather.py -C france

outputs something like:

    Aix-en-Provence: Tue 11:52 PM Clear. Cool. 57 °F  
    Le Havre: Tue 11:52 PM 55 °F  
    Orléans: Tue 11:52 PM Overcast. Cool. 57 °F  
    Ajaccio: Tue 11:52 PM 54 °F  
    Le Mans: Tue 11:52 PM Clear. Cool. 57 °F  
    Papeete: Tue 11:52 AM 86 °F  
    Amiens: Tue 11:52 PM Clear. Cool. 57 °F  
    Lens: Tue 11:52 PM 52 °F  
    Paris: Tue 11:52 PM 59 °F  
    Angers: Tue 11:52 PM 57 °F  
    Lille: Tue 11:52 PM Scattered showers. Scattered clouds. Warm. 52 °F  
    Perpignan: Tue 11:52 PM 63 °F  
    Bastia: Tue 11:52 PM Passing clouds. Cool. 52 °F  
    Limoges: Tue 11:52 PM 57 °F  
    Reims: Tue 11:52 PM Passing clouds. Cool. 55 °F  
    Besançon: Tue 11:52 PM 61 °F  
    Lyon: Tue 11:52 PM 64 °F  
    Rennes: Tue 11:52 PM 55 °F  
    Bordeaux: Tue 11:52 PM 61 °F  
    Marigot: Tue 5:52 PM 81 °F  
    Rouen: Tue 11:52 PM Passing clouds. Cool. 55 °F  
    Boulogne-Billancourt: Tue 11:52 PM 61 °F  
    Marseille: Tue 11:52 PM Passing clouds. Mild. 57 °F  
    Royan: Tue 11:52 PM 59 °F  
    . . .

for a city, there are flags to output only particular data.

    tndweather.py -c brasilia -C brazil -t 

outputs temperature in Fahrenheit (timeanddate.com doesn't seem to have Celsius:    
    
    75 °F

see tndweather.py -h for all options

## BUGS

The data table on timeanddate.com is not always consistent, so sometimes data will
come back switched, i.e. wind speed where visibility is, etc.
