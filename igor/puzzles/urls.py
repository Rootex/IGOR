# coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    # landing: /puzzles/
    url(r'^$', views.home, name='home'),
    # ex: /puzzles/5/
    url(r'^playground/', views.playground, name='playground'),
    url(r'^solve/(?P<puzzle_id>[0-9]+)/$', views.solve, name='solve'),
    # ex: /puzzle/5/solutions/
    url(r'^(?P<puzzle_id>[0-9]+)/solutions/$', views.view_solutions, name='solutions')
]
