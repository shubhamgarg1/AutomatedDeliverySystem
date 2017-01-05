__author__ = 'Shubham'

import csv
f=open("data_inp3.csv")
a={}
#e=rating by seller
#f=number of review
#g=number of helpful review
count=0

for row in csv.reader(f):


    rating=float(row[2])/5




    city_demand=1-float(row[3])/float(row[4])





    revenue=.01
    if float(row[5])!=0:
        revenue=float(row[6])/float(row[5])

    #score=success*(.5+float(row[1])/1000)+review*(.2)+ratingtouser*(.2)+predfactor*(.4)/((.5+float(row[1])/1000)+(.2)+.2+.4)
    score=rating*(.3)+city_demand*(.1)+revenue*(.6)

    if score>1:
        score=1.0
    print score
'''
    if row[0] in a.keys():
        a[row[0]]+=(score*success)
    else:
        a[row[0]]=score*success

with open('datapin.csv', 'w') as csvfile:
    fieldnames = ['citypin', 'Aggregate User Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in a:
        writer.writerow({'citypin': i, 'Aggregate User Score': a[i]})

'''




