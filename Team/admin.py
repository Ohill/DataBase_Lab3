from django.contrib import admin
from .models import *

class Team_Admin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Team._meta.fields]

    # exclude = [""]
    # inlines = [FieldMappingInline]
    # fields = []
    # #exclude = ["type"]
    # #list_filter = ('report_data',)
    # search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Team


admin.site.register(Team, Team_Admin)