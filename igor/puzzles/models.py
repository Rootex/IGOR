from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import json


class Puzzle(models.Model):
    """
        Puzzle model: defines puzzles and their properties. Name and description as text.
    """
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    
    # Function template that users should implement
    function_template = models.TextField(default="def solution():\n    pass")
    
    # Test cases stored as JSON
    test_cases = models.TextField(default="[]")
    
    # Instructions for what the function should do
    instructions = models.TextField(default="")

    def __str__(self):
        return self.name
    
    def get_test_cases(self):
        """Parse test cases from JSON"""
        try:
            return json.loads(self.test_cases)
        except (json.JSONDecodeError, ValueError):
            return []
    
    def set_test_cases(self, test_cases_list):
        """Store test cases as JSON"""
        self.test_cases = json.dumps(test_cases_list)


class Solution(models.Model):
    """
        Solution model: Defines the solution that a user give associated to a puzzle.
    """
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    solution = models.CharField(max_length=200)

    def __str__(self):
        return "Puzzles: {0}\nSolution: {1}".format(self.puzzle, self.solution)


class UserProgress(models.Model):
    """
        Track user progress on puzzles
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    is_solved = models.BooleanField(default=False)
    solution_code = models.TextField(blank=True)
    solved_at = models.DateTimeField(null=True, blank=True)
    attempts = models.IntegerField(default=0)
    best_score = models.IntegerField(default=0)  # percentage of tests passed
    
    class Meta:
        unique_together = ('user', 'puzzle')
    
    def __str__(self):
        status = "✓" if self.is_solved else "○"
        return f"{status} {self.user.username} - {self.puzzle.name}"
