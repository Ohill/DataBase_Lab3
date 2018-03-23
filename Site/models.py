from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15, blank=True, null=True, default=None, unique=True)

    def __str__(self):
        return self.name

class Site(models.Model):
    Site_id = models.IntegerField( primary_key=True)
    Site_Name =  models.CharField(max_length=48, blank=True, null=True, default=None)
    Site_Category = models.ForeignKey(Category, to_field="name")
    def __str__(self):
        #return str(self.Site_id)
        return ("%d.%s")%(self.Site_id,self.Site_Name)


