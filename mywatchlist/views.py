from django.shortcuts import render
from mywatchlist.models import WatchListItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.

def show_notice(request):
    data_watchlist = WatchListItem.objects.all()
    filmWatched = 0
    for data in data_watchlist:
        if data.watched == True:
            filmWatched += 1
    if filmWatched >= (len(data_watchlist) - filmWatched):
        return "Selamat, kamu sudah banyak menonton! 🍿🥇"
    return "Wah, kamu masih sedikit menonton! 😴🥉"
    
def show_watchlist(request):
    data_watchlist = WatchListItem.objects.all()
    context = {
    'list_watchlist': data_watchlist,
    'nama': 'Anindya Lokeswara',
    'notice': show_notice(request)
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_watchlist = WatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_json(request):
    data_watchlist = WatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")

def show_json_by_id(request, id):
    data_watchlist = WatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")

def show_xml_by_id(request, id):
    data = data_watchlist = WatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")