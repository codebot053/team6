import csv

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "team6.settings")
import django
django.setup()

from place.models import PlaceModel

def makedb(name, tags, img, url):
    PM = PlaceModel()
    PM.name = name
    PM.tags = tags
    PM.images = img
    PM.address = url
    PM.save()

placeinfo = open("place_with_images.csv", "r", encoding="utf-8-sig")
reader = csv.reader(placeinfo)

if __name__=='__main__':
    for line in reader:
        name = line[2].lstrip()
        tag_list = line[3].split(' • ')
        tags = ",".join(tag_list)
        img = line[5]
        url = line[4]
        makedb(name, tags, img, url)
        print(name, tags, img, url)