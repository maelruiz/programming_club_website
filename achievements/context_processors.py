from .models import Achievement

def achievements(request):
    # Fetch the achievements you want to display (e.g., latest achievements)
    latest_achievements = Achievement.objects.order_by('-date_achieved')[:5]

    # Return the achievements in a dictionary
    return {'latest_achievements': latest_achievements}
