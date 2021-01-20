from django.db import models

from django.core.exceptions import ValidationError

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Number of Train')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel time')
    city_from = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='city_from_set',
                                  verbose_name='from which city')
    city_to = models.ForeignKey(City, on_delete=models.CASCADE,
                                related_name='city_to_set',
                                verbose_name='to which city')

    def __str__(self):
        return f'Train №{self.name} from {self.city_from} to {self.city_to}'

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        ordering = ['travel_time']

    def clean(self):
        if self.city_from == self.city_to:
            raise ValidationError(
                'The train cannot leave and arrive in the same city')

        qs = Train.objects.filter(city_from=self.city_from, city_to=self.city_to,
                                  travel_time=self.travel_time).exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError('change travel time')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
