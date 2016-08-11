from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Puzzle


def home(request):
    return render_to_response('puzzles/home.html', {'puzzles': Puzzle.objects.all()})
