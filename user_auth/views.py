from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.template import context
from django.http import HttpResponse

"""
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)

    else:

"""



"""

def index(request):
    return HttpResponse("Hello World")


def all(request):
    all_animes = utils.get_all_anime_names()
    return render(request, 'anime/all_animes.html', {'message' : all_animes})


def anime_details(request, anime_title):
    anime_infos = sorted(utils.get_all_info_by_anime_name(anime_title), key=lambda x: float(x[1]))
    return render(request, 'anime/anime_infos.html', {'message' : anime_infos})


"""

















