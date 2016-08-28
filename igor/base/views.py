from django.shortcuts import render
from .forms import SignUpForm


def index(request):
    """

    :param request:
    :return:
    """
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = "John Doe"
        instance.save()
    context = {
        'form': form,
    }
    return render(request, 'base/index.html', context)
