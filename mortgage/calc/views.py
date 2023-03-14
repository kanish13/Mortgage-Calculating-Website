from django.shortcuts import render
import math
# Create your views here.
def index(request):
    return render(request,"index.html")
def monthly(request):
    loan_amount=int(request.GET["amount"])
    interest_rate=int(request.GET["interest"])
    loan_term=int(request.GET["term"])
    number_of_payments=loan_term*12
    monthly_mortgage_payment=loan_amount*(interest_rate*(1 + interest_rate)**number_of_payments )/( (1 + interest_rate)**number_of_payments-1 )
    return render(request,"result_monthly.html",{"result_monthly":monthly_mortgage_payment})
def monthly_period_to_pay_back(request):
    loan_amount=int(request.GET["money"])
    interest_rate=int(request.GET["rate"])
    monthly_mortgage_payment=int(request.GET["mmp"])
    n=-math.log(1-interest_rate*loan_amount/monthly_mortgage_payment)/math.log(1+interest_rate)
    return render(request,"result_monthly_2",{"result_monthly_2":n})

