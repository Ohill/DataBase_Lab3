from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=36, blank=True, null=True, default=None, unique=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    Team_id = models.IntegerField(primary_key=True)
    Team_Name =  models.CharField(max_length=48, blank=True, null=True, default=None)
    Country = models.ForeignKey(Country, to_field='name')
    Characters = models.TextField(max_length=128, blank=True, null=True, default=None)


    def __str__(self):
        return ("%d.%s") % (self.Team_id, self.Team_Name)

