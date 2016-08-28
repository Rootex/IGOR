# coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    # landing: /puzzles/
    url(r'^puzzles/', views.home, name='home'),
    url(r'^arena/', views.arena, name='arena'),
    # ex: /puzzles/5/
    url(r'^solve/(?P<puzzle_id>[0-9]+)/$', views.solve, name='solve'),
    # ex: /puzzle/5/solutions/
    url(r'^(?P<puzzle_id>[0-9]+)/solutions/$', views.view_solutions, name='solutions')
]
