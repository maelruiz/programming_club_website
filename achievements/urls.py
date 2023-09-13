from django.urls import path
from . import views

urlpatterns = [
    path('achievement/create/', views.create_achievement, name='create-achievement'),
    path('achievement/update/<int:pk>/', views.update_achievement, name='update-achievement'),
    path('achievement/delete/<int:pk>/', views.delete_achievement, name='delete-achievement'),
    path('achievement/<int:pk>/', views.AchievementDetailView.as_view(), name='achievement-detail'),
    path('achievement/update/<int:pk>/', views.AchievementUpdateView.as_view(), name='achievement-update'),
    path('user/achievements/', views.user_achievements, name='user-achievements'),
    path('user/<str:username>/achievements/', views.user_profile_achievements, name='user-profile-achievements'),
]
