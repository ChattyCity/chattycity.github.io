# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 17:02:56 2014

@author: Milad
"""
import simplejson
import os

chatty = "C:/Users/Milad/Documents/code/fun/ChattyCity"
indir = chatty+"/parsedfiles"
outdir = os.getcwd()
g = os.path.join(indir, "tweets.Jul12-1801.txt_parsed.txt")

t = []  
with open(g, "r") as readfile:
    readfile.readline()
    for line in readfile:
        l = line.split("\t")
        #grab records that have both source and dest cities and non-zero sent
        if l[3] != "None" and l[4] != "None" and float(l[6].rstrip("\n")) != 0:
                t.append([l[3],l[4],l[6].rstrip("\n")])

#build list of cities with only pos or neg sentiments
cities = []
for tup in t:
    cities.append(tup[0])
    cities.append(tup[1])
    cities = list(set(cities))



#find 50 cities with most tweets
count_dict = {}
for i in cities:
    count = 0
    for tup in t:
        if tup[0] == i or tup[1] == i:
            count += 1
    count_dict[i] = count

cities = sorted(count_dict, key=count_dict.__getitem__,reverse = True)[0:50]


#order cities using ordered_cities.txt
quad = {}
cities_dict = {}
count = 0
with open("ordered_cities.txt","r") as readfile:
    for line in readfile:
        quad[line.split(",")[0].lower()] = line.split(",")[1][0:2]
        cities_dict[line.split(",")[0].lower()] = count
        count += 1
        
cities = sorted(cities, key=lambda word: [cities_dict[word]])

#build pos and neg matrices
matrix_pos = []
matrix_neg = []

for i in cities:
    mp, mn = [], []
    for j in cities:
        count_pos, count_neg = 0, 0
        for tup in t:
            if tup[0] == i and tup[1] == j:
                if float(tup[2]) > 0:
                    count_pos += 1
                elif float(tup[2]) < 0:
                    count_neg += 1

        mp.append(count_pos)
        mn.append(count_neg)
        
    matrix_pos.append(mp)
    matrix_neg.append(mn)

#normalize pos and neg matrices
total_vol_pos = sum(matrix_pos)
total_vol_neg = sum(matrix_neg)


for i in range(len(matrix_pos)):
    for j in range(len(matrix_pos[i])):
        matrix_pos[i][j] = float(matrix_pos[i][j])/total_vol_pos if float(matrix_pos[i][j])/total_vol_pos > 0.0005 else 0
        # 0.5% threashold
for i in range(len(matrix_neg)):
    for j in range(len(matrix_neg[i])):
        matrix_neg[i][j] = float(matrix_neg[i][j])/total_vol_neg if float(matrix_neg[i][j])/total_vol_neg > 0.0005 else 0
        # 0.5% threshold
        
#save to json file
with open(os.path.join(outdir, "matrix_pos.json"),"w") as writefile:
    simplejson.dump(matrix_pos, writefile)

with open(os.path.join(outdir, "matrix_neg.json"),"w") as writefile:
    simplejson.dump(matrix_neg, writefile)
    
with open(os.path.join(outdir, "cities.csv"),"w") as writefile:
    writefile.write("name,quad,ind\n")
    new = False
    count = 0
    for i in range(len(cities)):
        writefile.write(cities[i]+","+quad[cities[i]]+","+str(count)+"\n")

        if i<len(cities)-1 and quad[cities[i]] != quad[cities[i+1]]:
            new = True
        if new:
            count = 0
            new = False
        else:
            count += 1                