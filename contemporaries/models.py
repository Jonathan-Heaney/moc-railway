from django.db import models

# Create your models here.


class FamousPerson(models.Model):
    name = models.CharField(max_length=1000)
    occupation = models.CharField(max_length=255)
    gender = models.CharField(max_length=2)
    alive = models.BooleanField(null=True, blank=True)
    bplace_name = models.CharField(max_length=2000, null=True, blank=True)
    bplace_country = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.CharField(max_length=20, null=True, blank=True)
    birthyear = models.IntegerField(null=True, blank=True)
    dplace_name = models.CharField(max_length=2000, null=True, blank=True)
    dplace_country = models.CharField(max_length=255, null=True, blank=True)
    deathdate = models.CharField(max_length=20, null=True, blank=True)
    deathyear = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    hpi = models.FloatField()

    def __str__(self):
        return self.name
