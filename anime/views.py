#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import context
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .anime_utils import utils

# Create your views here.


def index(request):
    return HttpResponse("Hello World")


@login_required
def all(request):
    all_animes = utils.get_all_anime_names()
    return render(request, 'anime/all_animes.html', {'message' : all_animes})


@login_required
def anime_details(request, anime_title):
    anime_infos = sorted(utils.get_all_info_by_anime_name(anime_title), key=lambda x: float(x[1]))
    return render(request, 'anime/anime_infos.html', {'message' : anime_infos})













