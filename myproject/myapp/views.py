from django.shortcuts import render
from .models import CustomUser, Game

def user_list(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'user_list.html', context)
