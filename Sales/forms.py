from django import forms
from .models import *

class Fact_Sales_Form(forms.Form):

    # class Meta:
    #     model = Fact_Sale
    #     exclude = [""]
    Date = forms.Field()
    Cost = forms.IntegerField()
    Team_id = Team.objects.all().values_list('Team_id', 'Team_id')
    Team_id = forms.CharField(widget=forms.Select(choices=Team_id))
    Site_id = Site.objects.all().values_list('Site_id', 'Site_id')
    Site_id = forms.CharField(widget=forms.Select(choices=Site_id))
    Customer_id = Customer.objects.all().values_list('Customer_id', 'Customer_id')
    Customer_id = forms.CharField(widget=forms.Select(choices=Customer_id))



class Fact_Sales_Form_ID(forms.Form):
    id_delete = forms.IntegerField()



class Site_ID_search(forms.Form):
    id_from = forms.CharField(max_length=6)


class Fact_Sales_Form2(forms.Form):
    id_Update = Fact_Sale.objects.all().values_list('id', 'id')
    id_Update = forms.CharField(widget=forms.Select(choices=id_Update))
    Date = forms.DateField()
    Cost = forms.IntegerField()
    Team_id_Update = Team.objects.all().values_list('Team_id','Team_id')
    Team_id_Update = forms.CharField(widget=forms.Select(choices=Team_id_Update))
    Site_id_Update = Site.objects.all().values_list('Site_id', 'Site_id')
    Site_id_Update = forms.CharField(widget=forms.Select(choices=Site_id_Update))
    Customer_id_Update = Customer.objects.all().values_list('Customer_id', 'Customer_id')
    Customer_id_Update = forms.CharField(widget=forms.Select(choices=Customer_id_Update))

class Site_Category_Form(forms.Form):
    Category = forms.CharField()


class Team_Form(forms.Form):

    search_in = (('1', 'ID',), ('2', 'Country',),('3', 'Characters',),)
    search_in = forms.ChoiceField(widget=forms.RadioSelect, choices=search_in)

    _ = forms.CharField()

class Customer_ID_Form(forms.Form):
    id_=forms.CharField()

class Customer_Name_Form(forms.Form):
    Customer_Name=forms.CharField()

class Upload_Form(forms.Form):
    upload_from = forms.CharField()

class Trigger_Form (forms.Form):
    Trigger = (('1', 'ON',), ('2', 'OFF',),)
    Trigger = forms.ChoiceField(widget=forms.RadioSelect, choices=Trigger)