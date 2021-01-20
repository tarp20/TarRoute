from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Train


class TrainAdmin(admin.ModelAdmin):

    class Meta:
        model = Train

    list_display = ('name', 'city_from', 'city_to', 'travel_time')
    list_editable = ('travel_time',)


admin.site.register(Train, TrainAdmin)
