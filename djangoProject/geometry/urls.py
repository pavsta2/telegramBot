from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area),
    path('square/<int:width>', views.get_square_area),
    path('circle/<int:radius>', views.get_circle_area),
    path('square/<str:width>', views.get_square_area_str),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area_redirect),
]