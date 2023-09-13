from django.apps import AppConfig



class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

class AchievementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'achievements'