from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SubscribeForm, CustomUserCreationForm, LoginForm


def index(request):
    """

    :param request:
    :return:
    """
    form = SubscribeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'form': form,
    }
    return render(request, 'base/index.html', context)


def register(request):
    """
    Registration view
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'base/register.html', context)


def user_login(request):
    """
    Login view
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next', 'home')
                return redirect(next_page)
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    context = {'form': form}
    return render(request, 'base/login.html', context)


def user_logout(request):
    """
    Logout view
    :param request:
    :return:
    """
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('index')


@login_required
def dashboard(request):
    """
    User dashboard showing progress
    :param request:
    :return:
    """
    from puzzles.models import Puzzle, UserProgress
    
    # Get all puzzles and user progress
    puzzles = Puzzle.objects.all()
    user_progress = UserProgress.objects.filter(user=request.user)
    
    # Create progress dict for easy lookup
    progress_dict = {up.puzzle_id: up for up in user_progress}
    
    # Combine puzzle and progress data
    puzzle_data = []
    for puzzle in puzzles:
        progress = progress_dict.get(puzzle.id)
        puzzle_data.append({
            'puzzle': puzzle,
            'progress': progress,
            'is_solved': progress.is_solved if progress else False,
            'attempts': progress.attempts if progress else 0,
            'best_score': progress.best_score if progress else 0,
        })
    
    # Calculate statistics
    total_puzzles = len(puzzles)
    solved_puzzles = len([p for p in puzzle_data if p['is_solved']])
    total_attempts = sum(p['attempts'] for p in puzzle_data)
    
    context = {
        'puzzle_data': puzzle_data,
        'total_puzzles': total_puzzles,
        'solved_puzzles': solved_puzzles,
        'total_attempts': total_attempts,
        'completion_rate': (solved_puzzles / total_puzzles * 100) if total_puzzles > 0 else 0,
    }
    return render(request, 'base/dashboard.html', context)


def about(request):
    """

    :param request: 
    :return: 
    """
    context = {}
    return render(request, 'base/about.html', context)
