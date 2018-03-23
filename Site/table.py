import django_tables2 as tables
from .models import Site

class Site_Table(tables.Table):
    class Meta:
        model = Site
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}