from django.contrib import admin
from .models import Puzzle, Solution


class SolutionInline(admin.StackedInline):
    model = Solution
    extra = 3


class PuzzleAdmin(admin.ModelAdmin):
    search_fields = ['text']
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    fieldsets = [
        (None,  {'fields': ['name', 'text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [SolutionInline]
    class Meta:
        model = Puzzle

admin.site.register(Puzzle, PuzzleAdmin)
admin.site.register(Solution)
