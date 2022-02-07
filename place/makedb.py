from .models import PlaceModel
import csv


def makedb(name, tags, img, url):
    PM = PlaceModel()
    PM.name = name
    PM.tags = tags
    PM.images = img
    PM.address = url
    PM.save()