from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product, MyUser
from django.core import serializers
from multiprocessing import Process
import datetime, time, json
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.

def Get_All_Products(request):
    products = Product.objects.all()
    prod_list = serializers.serialize('json', products)
    prod_list = eval(prod_list)
    products = []
    for i in prod_list:
        products.append(i)
    data = {'products': prod_list}
    return render(request, 'list_carts.html', data)

def Product_Details(request, key):
    products = Product.objects.filter(pk=key)
    prod_list = serializers.serialize('json', products)
    prod_list = eval(prod_list)
    data = {'products': prod_list}
    return render(request, 'list_carts.html', data)


def Add_To_Cart(request, key):
    prod_id = key
    response = redirect('/')
    try:
        temp_cart = request.session['shopping_cart']
        temp_cart.append(prod_id)
        request.session['shopping_cart'] = temp_cart
    except:
        request.session['shopping_cart'] = [prod_id]
    return response

def RemoveCart(request):
    try:
        del request.session['shopping_cart']
    except:
        pass
    response = redirect('/')
    return response

def RegistartionFrom(request):
    return render(request, 'registration.html')

def UserAdd(request):
    if request.POST:
        user = MyUser(name = request.POST['name'],surname = request.POST['surname'],telephone_number = request.POST['phone_number'],email = request.POST['email'])
        user.save()
    return redirect('/')

def DeleteFromCart(request, key):
    #try:
    temp_cart = request.session['shopping_cart']
    print(temp_cart)
    if key in temp_cart:
        ind = temp_cart.index(key)
        temp_cart.pop(ind)
        request.session['shopping_cart'] = temp_cart
    #except:
            #return redirect('/')
    return redirect('/')

def Cart(request):
    try:
        temp_cart = request.session['shopping_cart']
    except:
        return redirect('/')
    amounts = {}
    product_list = []
    price = 0
    for i in temp_cart:
        #if i not in amounts.keys():
        amount = temp_cart.count(i)
        amounts[i] = amount
    for i in amounts.keys():
        pr = Product.objects.get(pk=i)
        product_list.append(pr)
    product_list = serializers.serialize('json', product_list)
    product_list = eval(product_list)
    for i in product_list:
        i['fields']['amount'] = amounts[i['pk']]
        price += int(i['fields']['price']) * int(i['fields']['amount'])
    data = {'products': product_list}
    data['price'] = price
    return render(request, 'cart.html', data)

def index(request):
    return render(request, 'index.html')

def login_user(request):
    _email = request.POST['email']
    _password = request.POST['password']
    try:
        user = MyUser.objects.get(email=_email, password=_password)
    except:
        data = {'answer': 'Неверный логин или пароль'}
        return redirect('/login', data)
    print(user)
    return redirect('/login')

def login_form(request):
    return render(request, 'login.html')
