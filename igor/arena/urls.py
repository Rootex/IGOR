from django.urls import path
from . import views


urlpatterns = [
    # landing: /arena/
    path('', views.arena, name='arena'),
]
