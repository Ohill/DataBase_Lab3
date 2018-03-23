from django.contrib import admin
from .models import *



class Fact_Sale_Admin (admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Fact_Sale._meta.fields]


    class Meta:
        model = Fact_Sale


admin.site.register(Fact_Sale,Fact_Sale_Admin)