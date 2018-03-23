import django_tables2 as tables
from .models import Fact_Sale

class Fact_Sale_Table(tables.Table):
    class Meta:
        model = Fact_Sale
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

