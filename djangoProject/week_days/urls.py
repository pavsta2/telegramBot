from django.urls import path
from . import views


urlpatterns = [
    path('todo_week/<int:day_of_week>', views.moi_dela_v_etot_den_by_number),
    path('todo_week/<day_of_week>', views.moi_dela_v_etot_den, name="number_of_day"),
    # path('monday', views.monday),
    # path('tuesday', views.tuesday),
]