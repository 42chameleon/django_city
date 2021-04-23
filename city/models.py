from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, verbose_name="Город", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField('Название мероприятия', max_length=250, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'
