# coding=utf-8
from django.urls import path
from . import views


urlpatterns = [
    # landing: /puzzles/
    path('', views.home, name='home'),
    # ex: /puzzles/5/
    path('playground/', views.playground, name='playground'),
    path('solve/<int:puzzle_id>/', views.solve, name='solve'),
    # Submit solution for validation
    path('submit/<int:puzzle_id>/', views.submit_solution, name='submit_solution'),
    # ex: /puzzle/5/solutions/
    path('<int:puzzle_id>/solutions/', views.view_solutions, name='solutions')
]
