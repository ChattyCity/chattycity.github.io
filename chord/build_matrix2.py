# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 17:02:56 2014

@author: Milad
"""
import simplejson
import os
import time

chatty = "C:/Users/Milad/Documents/code/fun/ChattyCity"
indir = chatty+"/parsedfiles"
outdir = os.getcwd()
g = os.path.join(indir, "one.txt")

n = 40
# number of cities 

t = []  
with open(g, "r") as readfile:
    readfile.readline()
    for line in readfile:
        l = line.split("\t")
        date2 = l[2]
        #grab records that have both source and dest cities and non-zero sentiment
        if l[5] != "None" and l[6] != "None" and float(l[8].rstrip("\n")) != 0:
                t.append([l[5],l[6],l[8].rstrip("\n")])


with open(g,"r") as readfile:
    readfile.readline()
    date1 = readfile.readline().split("\t")[2]

dt = time.strptime(date1, '%Y-%m-%dT%H:%M:%S.000Z') # 'Mon Jun 8 10:51:32 +0000 2009'
date1 = time.strftime('%A, %B %d, %Y',dt) #Monday, Jun 8, 2009

dt = time.strptime(date2, '%Y-%m-%dT%H:%M:%S.000Z') # 'Mon Jun 8 10:51:32 +0000 2009'
date2 = time.strftime('%A, %B %d, %Y',dt) #Monday, Jun 8, 2009
#date range: date1 to date 2

#build list of cities with only pos or neg sentiments
cities = []
for tup in t:
    cities.append(tup[0])
    cities.append(tup[1])
    cities = list(set(cities))
    if len(cities) > 99:
        break


#find n cities with most tweets
count_dict = {}
for i in cities:
    count = 0
    for tup in t:
        if tup[0] == i or tup[1] == i:
            count += 1
    count_dict[i] = count
    
cities = sorted(count_dict, key=count_dict.__getitem__,reverse = True)[0:n]


#order cities using ordered_cities.txt
quad = {}
cities_dict = {}
count = 0
with open("ordered_cities.txt","r") as readfile:
    for line in readfile:
        quad[line.split(",")[0].lower()] = [line.split(",")[1][0:2], line.split(",")[2][0:2]] #state,quad
        cities_dict[line.split(",")[0].lower()] = count
        count += 1
        
cities = sorted(cities, key=lambda word: [cities_dict[word]])


#build pos and neg matrices
matrix_pos, matrix_neg = [], []
sent_matrix_pos, sent_matrix_neg = [], []

for i in cities:
    mp, mn = [], []
    smp, smn = [], []
    for j in cities:
        count_pos, count_neg = 0, 0
        sent_pos, sent_neg = 0.0, 0.0
        #if statement removes cities talking to themselves
        if i!=j:
            for tup in t:
                if tup[0] == i and tup[1] == j:
                    if float(tup[2]) > 0:
                        count_pos += 1
                        sent_pos += float(tup[2])
                    elif float(tup[2]) < 0:
                        count_neg += 1
                        sent_neg += float(tup[2])

        mp.append(count_pos)
        mn.append(count_neg)
        smp.append(sent_pos/count_pos if count_pos > 0 else 0)
        smn.append(sent_neg/count_neg if count_neg > 0 else 0)
        
    matrix_pos.append(mp)
    matrix_neg.append(mn)
    sent_matrix_pos.append(smp)
    sent_matrix_neg.append(smn)

#build summary dataset
#schema for each city:        [[city, #total about, %neg, #total by, %neg],
# --> top 5 talking about      [[city, vol, neg%],[city, vol, neg%],[city, vol, neg%],[city, vol, neg%],[city, vol, neg%],[max vol portion]],
# --> top 5 tweets by          [[city, vol, neg%],[city, vol, neg%],[city, vol, neg%],[city, vol, neg%],[city, vol, neg%],[max vol portion]]]
a1, a2 = {}, {}
a1vals, a2vals = {}, {}
summary = []
for i in range(len(cities)):
    #general stats
    cityname = "%s, %s"%(cities[i],quad[cities[i]][0].lower())
    l1 = [cityname]
    neg = 0
    for j in range(len(cities)):
        neg += matrix_neg[j][i]
    pos = 0
    for j in range(len(cities)):
        pos += matrix_pos[j][i]
    l1.append(neg+pos)
    a1[cities[i]] = neg+pos
    a1vals[cities[i]] = [a1[cities[i]], float(neg)/float(a1[cities[i]])]
    l1.append(float(neg)/float(neg+pos))
    neg = sum(matrix_neg[i])
    pos = sum(matrix_pos[i])
    l1.append(neg+pos)
    a2[cities[i]] = neg+pos
    a2vals[cities[i]] = [a2[cities[i]], float(neg)/float(a2[cities[i]])]
    l1.append(float(neg)/float(neg+pos))

    #others talking about city X    
    max_dict = {}
    max_dict_vals = {}
    top5 = []
    for j in range(len(cities)):
        max_dict[j] = matrix_pos[i][j] + matrix_neg[i][j]
        max_dict_vals[j] = [max_dict[j], float(matrix_neg[i][j])/float(max_dict[j])] if max_dict[j] > 0 else [0,0]
    top5 = sorted(max_dict, key=max_dict.__getitem__,reverse = True)[0:5]
    l2 = []
    for j in top5:
        l2.append([cities[j],max_dict_vals[j][0],max_dict_vals[j][1]])
    maxvp = 0
    localmax = 0
    for l in l2:
        localmax = max(l[1]*l[2], l[1]*(1-l[2]))
        maxvp = max(maxvp, localmax)
    l2.append([maxvp])
        
    #city X talking about others
    max_dict = {}
    max_dict_vals = {}
    top5 = []
    for j in range(len(cities)):
        max_dict[j] = matrix_pos[j][i] + matrix_neg[j][i]
        max_dict_vals[j] = [max_dict[j], float(matrix_neg[j][i])/float(max_dict[j])] if max_dict[j] > 0 else [0,0]
    top5 = sorted(max_dict, key=max_dict.__getitem__,reverse = True)[0:5]
    l3 = []
    for j in top5:
        l3.append([cities[j],max_dict_vals[j][0],max_dict_vals[j][1]])
    maxvp = 0
    localmax = 0
    for l in l3:
        localmax = max(l[1]*l[2], l[1]*(1-l[2]))
        maxvp = max(maxvp, localmax)
    l3.append([maxvp])
    
    summary.append([l1,l2,l3])

total_vol_pos = sum(matrix_pos)
total_vol_neg = sum(matrix_neg)

#build aggregate
agg = []
agg.append([total_vol_neg, total_vol_pos, date1.lower(), date2.lower()])

agg1 = []
a1_top5 = sorted(a1, key=a1.__getitem__,reverse = True)[0:7]
maxvp = 0
localmax = 0
for j in a1_top5:
    agg1.append([j, a1vals[j][0], a1vals[j][1]])
    localmax = max(a1vals[j][0]*a1vals[j][1], a1vals[j][0]*(1-a1vals[j][1]))
    maxvp = max(maxvp, localmax)
agg1.append([maxvp])

maxvp = 0
localmax = 0
agg2 = []   
a2_top5 = sorted(a2, key=a2.__getitem__,reverse = True)[0:7]
for j in a2_top5:
    agg2.append([j, a2vals[j][0], a2vals[j][1]])
    localmax = max(a2vals[j][0]*a2vals[j][1], a2vals[j][0]*(1-a2vals[j][1]))
    maxvp = max(maxvp, localmax)   
agg2.append([maxvp])  
 
agg.append(agg1)
agg.append(agg2)

#normalize pos and neg matrices
#set threshold
for i in range(len(matrix_pos)):
    for j in range(len(matrix_pos[i])):
        matrix_pos[i][j] = float(matrix_pos[i][j])/total_vol_pos if float(matrix_pos[i][j])/total_vol_pos > 0.001 else 0
        # 1% threashold
for i in range(len(matrix_neg)):
    for j in range(len(matrix_neg[i])):
        matrix_neg[i][j] = float(matrix_neg[i][j])/total_vol_neg if float(matrix_neg[i][j])/total_vol_neg > 0.001 else 0
        # 1% threshold
        
#save to json file
with open(os.path.join(outdir, "matrix_pos.json"),"w") as writefile:
    simplejson.dump(matrix_pos, writefile)

with open(os.path.join(outdir, "matrix_neg.json"),"w") as writefile:
    simplejson.dump(matrix_neg, writefile)

with open(os.path.join(outdir, "sent_matrix_pos.json"),"w") as writefile:
    simplejson.dump(sent_matrix_pos, writefile)

with open(os.path.join(outdir, "sent_matrix_neg.json"),"w") as writefile:
    simplejson.dump(sent_matrix_neg, writefile)
    
with open(os.path.join(outdir, "cities.csv"),"w") as writefile:
    writefile.write("name,state,quad,ind\n")
    new = False
    count = 0
    for i in range(len(cities)):
        writefile.write(cities[i]+","+quad[cities[i]][0].lower()+","+quad[cities[i]][1]+","+str(count)+"\n")

        if i<len(cities)-1 and quad[cities[i]][1] != quad[cities[i+1]][1]:
            new = True
        if new:
            count = 0
            new = False
        else:
            count += 1

with open(os.path.join(outdir, "summary.json"), "w") as writefile:
    simplejson.dump(summary, writefile)

with open(os.path.join(outdir, "aggregate.json"), "w") as writefile:
    simplejson.dump(agg, writefile)