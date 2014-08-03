# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:28:16 2014

@author: Milad
"""

cities_quad = []
with open("cities_quad.txt","r") as readfile:
    for line in readfile:
        cities_quad.append(line.split(","))

quad_dict = {"NE": 1, "SE": 2, "SW": 3, "NW": 4}
cities_o = sorted(cities_quad, key=lambda word: [quad_dict[c] for c in word[2].rsplit()])

with open("ordered_cities.txt","w") as writefile:
    for i in cities_o:    
        writefile.write(str(i[0])+","+str(i[1])+","+str(i[2]))