from django.contrib import admin
from .models import *

class Site_Admin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Site._meta.fields]

    # exclude = [""]
    # inlines = [FieldMappingInline]
    # fields = []
    # #exclude = ["type"]
    # #list_filter = ('report_data',)
    # search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Site


admin.site.register(Site, Site_Admin)