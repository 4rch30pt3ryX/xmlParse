#xml parser/ ElementTree comes standard with python
import xml.etree.ElementTree as ET

"""
This program is designed to parse information from Transaction Wireless
eGift Card purchases from XML payloads.  It scrapes Parent(TransactionNumber),
Child(MsgId), and then returns an additional list with an Optin Status of '1'
tied by MsgId

Running this will require the installation of Python2.7 or Python3
"""


filepath = (
    r'C:\Users\gemmml9\Documents\Transaction Wireless\yard_house_recon_20170612_050015.xml'
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
    

            
# xmlParse
