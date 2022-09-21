from django.shortcuts import render
from mywatchlist.models import mywatchlistItem
from django.http import HttpResponse
from django.core import serializers

list_mywatchlist = mywatchlistItem.objects.all()
# TODO: Create your views here.
def show_watchlist(request):
    return render(request, "mywatchlist1.html")

def show_watched(request):
    list_mywatchlist = mywatchlistItem.objects.all() 
    movie_sum = list_mywatchlist.count()
    
    nonton = 0
    for movie in list_mywatchlist:
        if (movie.watched): 
            nonton += 1

    if 2*nonton > movie_sum : 
        result = "Selamat, kamu sudah banyak menonton!"
    else : 
        result = "Wah, kamu masih sedikit menonton!"   

    context = {
        'list_mywatchlist': list_mywatchlist,
        'nama': 'Nyoo Steven',
        'npm' : '2106630050',
        'result': result
    }
    return render(request, "mywatchlist.html", context)

def show_json(request):
    list_mywatchlist = mywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", list_mywatchlist), content_type="application/json")

def show_xml(request):
    list_mywatchlist = mywatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", list_mywatchlist), content_type="application/xml")

def show_json_by_id(request, id):
    list_mywatchlist = mywatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", list_mywatchlist), content_type="application/json")

def show_xml_by_id(request, id):
    list_mywatchlist = mywatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", list_mywatchlist), content_type="application/xml")