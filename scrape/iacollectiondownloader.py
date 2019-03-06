import os
import time
import sys
import internetarchive as ia
from internetarchive.session import ArchiveSession
from internetarchive import get_item
from internetarchive import download

ident = 'podcasts'
destifolder = 'iapodcasts'
search = ia.search_items('collection:%s' % ident)
current = [f for f in os.listdir(destifolder)]

num = 0

for result in search: #for all items in a collection
    num = num + 1 #item count
    itemid = result['identifier']
    print('Downloading: #' + str(num) + '\t' + itemid)
    if itemid not in current:
        try:
            download(itemid, destdir=destifolder, retries=5, glob_pattern=['*.ogg', '*.mp3', '*.wav', '*.flv'])
            print('\t\t Download success.')
        except Exception as e:
            print("Error Occurred downloading () = {}".format(itemid, e) )
            print('Pausing for 20 minutes')
            #time.sleep(1200)
        #time.sleep(0.5)

    if num == 5000:
        break
