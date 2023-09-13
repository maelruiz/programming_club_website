from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Achievement
from django.contrib.auth.models import User
from .forms import AchievementForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.views.generic import DetailView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator

@login_required
def create_achievement(request):
    if request.method == 'POST':
        form = AchievementForm(request.POST)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.user = request.user
            achievement.date_achieved = datetime.now()
            achievement.save()
            messages.success(request, 'Achievement created successfully.')
            return redirect('profile')  # Redirect to the profile page after creating achievement
    else:
        form = AchievementForm()
    
    # Retrieve the user's achievements and pass them to the template
    user_achievements = Achievement.objects.filter(user=request.user)
    # Paginate the user's achievements
    paginator = Paginator(user_achievements, 10)  # Display 10 achievements per page
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    # Retrieve all achievements for the sidebar
    all_achievements = Achievement.objects.all()
    return render(request, 'achievements/create_achievement.html', {'form': form, 'user_achievements': user_achievements, 'page': page, 'all_achievements': all_achievements})
@login_required
def update_achievement(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AchievementForm(request.POST, instance=achievement)
        if form.is_valid():
            form.save()
            messages.success(request, ' updated successfully.')
            return redirect('profile')  # Redirect to the profile page after updating achievement
    else:
        form = AchievementForm(instance=achievement)
    
    # Retrieve the user's achievements and pass them to the template
    achievements = Achievement.objects.filter(user=request.user)
    # Paginate the achievements
    paginator = Paginator(achievements, 10)  # Display 10 achievements per page
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'achievements/update_achievement.html', {'form': form, 'achievements': achievements, 'page': page})

@login_required
def delete_achievement(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk, user=request.user)
    if request.method == 'POST':
        achievement.delete()
        messages.success(request, 'Achievement deleted successfully.')
        return redirect('profile')  # Redirect to the profile page after deleting achievement
    
    # Retrieve the user's achievements and pass them to the template
    achievements = Achievement.objects.filter(user=request.user)
    # Paginate the achievements
    paginator = Paginator(achievements, 10)  # Display 10 achievements per page
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'achievements/delete_achievement.html', {'achievements': achievements, 'page': page})



class AchievementDetailView(DetailView):
    model = Achievement
    template_name = 'achievements/achievement_detail.html'  # Create this template
    context_object_name = 'achievement'

class AchievementUpdateView(SuccessMessageMixin, UpdateView):
    model = Achievement
    form_class = AchievementForm
    template_name = 'achievements/achievement_form.html'  # Create this template
    context_object_name = 'achievement'
    success_message = "Achievement updated successfully"

    def get_success_url(self):
        return reverse('achievement-detail', kwargs={'pk': self.object.pk})
    
@login_required
def user_achievements(request):
    user_achievements = Achievement.objects.filter(user=request.user)
    paginator = Paginator(user_achievements, 10)  # Display 10 achievements per page
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'achievements/user_achievements.html', {'user_achievements': user_achievements, 'page': page})

# View to display achievements for a specific user (publicly accessible)
def user_profile_achievements(request, username):
    user = get_object_or_404(User, username=username)
    user_achievements = Achievement.objects.filter(user=user)
    paginator = Paginator(user_achievements, 10)  # Display 10 achievements per page
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'achievements/user_profile_achievements.html', {'user_achievements': user_achievements, 'page': page})