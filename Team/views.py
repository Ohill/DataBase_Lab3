from django.shortcuts import render
from .forms import Team_Form



def Team(request):

    # form =  Fact_Sales_Form(request.POST or None)
    # if request.method == "POST" and form.is_valid() :
    #     new_form = form.save()
    #p = Team.objects.raw("select * from team_country")
    return render(request, 'Sales/Sales.html', locals())