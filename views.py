from unicodedata import category
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from .models import Menu


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def recipe(request, category):
    menu_data = Menu.objects.filter(category=category)
    category = category
    return render(request, 'recipe.html', {'menu_data': menu_data, 'category':category})


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def loginForm(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('/menu')
        else:
            messages.success(request, 'Please enter valid credentials.')
            return redirect('/login')
    else:
        return redirect('/login')


@login_required(login_url='/login')
def logout(request):
    auth_logout(request)
    messages.success(request, 'Logout successfully.')
    return redirect('/login')


@login_required(login_url='/login')
def menu(request):
    shelf = Menu.objects.all()
    return render(request, 'menu-list.html', {'shelf': shelf})


@login_required(login_url='/login')
def addMenu(request):
    return render(request, 'add-menu.html')


@login_required(login_url='/login')
def addMenuStore(request):
    product_name = request.POST['product_name']
    price = request.POST['price']
    product_image = request.FILES['product_image']
    category = request.POST['category']
    print(product_name, price, product_image, category)

    menu = Menu()
    menu.product_name = product_name
    menu.price = price
    menu.product_image = product_image
    menu.category = category
    menu.save()
    messages.success(request, 'Add Record Successfully.')
    return redirect('/menu')


@login_required(login_url='/login')
def menuEdit(request, menu_id):
    menu_data = Menu.objects.get(id=menu_id)
    return render(request, 'edit-menu.html', {'menu_data': menu_data})


@login_required(login_url='/login')
def updateMenu(request):
    menu_id = request.POST['id']
    product_name = request.POST['product_name']
    price = request.POST['price']
    product_image = request.FILES['product_image']
    category = request.POST['category']

    menu = Menu.objects.get(id=menu_id)
    menu.product_name = product_name
    menu.price = price
    menu.product_image = product_image
    menu.category = category
    menu.save()
    messages.success(request, 'Update Record Successfully.')
    return redirect('/menu')


@login_required(login_url='/login')
def menuDelete(request, menu_id):
    menu = Menu.objects.get(id=menu_id)
    menu.delete()
    messages.success(request, 'Record Deleted Successfully.')
    return redirect('/menu')
