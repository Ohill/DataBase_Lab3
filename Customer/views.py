from django.shortcuts import render
from .forms import Customer_Form



def Customer(request):


     return render(request, 'Sales/Sales.html', locals())