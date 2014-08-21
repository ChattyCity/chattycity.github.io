# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 22:07:55 2014

@author: Milad

capitals: capital of 50 states, in state alphabetical order
top_cities_pop: top 100 cities by population
cities: 50 capitals + 50 most populous cities that are not capitals

"""

capitals = ['Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'Saint Paul', 'Jackson', 'Jefferson City', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Santa Fe', 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne']

top_cities_pop = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Indianapolis', 'Jacksonville', 'San Francisco', 'Columbus', 'Charlotte', 'Fort Worth', 'Detroit', 'El Paso', 'Memphis', 'Seattle', 'Denver', 'Washington', 'Boston', 'Nashville', 'Baltimore', 'Oklahoma City', 'Louisville', 'Portland', 'Las Vegas', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Long Beach', 'Kansas City', 'Mesa', 'Virginia Beach', 'Atlanta', 'Colorado Springs', 'Omaha', 'Raleigh', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Cleveland', 'Wichita', 'Arlington', 'New Orleans', 'Bakersfield', 'Tampa', 'Honolulu', 'Aurora', 'Anaheim', 'Santa Ana', 'St. Louis', 'Riverside', 'Corpus Christi', 'Lexington', 'Pittsburgh', 'Anchorage', 'Stockton', 'Cincinnati', 'Saint Paul', 'Toledo', 'Greensboro', 'Newark', 'Plano', 'Henderson', 'Lincoln', 'Buffalo', 'Jersey City', 'Chula Vista', 'Fort Wayne', 'Orlando', 'St. Petersburg', 'Chandler', 'Laredo', 'Norfolk', 'Durham', 'Madison', 'Lubbock', 'Irvine', 'Winston Salem', 'Glendale', 'Garland', 'Hialeah', 'Reno', 'Chesapeake', 'Gilbert', 'Baton Rouge', 'Irving', 'Scottsdale', 'North Las Vegas', 'Fremont', 'Boise', 'Richmond', 'San Bernardino']

cities = ['Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'Saint Paul', 'Jackson', 'Jefferson City', 'Helena', 'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Santa Fe', 'Albany', 'Raleigh', 'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne', 'New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Jacksonville', 'San Francisco', 'Charlotte', 'Fort Worth', 'Detroit', 'El Paso', 'Memphis', 'Seattle', 'Washington', 'Baltimore', 'Louisville', 'Portland', 'Las Vegas', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Long Beach', 'Kansas City', 'Mesa', 'Virginia Beach', 'Colorado Springs', 'Omaha', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Cleveland', 'Wichita', 'Arlington', 'New Orleans', 'Bakersfield', 'Tampa', 'Aurora', 'Anaheim', 'Santa Ana', 'St. Louis', 'Riverside', 'Corpus Christi', 'Lexington', 'Pittsburgh']

cities_l = ['montgomery', 'juneau', 'phoenix', 'little rock', 'sacramento', 'denver', 'hartford', 'dover', 'tallahassee', 'atlanta', 'honolulu', 'boise', 'springfield', 'indianapolis', 'des moines', 'topeka', 'frankfort', 'baton rouge', 'augusta', 'annapolis', 'boston', 'lansing', 'saint paul', 'jackson', 'jefferson city', 'helena', 'lincoln', 'carson city', 'concord', 'trenton', 'santa fe', 'albany', 'raleigh', 'bismarck', 'columbus', 'oklahoma city', 'salem', 'harrisburg', 'providence', 'columbia', 'pierre', 'nashville', 'austin', 'salt lake city', 'montpelier', 'richmond', 'olympia', 'charleston', 'madison', 'cheyenne', 'new york', 'los angeles', 'chicago', 'houston', 'philadelphia', 'san antonio', 'san diego', 'dallas', 'san jose', 'jacksonville', 'san francisco', 'charlotte', 'fort worth', 'detroit', 'el paso', 'memphis', 'seattle', 'washington', 'baltimore', 'louisville', 'portland', 'las vegas', 'milwaukee', 'albuquerque', 'tucson', 'fresno', 'long beach', 'kansas city', 'mesa', 'virginia beach', 'colorado springs', 'omaha', 'miami', 'oakland', 'minneapolis', 'tulsa', 'cleveland', 'wichita', 'arlington', 'new orleans', 'bakersfield', 'tampa', 'aurora', 'anaheim', 'santa ana', 'st. louis', 'riverside', 'corpus christi', 'lexington', 'pittsburgh']

cities_ln = ['montgomery', 'juneau', 'phoenix', 'littlerock', 'sacramento', 'denver', 'hartford', 'dover', 'tallahassee', 'atlanta', 'honolulu', 'boise', 'springfield', 'indianapolis', 'desmoines', 'topeka', 'frankfort', 'batonrouge', 'augusta', 'annapolis', 'boston', 'lansing', 'saintpaul', 'jackson', 'jeffersoncity', 'helena', 'lincoln', 'carsoncity', 'concord', 'trenton', 'santafe', 'albany', 'raleigh', 'bismarck', 'columbus', 'oklahomacity', 'salem', 'harrisburg', 'providence', 'columbia', 'pierre', 'nashville', 'austin', 'saltlakecity', 'montpelier', 'richmond', 'olympia', 'charleston', 'madison', 'cheyenne', 'newyork', 'losangeles', 'chicago', 'houston', 'philadelphia', 'sanantonio', 'sandiego', 'dallas', 'sanjose', 'jacksonville', 'sanfrancisco', 'charlotte', 'fortworth', 'detroit', 'elpaso', 'memphis', 'seattle', 'washington', 'baltimore', 'louisville', 'portland', 'lasvegas', 'milwaukee', 'albuquerque', 'tucson', 'fresno', 'longbeach', 'kansascity', 'mesa', 'virginiabeach', 'coloradosprings', 'omaha', 'miami', 'oakland', 'minneapolis', 'tulsa', 'cleveland', 'wichita', 'arlington', 'neworleans', 'bakersfield', 'tampa', 'aurora', 'anaheim', 'santaana', 'st.louis', 'riverside', 'corpuschristi', 'lexington', 'pittsburgh']

cities_filter = ['Montgomery,Juneau,Phoenix,Little Rock,Sacramento,Denver,Hartford,Dover,Tallahassee,Atlanta,Honolulu,Boise,Springfield,Indianapolis,Des Moines,Topeka,Frankfort,Baton Rouge,Augusta,Annapolis,Boston,Lansing,Saint Paul,Jackson,Jefferson City,Helena,Lincoln,Carson City,Concord,Trenton,Santa Fe,Albany,Raleigh,Bismarck,Columbus,Oklahoma City,Salem,Harrisburg,Providence,Columbia,Pierre,Nashville,Austin,Salt Lake City,Montpelier,Richmond,Olympia,Charleston,Madison,Cheyenne,New York,Los Angeles,Chicago,Houston,Philadelphia,San Antonio,San Diego,Dallas,San Jose,Jacksonville,San Francisco,Charlotte,Fort Worth,Detroit,El Paso,Memphis,Seattle,Washington,Baltimore,Louisville,Portland,Las Vegas,Milwaukee,Albuquerque,Tucson,Fresno,Long Beach,Kansas City,Mesa,Virginia Beach,Colorado Springs,Omaha,Miami,Oakland,Minneapolis,Tulsa,Cleveland,Wichita,Arlington,New Orleans,Bakersfield,Tampa,Aurora,Anaheim,Santa Ana,St. Louis,Riverside,Corpus Christi,Lexington,Pittsburgh,SF,SanFrancisco,SanFran,San Fran,The City By The Bay, Fog City,The Paris of the West,TheCitybytheBay,FogCity,Frisco,TheParisoftheWest']

sf = ['san francisco,sf']

#need a list of short city names: ex. sf

"""
cities = open("top_100_cities.txt","r")
top_cities_pop = []
for city in cities:
    top_cities_pop.append(city.rstrip())

print top_cities_pop



cities = capitals

i = 0
while len(cities)<100:
    if top_cities_pop[i] not in cities:
        cities.append(top_cities_pop[i])
    i += 1

print cities, len(cities)



cities_filter = ""
for i in cities:
    cities_filter += i+","
cities_filter = cities_filter[:len(cities_filter)-1]
cities_filter = [cities_filter]

print cities_filter



cities_l = [x.lower() for x in cities]
print cities_l



cities_ln = [x.lower().replace(" ","") for x in cities]
print cities_ln


"""
