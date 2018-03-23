from django.db import models

class Customer(models.Model):
    Customer_id = models.IntegerField( primary_key=True)
    Customer_Name = models.CharField(max_length=48, blank=True, null=True, default=None)

    def __str__(self):
        #return str(self.Customer_id)
        return ("%d.%s") % (self.Customer_id, self.Customer_Name)