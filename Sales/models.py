from django.db import models
from Customer.models import Customer
from Team.models import Team
from Site.models import Site


class Fact_Sale(models.Model):
    id = models.AutoField(primary_key=True)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    Cost = models.IntegerField()
    Team_id = models.ForeignKey(Team, to_field="Team_id")
    Site_id = models.ForeignKey(Site, to_field="Site_id")
    Customer_id = models.ForeignKey(Customer, to_field="Customer_id")

    def __str__(self):
        return "Id:%d Customer_id:%d Cost:%s Team_id:%d Site_id:%d Date:%s " %(self.id,self.Customer_id.Customer_id,self.Cost,self.Team_id.Team_id,self.Site_id.Site_id,self.Date)
