from django.contrib import admin
from .models import *




class Customer_Admin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Customer._meta.fields]

    # exclude = [""]
    # inlines = [FieldMappingInline]
    # fields = []
    # #exclude = ["type"]
    # #list_filter = ('report_data',)
    # search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Customer


admin.site.register(Customer, Customer_Admin)