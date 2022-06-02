from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


# def monday(request):
#     return HttpResponse("9:00 Подъем, "
#                         "22:00 Спать")
#
#
# def tuesday(request):
#     return HttpResponse("8:00 Подъем, "
#                         "22:00 Спать")

day = {
        'monday': 'понедельник день тяжелый',
        'tuesday': 'вторник',
        'thursday': 'среда',
        'wednesday': 'четверг',
        'friday': 'пятница',
        'saturday': 'суббота',
        'sunday': "воскресенье",
    }

def moi_dela_v_etot_den(request, day_of_week:str):
    if day_of_week.lower() in day:
        return HttpResponse(day[day_of_week.lower()])
    else:
        return HttpResponse("нет такого дня")


def moi_dela_v_etot_den_by_number(request, day_of_week: int):
    list_days = list(day.keys())
    if 7 >= day_of_week >= 1:
        red_url = reverse("number_of_day", args=[list_days[day_of_week-1]])
        return HttpResponseRedirect(red_url)
    else:
        return HttpResponseNotFound(f"нет такого дня - {day_of_week}")
