#!usr/bin/python
"""
                        *******************************
                        *   Created by 4rch30pt3ryX   *
                        *******************************

"""

"""
This program is designed to parse information from Transaction Wireless
eGift Card purchases from XML payloads.  It scrapes Parent(TransactionNumber),
Child(MsgId), and then returns an additional list with an Optin Status of '1'
tied by MsgId

"""

import xml.etree.ElementTree as ET
#xml parser/ ElementTree comes standard with python
import os

def creator():
    rows, columns = os.popen('stty size', 'r').read().split()

    intcol = int(columns)
    print('\n')
    print('*-    Simple XML Parser    -*'.center(intcol))
    print('\n')
    print('*************************************'.center(intcol))
    print('*    - Created By 4rch30pt3ryX -    *'.center(intcol))
    print('*************************************'.center(intcol))
    print('_' * intcol)
    print('\n')

creator()


filepath = (
    r'C:\Users\<username>\Documents\Path\to\file.xml'
    ) #swap these accordingly

tree = ET.ElementTree(file=filepath)

parsedTuple = []

purchlist = []

for elem in tree.iter(tag='transaction'): #Main information thread
    for item in elem.getchildren():
        if item.tag == 'Recipient': #child XML tag
            for itm in item.getchildren():
                if itm.tag == 'MsgId': #child XML tag, we want this
                    
                    msgid = (itm.tag, itm.text)
                    parsedTuple.append(msgid)
                    
        if item.tag == 'Purchaser': #child XML tag, we want it's child
            for it in item.getchildren():
                if it.tag == 'OptIn':#child of child XML tag, we want this
                    optin = (it.tag, it.text)
                    if it.text == '1':
                        optins = (optin, msgid)
                        #print (optins)
                        purchlist.append(optins)
            
        if item.tag == 'TransactionNumber': #child XML tag we want this
            #print (item.tag, item.text)
            transmsgid = (item.tag, item.text)
            parsedTuple.append(transmsgid)
            
#print (parsedTuple)

purchlen = len(purchlist)
print(str(purchlen) + '\n')
print(purchlist)


#print to file 'parsedXML.txt'
f = open('parsedXML.txt', 'w')

for x in parsedTuple:
    line = ' '.join(str(s) for s in x)
    f.write(line + '\n')

for y in purchlist:
    line = ' '.join(str(s) for s in y)
    f.write(line + '\n')
f.close()
    

            
