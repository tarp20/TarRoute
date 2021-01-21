from django.db import models

from django.core.exceptions import ValidationError

from cities.models import City
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Number of Train')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Total Travel Time')
    city_from = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='route_city_from_set',
                                  verbose_name='from which city')
    city_to = models.ForeignKey(City, on_delete=models.CASCADE,
                                related_name='route_city_to_set',
                                verbose_name='to which city')

    trains = models.ManyToManyField(Train,verbose_name='Train List')

    def __str__(self):
        return f'Route {self.name} from {self.city_from} to {self.city_to}'

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'
        ordering = ['travel_times']

  
