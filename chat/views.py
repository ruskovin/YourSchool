from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pages.models import User as Student
from pages.models import ClassRoom
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'chat/index.html')


@login_required
def room(request, room_name):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Anonymous"
    
    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username})
