from django.contrib import admin
from .models import Puzzle
from .models import SignUp
from .forms import SignUpForm


class SignUpAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'timestamp', 'updated')
    form = SignUpForm
    # class Meta:
    #     model = SignUp


class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    class Meta:
        model = Puzzle

admin.site.register(SignUp)
admin.site.register(Puzzle)
