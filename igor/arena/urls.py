from django.conf.urls import url
from . import views


urlpatterns = [
    # landing: /puzzles/
    url(r'^', views.arena, name='arena'),
]
