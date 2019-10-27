from django.shortcuts import render
from .models import Users
from django.shortcuts import redirect
from django.shortcuts import redirect

from .stock_model import any_stock
# Create your views here.

def welcome(request):
    # rendering WELCOME page
    return render(request, 'home/index.html')

def stock_display(request):
    # rendering display page
    # checking if method is post
    if request.method == 'POST':
        stock_id = request.POST['post_stock_id']
        stock_id = stock_id.capitalize()
        message = any_stock(stock_id)
        print(type(message))
        context = {'messages':message}
        return render(request, 'home/final.html',context)
    else:
        return render(request, 'home/index.html')

def stock_get(request):
    # rendering search page
    return render(request, 'home/getstock.html')

