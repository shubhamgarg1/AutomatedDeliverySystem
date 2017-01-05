__author__ = 'Shubham'
import urllib

import json
import csv

j=1


try:

    '''area="Yeshwantpur"
    city="Bangalore"
    pincode="560022"'''


    area="Yeshwantpur"
    city="Bangalore"
    pincode="560022"

    area="Sector 121 Gymkhana Club"
    city="Faridabad"
    pincode="121102"


    i=0
    while i<len(area):
        if(area[i]==','):
            area[i]=' '
        i+=1



    address=area.split(' ')

    print "Input \nArea:"+area+" \nCity:"+city+" \npincode:"+pincode
    url="https://maps.googleapis.com/maps/api/geocode/json?address="+str(area)+str(city)+"&key=AIzaSyCk05HoXI0NyBl2dVclxm3NOXNKIn-ck-4"

    response=urllib.urlopen(url)
    content=response.read()
    data=json.loads(content)

    ans=1
    if "status" in data:
        #print data["status"]
        if data["status"]!="OK":
            ans=0

    if ans==0:
        print "Not Accepted"



    count=0
    count1=0

    if ans==1:
        for i in data["results"]:
            for j in i["address_components"]:
                for k in j["types"]:
                    if k=="sublocality" :
                        flnew=1
                        for val in address:
                            s=0
                            flag=0
                            while s<10:

                                if str(s) in val:
                                    flag=1
                                    break
                                s+=1
                            if flag==1:
                                if str(val) not in j["short_name"]:
                                    flnew=0



                        if (flnew==1):
                            count1=count1+1
                    if k=="locality":


                        city=j["long_name"]
                        count=count+1

                        break
                    if(count==1):
                        break
                if(count==1):
                    break
            if(count==1):
                break

        if count==0:
            ans=0

        if count1==0:
            ans=0



        flag=0
        f=open("pincode.csv")
        count=0
        for row in csv.reader(f):

            if (row[0]==pincode):

                if(row[1]==city ):
                    flag=1
                    break
        if(flag==1 and ans==1):
            print "Accepted"
        else:
            print "Not Accepted"


except Exception,e:
    print str(e)
    pass


