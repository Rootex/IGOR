from django.contrib import admin
from .forms import SubscribeForm
from .models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'timestamp', 'updated')
    form = SubscribeForm
    # class Meta:
    #     model = SignUp

admin.site.register(Subscribe, SubscribeAdmin)
