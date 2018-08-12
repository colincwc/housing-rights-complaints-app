from django.contrib import admin
from django.urls import path, include
from personal.views import personal, index, report, complaint, confirmed

urlpatterns = [
    path('index/', index, name='index'),
    path('personal/', personal, name='personal'),
    path('report/', report, name='report'),
    path('complaint/', complaint, name='complaint'),
    path('confirmed/', confirmed, name='confirmed'),
]