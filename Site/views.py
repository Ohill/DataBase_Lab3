from django.shortcuts import render
from .forms import Site_Form



def Site(request):


     return render(request, 'Sales/Sales.html', locals())