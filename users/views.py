from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Achievement  # Import the Achievement model
from django.core.paginator import Paginator

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in, {username}')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Fetch the user's achievements
    achievements = Achievement.objects.filter(user=request.user)
    # Paginate the achievements
    paginator = Paginator(achievements, 10)  # Display 10 achievements per page
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)


    context = {
        'u_form': u_form,
        'p_form': p_form,
        'page': page,  # Pass achievements to the template
    }
    return render(request, 'users/profile.html', context)
