from django.shortcuts import render

# Create your views here.


def arena(request):
    """

    :param request:
    :return:
    """
    template = "arena/arena.html"
    return render(request, template, {})
