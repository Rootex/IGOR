#!/usr/bin/env python
import os
import sys
import django

# Setup Django environment
sys.path.append('/home/plaix/dev/IGOR/igor')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'igor.settings')
django.setup()

from puzzles.models import Puzzle

# Create sample puzzles
puzzles_data = [
    {
        'name': 'Two Sum',
        'text': 'Find two numbers in array that add up to target. Return their indices. Example: [2,7,11,15] target=9 → [0,1]'
    },
    {
        'name': 'FizzBuzz',
        'text': 'Print 1-100. Replace multiples of 3 with "Fizz", 5 with "Buzz", both with "FizzBuzz".'
    },
    {
        'name': 'Palindrome Check',
        'text': 'Check if string reads same forwards and backwards. "racecar" → True, "hello" → False.'
    },
    {
        'name': 'Fibonacci Sequence',
        'text': 'Return nth Fibonacci number. Sequence: 0,1,1,2,3,5,8... fib(6) = 8.'
    },
    {
        'name': 'Binary Search',
        'text': 'Find target in sorted array using binary search. Return index or -1. O(log n) complexity.'
    }
]

print("Creating sample puzzles...")

for puzzle_data in puzzles_data:
    puzzle, created = Puzzle.objects.get_or_create(
        name=puzzle_data['name'],
        defaults={'text': puzzle_data['text']}
    )
    if created:
        print(f"✓ Created puzzle: {puzzle.name}")
    else:
        print(f"- Puzzle already exists: {puzzle.name}")

print(f"\nTotal puzzles in database: {Puzzle.objects.count()}")