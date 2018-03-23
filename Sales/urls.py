"""test_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Sales import views

urlpatterns = [
    url(r'^Sales/$', views.Sales, name='Sales'),
    url(r'^table_edit/$', views.table_view, name='table_view'),
    url(r'^del_sale/$', views.del_sale, name='del_sale'),
    url(r'^update_sales/$', views.update_sales, name='update_sales'),
    url(r'^upload_data/$', views.upload_data, name='upload_data'),
    url(r'^add_data/$', views.add_data, name='add_data'),
    url(r'^work_trigger/$', views.work_trigger, name='work_trigger'),

]