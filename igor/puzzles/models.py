from django.db import models
from datetime import datetime


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email


class Puzzle(models.Model):
    """
        Puzzle model: defines puzzles and their properties. Name and description as text.
    """
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Solution(models.Model):
    """
        Solution model: Defines the solution that a user give associated to a puzzle.
    """
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    solution = models.CharField(max_length=200)

    def __str__(self):
        return "Puzzles: {0}\nSolution: {1}".format(self.puzzle, self.solution)