__author__ = 'Shubham'
import csv
import random
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
userscore={}
def userscorecalculator():
    f=open("user.csv")
    fp1=open("userscore.csv","wb")
    writer=csv.writer(fp1)
    fp2=open("userfinal.csv","wb")
    writer2=csv.writer(fp2)
    for row in csv.reader(f):
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
        global count
        count+=1
        success=0.4
        try:
            successfulorders=0
            if float(row[2])!=0:
                successfulorders=float(row[3])
                success=float(row[3])/float(row[2])


        except Exception,e:
            print count
            pass


        review=.4
        if (float(row[7])+float(row[6]))!=0:
            review=(float(row[7])*2+float(row[6]))/(3*(float(row[7])+float(row[6])))


        ratingtouser=float(row[5])/5

        predfactor=.4
        cod=0
        if float(row[3])!=0:
            cod=float(row[4])
            predfactor=1-float(row[4])/float(row[3])
        wt=0
        if(float(row[2])>30):
            score=success*(.5+.3)+review*(.2)+ratingtouser*(.2)+predfactor*(.4)/(.5+.3+(.2)+.2+.4)
            wt=.3

        else:
            score=success*(.5+float(row[2])/100)+review*(.3)+ratingtouser*(.2)+predfactor*(.4)/((.5+float(row[1])/100)+(.3)+.2+.4)
            wt=float(row[2])/100
        #score=success*(.5)+review*(.2)+ratingtouser*(.2)+predfactor*(.4)

        score+=random.uniform(-0.2,0.2)

        totalsuccesswt=wt
        if score>1:
            score=float(1.0000000)

        if float(row[2]==1):
            newuser=1
        else:
            newuser=0



        print str(count)+" : "+str(score)





        writer.writerow([count,score])


        writer2.writerow([row[1],row[2],row[3],row[4],row[5],row[6],row[7],score])

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













def pincodescoregenerator():
    for i in a:
        a[i]=a[i]/d[i]

    f=open("pin.csv")
    fp=open("pinscore.csv","wb")
    writer=csv.writer(fp)
    fp2=open("pinfinal.csv","wb")
    writer2=csv.writer(fp2)
    count=0
    for row in csv.reader(f):
        timely=float(row[2])
        total=float(row[1])
        delcost=float(row[3])

        #print "success wt:"+str(totalsuccesswt)

        aggregateuserrating=a[row[0]]
        newuserratio=b[row[0]]/10

        timeratio=timely/c[row[0]]

        delratio=delcost/200

        prepratio=1-co[row[0]]/c[row[0]]

        scorepin=(.4*aggregateuserrating+.15*newuserratio+0.25*timeratio+0.2*delratio+.4*prepratio)/(.4+.15+.25+.2+.4)

        writer.writerow([row[0],scorepin])
        writer2.writerow([row[0],aggregateuserrating,newuserratio,timeratio,delratio,prepratio,scorepin])

        print "city:"+str([row[0]])+" : "+str(scorepin)
        count=count+1


if __name__ == '__main__':
    userscorecalculator()
    pincodescoregenerator()







