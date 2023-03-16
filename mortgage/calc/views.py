from django.shortcuts import render
import math
# Create your views here.
def index(request):
    return render(request,"index.html")
def mon(request):
    return render(request,"monthly.html")
def wee(request):
    return render(request,"weekly.html")
def dai(request):
    return render(request,"daily.html")
def monthly(request):
    loan_amount=int(request.GET["amount"])
    interestt=int(request.GET["interest"])
    loan_term=int(request.GET["term"])
    interest_rate=(interestt/100)/12
    number_of_payments=loan_term*12
    monthly_mortgage_payment=(loan_amount*(interest_rate*(1 + interest_rate)**number_of_payments ))/(((1+interest_rate)**number_of_payments)-1 )
    return render(request,"monthly.html",{"result_monthly_view":monthly_mortgage_payment})

def monthly_period_to_pay_back(request):
    loan_amount=int(request.GET["money"])
    interestt=int(request.GET["rate"])
    monthly_mortgage_payment=int(request.GET["mmp"])
    interest_rate=(interestt/100)/12
    n=int(-math.log(1-interest_rate*loan_amount/monthly_mortgage_payment)/(math.log(1+interest_rate)))
    return render(request,"monthly.html",{"result_monthly_2_view":n})

def weekly(request):
    loan_amount=int(request.GET["amount_week"])
    interestt=int(request.GET["interest_week"])
    loan_term=int(request.GET["term_week"])
    interest_rate=(interestt/100)/52
    number_of_payments=loan_term*52
    weekly_mortgage_payment=(loan_amount*(interest_rate*(1 + interest_rate)**number_of_payments ))/(((1+interest_rate)**number_of_payments)-1 )
    return render(request,"weekly.html",{"result_weekly_view":weekly_mortgage_payment})

def weekly_period_to_pay_back(request):
    loan_amount=int(request.GET["money_week"])
    interestt=int(request.GET["rate_week"])
    weekly_mortgage_payment=int(request.GET["mmp_week"])
    interest_rate=(interestt/100)/52
    n=int(-math.log(1-interest_rate*loan_amount/weekly_mortgage_payment)/(math.log(1+interest_rate)))
    return render(request,"weekly.html",{"result_weekly_2_view":n})


def daily(request):
    loan_amount=int(request.GET["amount_daily"])
    interestt=int(request.GET["interest_daily"])
    loan_term=int(request.GET["term_daily"])
    interest_rate=(interestt/100)/365
    number_of_payments=loan_term*365
    daily_mortgage_payment=(loan_amount*(interest_rate*(1 + interest_rate)**number_of_payments ))/(((1+interest_rate)**number_of_payments)-1 )
    return render(request,"daily.html",{"result_daily_view":daily_mortgage_payment})

def daily_period_to_pay_back(request):
    loan_amount=int(request.GET["money_daily"])
    interestt=int(request.GET["rate_daily"])
    daily_mortgage_payment=int(request.GET["mmp_daily"])
    interest_rate=(interestt/100)/365
    n=int(-math.log(1-(interest_rate*loan_amount/daily_mortgage_payment))/(math.log(1+interest_rate)))
    return render(request,"daily.html",{"result_daily_2_view":n})

