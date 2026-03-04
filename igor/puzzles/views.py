from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import json
from .models import Puzzle, UserProgress
from .code_runner import CodeRunner


def home(request):
    """
        Landing page containing all available puzzles
    :param request:
    :return:
    """
    puzzles = Puzzle.objects.all()
    puzzle_data = []
    
    if request.user.is_authenticated:
        # Get user progress for each puzzle
        user_progress = UserProgress.objects.filter(user=request.user)
        progress_dict = {up.puzzle_id: up for up in user_progress}
        
        for puzzle in puzzles:
            progress = progress_dict.get(puzzle.id)
            puzzle_data.append({
                'puzzle': puzzle,
                'is_solved': progress.is_solved if progress else False,
                'attempts': progress.attempts if progress else 0,
            })
    else:
        for puzzle in puzzles:
            puzzle_data.append({
                'puzzle': puzzle,
                'is_solved': False,
                'attempts': 0,
            })
    
    return render(request, 'puzzles/home.html', {'puzzle_data': puzzle_data})


def solve(request, puzzle_id):
    """
        Solve a particular puzzle
    :param request:
    :param puzzle_id:
    :return:
    """
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
    
    # Get or create user progress if user is logged in
    user_progress = None
    saved_solution = puzzle.function_template
    
    if request.user.is_authenticated:
        user_progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            puzzle=puzzle
        )
        
        # If user has solved the puzzle, load their solution for review
        if user_progress.is_solved and user_progress.solution_code:
            saved_solution = user_progress.solution_code
    
    return render(request, 'puzzles/solve_puzzle.html', {
        'puzzle': puzzle,
        'function_template': saved_solution,
        'instructions': puzzle.instructions,
        'user_progress': user_progress,
        'is_review': user_progress.is_solved if user_progress else False,
    })


def playground(request):
    """

    :param request:
    :param puzzle_id
    :return:
    """
    return render(request, 'puzzles/solve_puzzle.html', {'puzzle': None})


def view_solutions(request, puzzle_id):
    """
        Submitted Solutions to an individual puzzle
    :param request:
    :param puzzle_id:
    :return:
    """
    return HttpResponse("Solutions to puzzle No. %s" % puzzle_id)


@csrf_exempt
@require_POST
def submit_solution(request, puzzle_id):
    """
        Submit and validate a solution for a puzzle
    :param request:
    :param puzzle_id:
    :return: JSON response with validation results
    """
    try:
        puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
        
        # Get submitted code
        data = json.loads(request.body)
        code = data.get('code', '')
        
        if not code.strip():
            return JsonResponse({
                'success': False,
                'error': 'No code submitted'
            })
        
        # Get test cases
        test_cases = puzzle.get_test_cases()
        
        # Execute code
        results = CodeRunner.execute_code(code, test_cases)
        
        # Update user progress if user is logged in
        if request.user.is_authenticated:
            user_progress, created = UserProgress.objects.get_or_create(
                user=request.user,
                puzzle=puzzle
            )
            
            # Update progress
            user_progress.attempts += 1
            score = int((results['passed_tests'] / results['total_tests']) * 100) if results['total_tests'] > 0 else 0
            user_progress.best_score = max(user_progress.best_score, score)
            
            # Mark as solved if all tests pass
            if results['success'] and not user_progress.is_solved:
                user_progress.is_solved = True
                user_progress.solved_at = timezone.now()
                user_progress.solution_code = code
                results['first_solve'] = True
            
            user_progress.save()
            
            # Add progress info to results
            results['attempts'] = user_progress.attempts
            results['best_score'] = user_progress.best_score
            results['is_solved'] = user_progress.is_solved
        
        return JsonResponse(results)
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })
