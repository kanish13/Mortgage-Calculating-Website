from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('monthly/',views.monthly,name="monthly"),
    path('weekly/',views.weekly,name="weekly"),
    path('daily/',views.daily,name="daily"),

]