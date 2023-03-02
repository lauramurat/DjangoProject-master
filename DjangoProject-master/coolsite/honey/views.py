from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect
from .models import *

menu = [
    {'title': "Біз жайлы", 'url_name':'about'},
    {'title': "Контактілер", 'url_name': 'contact'},
    {'title': "Блог", 'url_name': 'blog'},
    {'title': "Кіру", 'url_name': 'login'},
    {'title': "Тіркелу", 'url_name': 'register'}
]



def index(request):
    posts = Product.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title':'Basty bet',
        'cat_selected':0,
    }
    return render(request, 'honey/index.html', context=context)

def about(request):
    return render(request, 'honey/about.html', {'menu': menu, 'title': 'Біз жайлы'})

def contact(request):
    return HttpResponse("Keri bailanys")

def show_post(request, post_id):
    return HttpResponse(f"postty korsetu id = {post_id}")

def show_category(request, cat_id):
    posts = Product.objects.filter(cat_id=cat_id)
    # cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()


    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Basty bet',
        'cat_selected': cat_id,
    }
    return render(request, 'honey/index.html', context=context)

def blog(request):
    return HttpResponse("Blog")

def login(request):
    return HttpResponse("Avtorisaviya")

def register(request):
    return HttpResponse("Tirkelu")


def categories(request,category):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>all categories =) </h1><p>{category}</p>")

def archive(request,year):
    if int(year) > 2023:
        raise Http404()
    elif int(year) == 2021:
        raise PermissionDenied
    elif int(year) == 2004:
        raise BadRequest()
    return HttpResponse(f"<h1>archives =) </h1><p>{year}</p>")
def not_found(request, exception):
    return HttpResponseNotFound('<h1> 404 </h1> <h2> Stranitsa ne naidena! </h2> ')
def closed_access(request, exception):
    return HttpResponseNotFound('<h1>Dostup zakryt!</h1>')
def bad_request(request, exception):
    return HttpResponseBadRequest("<h1>Nevozmozhno obnovit' zapros!</h1>")
def server_error(request):
    return HttpResponseServerError('<h1> Oshibka servera! </h1>')



