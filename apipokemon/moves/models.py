from django.db import models

# Create your models here.

class Move(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=100)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.IntegerField()
    pp = models.IntegerField()
    accuracy = models.IntegerField()
    priority = models.IntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField()
    contest_type_id = models.IntegerField()
    super_contest_effect_id = models.IntegerField()

    def __str__(self):
        return self.name
