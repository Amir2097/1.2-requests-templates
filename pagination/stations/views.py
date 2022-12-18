from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        list_data = [item for item in reader]
        print(list_data)

    page_number = request.GET.get("page", default=1)
    if page_number.isnumeric():
        page = int(page_number)
    else:
        page = 1
    paginator = Paginator(list_data, 10)
    page_pag = paginator.get_page(page)
    bus_stations = page_pag.object_list

    context = {
        'bus_stations': bus_stations,
        'page': page_pag,
    }
    return render(request, 'stations/index.html', context)
