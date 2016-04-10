__author__ = 'VanDuan'
import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    #print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    #print 'Retrieved',len(data),'characters'
   # print data
    tree = ET.fromstring(data)

    results = tree.findall('result')
    try:
        add_com = results[0].find('address_component')
        uc = add_com.find('short_name').text
        if len(uc) != 2:
            print 'Not found!!!'
            continue
        print 'Country code:', uc
        print '==============<'
    except:
        print 'Not found!!!'