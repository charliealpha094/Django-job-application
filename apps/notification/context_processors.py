# Done by Carlos Amaral (2021/02/09)

from .models import Notification

def notifications(request):
    if request.user.is_authenticated:
        return {'notifications': request.user.notifications.filter(is_read=False)}
    else:
        return {'notifications': []}
