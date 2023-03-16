from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('monthly/',views.monthly,name="monthly"),
    path('mon',views.mon,name="mon"),
    path("monthly_period_to_pay_back/",views.monthly_period_to_pay_back,name='monthly_period_to_pay_back'),
    path('wee',views.wee,name="wee"),
    path('weekly/',views.weekly,name="weekly"),
    path("weekly_period_to_pay_back/",views.weekly_period_to_pay_back,name='weekly_period_to_pay_back'),
    path('dai',views.dai,name="dai"),
    path('daily/',views.daily,name="daily"),
    path("daily_period_to_pay_back/",views.daily_period_to_pay_back,name='monthly_period_to_pay_back'),

]