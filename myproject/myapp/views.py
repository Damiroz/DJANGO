from .models import CustomUser, Game, Playtime

def user_list():
    users = CustomUser.objects.select_related('playtime').all()

    for user in users:
        print(f"Full Name: {user.full_name},  Game: {user.Game.title if user.Game else 'None'}")

    games = Game.objects.all()

    for game in games:
        print(f"Game: {game.title}, Developer: {game.developer.full_name}")

    playtimes = Playtime.objects.select_related('user', 'game').all()

    for playtime in playtimes:
        print(f"{playtime.user.full_name} played {playtime.game.title} for {playtime.hours_played} hours")
