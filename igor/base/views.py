from django.shortcuts import render
from .forms import SubscribeForm


def index(request):
    """

    :param request:
    :return:
    """
    form = SubscribeForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data['email'])
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = "John Doe"
        instance.save()
    context = {
        'form': form,
    }
    return render(request, 'base/index.html', context)
