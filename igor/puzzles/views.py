from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Puzzle


def home(request):
    """
        Landing page containing all available puzzles
    :param request:
    :return:
    """
    return render(request, 'puzzles/home.html', {'puzzles': Puzzle.objects.all()})


def solve(request, puzzle_id):
    """
        Solve a particular puzzle
    :param request:
    :param puzzle_id:
    :return:
    """
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
    return render(request, 'puzzles/solve_puzzle.html', {'puzzle': puzzle})


def playground(request):
    """

    :param request:
    :param puzzle_id
    :return:
    """
    return render(request, 'puzzles/solve_puzzle.html', {'puzzle': None})


def view_solutions(request, puzzle_id):
    """
        Submitted Solutions to an individual puzzle
    :param request:
    :param puzzle_id:
    :return:
    """
    return HttpResponse("Solutoins to puzzle No. %s" % puzzle_id)
