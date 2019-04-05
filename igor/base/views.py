from django.shortcuts import render
from .forms import SubscribeForm


def index(request):
    """

    :param request:
    :return:
    """
    form = SubscribeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'form': form,
    }
    return render(request, 'base/index.html', context)


def register(request):
    """
    Registration view
    :param request:
    :return:
    """
    context = {}
    return render(request, 'base/register.html', context)


def about(request):
    """

    :param request: 
    :return: 
    """
    context = {}
    return render(request, 'base/about.html', context)
