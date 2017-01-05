__author__ = 'Shubham'

__author__ = 'Shubham'
import csv
f=open("pincode.csv")
a={}
#e=rating by seller
#f=number of review
#g=number of helpful review
count=0

for row in csv.reader(f):
    success=0.4
    if float(row[1])!=0:
        success=float(row[2])/float(row[1])


    review=.4
    if (float(row[6])+float(row[5]))!=0:
        review=(float(row[6])*2+float(row[5]))/(3*(float(row[6])+float(row[5])))


    ratingtouser=float(row[4])/5

    predfactor=.4
    if float(row[2])!=0:
        predfactor=1-float(row[3])/float(row[2])

    score=success*(.5+float(row[1])/1000)+review*(.2)+ratingtouser*(.2)+predfactor*(.4)/((.5+float(row[1])/1000)+(.2)+.2+.4)
    #score=success*(.5)+review*(.2)+ratingtouser*(.2)+predfactor*(.4)

    if score>1:
        score=1.0
    print score
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




