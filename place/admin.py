from django.contrib import admin
from .models import PlaceModel, PlaceComment

# Register your models here.
admin.site.register(PlaceModel)
admin.site.register(PlaceComment)