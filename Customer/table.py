import django_tables2 as tables
from .models import Customer

class Customer_Table(tables.Table):
    class Meta:
        model = Customer
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}