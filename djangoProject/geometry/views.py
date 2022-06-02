from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {width * height}')

def get_rectangle_area_redirect(request, width: int, height: int):
    return HttpResponseRedirect(f'http://127.0.0.1:8000/calculate_geometry/rectangle/{width}/{height}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата со стороной {width} равна {width ** 2}')

def get_square_area_str(request, width: str):
    return HttpResponse(f'Сторона квадрата {width} должна задаваться только в цифрах')



def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {3.14 * radius ** 2}')
