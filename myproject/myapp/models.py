from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):

    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



class Game(models.Model):

    title = models.CharField(max_length=255, default="Test")
    developer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=20.0)


    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.title

class Playtime(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    hours_played = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.full_name} played {self.game.title} for {self.hours_played} hours"
