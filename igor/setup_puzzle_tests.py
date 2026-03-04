#!/usr/bin/env python
import os
import sys
import django

# Setup Django environment
sys.path.append('/home/plaix/dev/IGOR/igor')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'igor.settings')
django.setup()

from puzzles.models import Puzzle

def setup_two_sum():
    """Setup Two Sum puzzle with test cases"""
    try:
        puzzle = Puzzle.objects.get(name='Two Sum')
        puzzle.function_template = '''def solution(nums, target):
    # Write your solution here
    # Return a list of two indices that add up to target
    pass'''
        
        puzzle.instructions = '''Implement a function that finds two numbers in the array that add up to the target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Your function should return the indices of the two numbers.'''
        
        test_cases = [
            {
                'input': [[2, 7, 11, 15], 9],
                'expected': [0, 1],
                'description': 'Basic case: [2,7,11,15], target=9'
            },
            {
                'input': [[3, 2, 4], 6],
                'expected': [1, 2],
                'description': 'Different indices: [3,2,4], target=6'
            },
            {
                'input': [[3, 3], 6],
                'expected': [0, 1],
                'description': 'Same values: [3,3], target=6'
            }
        ]
        puzzle.set_test_cases(test_cases)
        puzzle.save()
        print("✓ Updated Two Sum puzzle")
    except Puzzle.DoesNotExist:
        print("- Two Sum puzzle not found")

def setup_fizzbuzz():
    """Setup FizzBuzz puzzle with test cases"""
    try:
        puzzle = Puzzle.objects.get(name='FizzBuzz')
        puzzle.function_template = '''def solution():
    # Return a list of strings from 1 to 100
    # Replace multiples of 3 with "Fizz", 5 with "Buzz", both with "FizzBuzz"
    result = []
    # Your code here
    return result'''
        
        puzzle.instructions = '''Write a function that returns a list representing FizzBuzz from 1 to 100.
- Numbers divisible by 3 should be "Fizz"
- Numbers divisible by 5 should be "Buzz"  
- Numbers divisible by both 3 and 5 should be "FizzBuzz"
- All other numbers should be their string representation'''
        
        # Generate expected FizzBuzz result
        expected = []
        for i in range(1, 101):
            if i % 15 == 0:
                expected.append("FizzBuzz")
            elif i % 3 == 0:
                expected.append("Fizz")
            elif i % 5 == 0:
                expected.append("Buzz")
            else:
                expected.append(str(i))
        
        test_cases = [
            {
                'input': [],
                'expected': expected,
                'description': 'Complete FizzBuzz 1-100'
            }
        ]
        puzzle.set_test_cases(test_cases)
        puzzle.save()
        print("✓ Updated FizzBuzz puzzle")
    except Puzzle.DoesNotExist:
        print("- FizzBuzz puzzle not found")

def setup_palindrome():
    """Setup Palindrome puzzle with test cases"""
    try:
        puzzle = Puzzle.objects.get(name='Palindrome Check')
        puzzle.function_template = '''def solution(s):
    # Check if string reads the same forwards and backwards
    # Return True if palindrome, False otherwise
    pass'''
        
        puzzle.instructions = '''Write a function that checks if a string is a palindrome.
A palindrome reads the same forward and backward.
Ignore case, spaces, and punctuation for comparison.'''
        
        test_cases = [
            {
                'input': 'racecar',
                'expected': True,
                'description': 'Simple palindrome: "racecar"'
            },
            {
                'input': 'hello',
                'expected': False,
                'description': 'Not palindrome: "hello"'
            },
            {
                'input': 'A man a plan a canal Panama',
                'expected': True,
                'description': 'Complex palindrome with spaces'
            },
            {
                'input': 'race a car',
                'expected': False,
                'description': 'Not palindrome with spaces'
            }
        ]
        puzzle.set_test_cases(test_cases)
        puzzle.save()
        print("✓ Updated Palindrome Check puzzle")
    except Puzzle.DoesNotExist:
        print("- Palindrome Check puzzle not found")

def setup_fibonacci():
    """Setup Fibonacci puzzle with test cases"""
    try:
        puzzle = Puzzle.objects.get(name='Fibonacci Sequence')
        puzzle.function_template = '''def solution(n):
    # Return the nth Fibonacci number
    # Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    pass'''
        
        puzzle.instructions = '''Write a function that returns the nth number in the Fibonacci sequence.
The sequence starts with 0, 1, and each subsequent number is the sum of the previous two.
F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)'''
        
        test_cases = [
            {
                'input': 0,
                'expected': 0,
                'description': 'F(0) = 0'
            },
            {
                'input': 1,
                'expected': 1,
                'description': 'F(1) = 1'
            },
            {
                'input': 6,
                'expected': 8,
                'description': 'F(6) = 8'
            },
            {
                'input': 10,
                'expected': 55,
                'description': 'F(10) = 55'
            }
        ]
        puzzle.set_test_cases(test_cases)
        puzzle.save()
        print("✓ Updated Fibonacci Sequence puzzle")
    except Puzzle.DoesNotExist:
        print("- Fibonacci Sequence puzzle not found")

def setup_binary_search():
    """Setup Binary Search puzzle with test cases"""
    try:
        puzzle = Puzzle.objects.get(name='Binary Search')
        puzzle.function_template = '''def solution(nums, target):
    # Implement binary search
    # Return index of target if found, -1 otherwise
    # nums is a sorted array
    pass'''
        
        puzzle.instructions = '''Implement binary search to find the target value in a sorted array.
Return the index of the target if found, otherwise return -1.
The algorithm must have O(log n) time complexity.'''
        
        test_cases = [
            {
                'input': [[-1, 0, 3, 5, 9, 12], 9],
                'expected': 4,
                'description': 'Target found: 9 at index 4'
            },
            {
                'input': [[-1, 0, 3, 5, 9, 12], 2],
                'expected': -1,
                'description': 'Target not found: 2'
            },
            {
                'input': [[5], 5],
                'expected': 0,
                'description': 'Single element found'
            },
            {
                'input': [[1, 2, 3, 4, 5], 1],
                'expected': 0,
                'description': 'First element'
            }
        ]
        puzzle.set_test_cases(test_cases)
        puzzle.save()
        print("✓ Updated Binary Search puzzle")
    except Puzzle.DoesNotExist:
        print("- Binary Search puzzle not found")

if __name__ == "__main__":
    print("Setting up puzzle test cases...")
    setup_two_sum()
    setup_fizzbuzz()
    setup_palindrome()
    setup_fibonacci()
    setup_binary_search()
    print("Done!")