TNDWEATHER.py
=============

tndweather.py is a weather scraping tool that pulls data from timeanddate.com.
It can be used for general info, widget data, or entertainment if you are weird.

## usage: 

[python/python2] tndweather.py [-c <city>] [-C <country>] [-tlhv]

if no country is specified, 'Murica is used.

example: 

tndweather.py -c pensacola

output: 

Weather for pensacola:
----------

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

example 2:

tndweather.py -C france

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
Brest: Tue 11:52 PM Clear. Cool. 52 °F
Metz: Tue 11:52 PM 59 °F
Saint-Denis: Tue 11:52 PM Clear. Refreshingly cool. 61 °F
Caen: Tue 11:52 PM 55 °F
Montpellier: Tue 11:52 PM Clear. Cool. 61 °F
Saint-Étienne: Tue 11:52 PM 59 °F
Clermont-Ferrand: Tue 11:52 PM Clear. Refreshingly cool. 57 °F
Mulhouse: Tue 11:52 PM 61 °F
Strasbourg: Tue 11:52 PM Clear. Mild. 63 °F
Dijon: Tue 11:52 PM 59 °F
Nancy: Tue 11:52 PM Overcast. Cool. 57 °F
Taiohae: Tue 12:22 PM -
Douai: Tue 11:52 PM Clear. Cool. 52 °F
Nantes: Tue 11:52 PM 55 °F
Toulon: Tue 11:52 PM Scattered clouds. Warm. 54 °F
Grenoble: Tue 11:52 PM 57 °F
Nice: Tue 11:52 PM Overcast. Cool. 59 °F
Toulouse: Tue 11:52 PM 66 °F
Gustavia: Tue 5:52 PM Clear. Cool. 81 °F
Nîmes: Tue 11:52 PM 61 °F
Tours: Tue 11:52 PM Clear. Cool. 57 °F
Istres: Tue 11:52 PM 61 °F
Noumea: Wed 8:52 AM Clear. Cool. 77 °F
Villeurbanne: Tue 11:52 PM 64 °F

For a city, there are flags to output only particular data.

exampple 3:

tndweather.py -c brasilia -C brazil -t 
75 °F

# BUGS

The data table on timeanddate is not always consistent, so sometimes data will
come back switched, i.e. wind speed where visiblity is, etc.
