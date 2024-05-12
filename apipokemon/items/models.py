from django.db import models


# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=100)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField()
    fling_effect_id = models.IntegerField()

    def __str__(self):
        return self.name
