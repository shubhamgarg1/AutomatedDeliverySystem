__author__ = 'Shubham'
import csv

a={}
b={}
c={}
d={}
co={}
#e=rating by courrier
#f=number of review
#g=number of helpful review
count=0
newuser=0
successfulorders=0
cod=0
totalsuccesswt=0
try:
    '''
    if count%11==0:
        timely=float(row[2])
        total=float(row[1])
        delcost=float(row[3])
        a[row[0]]=a[row[0]]/totalsuccesswt
        print "success wt:"+str(totalsuccesswt)

        aggregateuserrating=a[row[0]]

        newuserratio=newuser/10

        timeratio=timely/successfulorders

        delratio=delcost/200

        prepratio=1-cod/successfulorders

        scorepin=(.4*aggregateuserrating+.15*newuserratio+0.25*timeratio+0.2*delratio+.4*prepratio)/(.4+.15+.25+.2+.4)

        print "city"+str(count/11)+" "+str(scorepin)
        successfulorders=0
        totalsuccesswt=0
        newuser=0
        cod=0
        count+=1
        continue
    '''
    count+=1
    success=0.4
    try:

        #if float(row[2])!=0:
            #successfulorders=float(row[3])
            #success=float(row[3])/float(row[2])
        success=


    except Exception,e:
        print count
        pass


    review=.4
    if (float(row[7])+float(row[6]))!=0:
        review=(float(row[7])*2+float(row[6]))/(3*(float(row[7])+float(row[6])))


    ratingtouser=float(row[5])/5

    predfactor=.4
    cod=0
    score=0
    f=open("userscore.csv")
    for row in f:

        if row[0]==username:

            if(float(row[2])>30):
                score=success*(.5+.3)+review*(.2)+ratingtouser*(.2)+predfactor*(.4)/(.5+.3+(.2)+.2+.4)
                wt=.3

            else:
                score=success*(.5+float(row[2])/100)+review*(.3)+ratingtouser*(.2)+predfactor*(.4)/((.5+float(row[1])/100)+(.3)+.2+.4)
                wt=float(row[2])/100
            score=(float(row[0])*float(row[2])+score*(1+day/1000))/(float(row[2])+(1+day/1000))
            flag=1
            break
        row[2]+=1
        row[3]+=success
        row[7]+=helpful
        row[6]+=review

        f.write()
    if flag==0:
        with open('user1.csv', 'a+') as csvfile:

            csvfile.write(pincode,username,total,success,cod,review,helpfulreview)
        with open('userscore1.csv', 'a+') as csvfile:

            csvfile.write(username,score,1)


    if(float(row[2])>30):
        score=success*(.5+.3)+review*(.2)+ratingtouser*(.2)+predfactor*(.4)/(.5+.3+(.2)+.2+.4)
        wt=.3

    else:
        score=success*(.5+float(row[2])/100)+review*(.3)+ratingtouser*(.2)+predfactor*(.4)/((.5+float(row[1])/100)+(.3)+.2+.4)
        wt=float(row[2])/100
    #score=success*(.5)+review*(.2)+ratingtouser*(.2)+predfactor*(.4)

    totalsuccesswt=wt
    if score>1:
        score=float(1.0000000)

    if float(row[2]==1):
        newuser=1
    else:
        newuser=0

    print str(count)+" "+str(score)
    with open('userscore.csv', 'a+') as csvfile:
        fieldnames = ['user', 'Aggregate Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if count==1:
            writer.writeheader()


        writer.writerow({'user': str(row[1]), 'Aggregate Score': score})

    if row[0] in a.keys():
        a[row[0]]+=(score*success*wt)
    else:
        a[row[0]]=score*success*wt

    if row[0] in b.keys():
        b[row[0]]+=newuser
    else:
        b[row[0]]=newuser

    if row[0] in c.keys():
        c[row[0]]+=successfulorders
    else:
        c[row[0]]=successfulorders

    if row[0] in d.keys():
        d[row[0]]+=totalsuccesswt
    else:
        d[row[0]]=totalsuccesswt
    if row[0] in co.keys():
        co[row[0]]+=cod
    else:
        co[row[0]]=cod

except Exception,e:
    print str(e)
    pass



    #if count%11==0:


        #
for i in a:
    a[i]=a[i]/d[i]

f=open("pin.csv")
count=0
for row in csv.reader(f):
    timely=float(row[2])
    total=float(row[1])
    delcost=float(row[3])

    print "success wt:"+str(totalsuccesswt)

    aggregateuserrating=a[row[0]]
    newuserratio=b[row[0]]/10

    timeratio=timely/c[row[0]]

    delratio=delcost/200

    prepratio=1-co[row[0]]/c[row[0]]

    scorepin=(.4*aggregateuserrating+.15*newuserratio+0.25*timeratio+0.2*delratio+.4*prepratio)/(.4+.15+.25+.2+.4)

    with open('pinscore.csv', 'a+') as csvfile:
        fieldnames = ['pin', 'Aggregate Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if count==0:
            writer.writeheader()


        writer.writerow({'pin': str(row[0]), 'Aggregate Score': scorepin})

    print "city"+str([row[0]])+" "+str(scorepin)
    count=count+1








