import csv

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "team6.settings")
import django
django.setup()

from place.models import PlaceModel

def makedb(name, tag_list, img, url):
    PM = PlaceModel()
    PM.name = name
    for tag in tag_list:
        PM.tags.add(tag)
    PM.images = img
    PM.address = url
    PM.save()

def updatetags(id, tag_list):
    PM = PlaceModel.objects.get(id=id)
    PM.tags.clear()
    for tag in tag_list:
        PM.tags.add(tag)
    PM.save()



if __name__=='__main__':
    placeinfo = open("place_with_images.csv", "r", encoding="utf-8-sig")
    reader = csv.reader(placeinfo)
    for line in reader:
        id = int(line[1])+10
        name = line[2].lstrip()
        tag_list = line[3].split(' • ')
        img = line[5]
        url = line[4]
        makedb(name, tag_list, img, url)
        # updatetags(id, tag_list)
        print(tag_list)