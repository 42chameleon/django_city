from django.contrib import admin
from django.contrib.admin import ModelAdmin

from city.models import City, Person, Event


@admin.register(City)
class CityAdmin(ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(ModelAdmin):
    pass
