__author__ = 'Xin'

import sys
import xml.etree.cElementTree as ET
import csv
import string
import random

def main():

    try:
        csvFile = sys.argv[1]
        ## print file
    except IndexError, e:
        print "please pass in a csv file to be processed, arg 1"
        sys.exit()

    #create promotions.xml and write the header
    xmlFile = open('promotions.xml', 'w')
    xmlFile.write('<?xml version="1.0" encoding="UTF-8" ?> \n')

    #read csv file
    csvData = csv.reader(open(csvFile, "rb"))

    #construct the tree starting from Promotions
    promotions = ET.Element("Promotions")

    for row in csvData:
        print row[0]#query
        print row[2]#link
        print row[3]#title

        eQuery = row[0].decode('utf-8')
        eLink = row[2].decode('utf-8')
        eTitle = row[3].decode('utf-8')

        #generate randomID for each promotion, the ID will be in the pattern of ${SearchQuery}+Random combination of Uppercase Letter and Number
        randomID = stripeString(eQuery)+id_generator()
        ET.SubElement(promotions, "Promotion", id=randomID, queries=eQuery, title=eTitle, url=eLink, image_url="",
                        start_date="", end_date="", is_regex="false", enabled="true", description="")


    tree = ET.ElementTree(promotions)
    tree.write(xmlFile)

    xmlFile.close()

def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def stripeString(str):
    return ''.join(e for e in str if e.isalnum())

if __name__ == '__main__':
    main()