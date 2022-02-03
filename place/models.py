from django.db import models
from django.forms import CharField, DateTimeField, FloatField
from user.models import UserModel
from taggit.managers import TaggableManager

# Create your models here.
class PlaceModel(models.Model):
    class Meta:
        db_table = "place"

    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class PlaceComment(models.Model):
    class Meta:
        db_table = "comment"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    place = models.ForeignKey(PlaceModel, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
