from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Venue, Order
import datetime


# Create your views here.
def home(request):
    context = {}
    return render(request, 'main/home.html', context)


def is_available_on(venue, date):
    results = Order.objects.filter(date=date)
    venue_names = [result.name for result in results]
    names = [venue.name for venue in venue_names]
    if venue in names:
        return False
    return True


def search(request):
    date = request.GET.get('date')
    city = request.GET.get('city')
    results = Venue.objects.filter(city=city)
    result_venues = [result.name for result in results]
    date_object = datetime.datetime.strptime(date, "%d %b %Y").date()
    final_results = []
    for idx, venue in enumerate(result_venues):
        if is_available_on(venue, date_object):
            final_results.append(results[idx])

    context = {
        'results': final_results,
        'date': date_object,
        'city': city
    }
    return render(request, 'main/search_results.html', context)


def profile(request):
    return HttpResponse("WELCOME TO PROFILE")


def venue_detail(request, venue_name):
    results = 
    return render(request, 'main/venue_details.html', context)
