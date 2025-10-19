from django.shortcuts import render, get_object_or_404
from .models import Game

def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    # Схожі ігри
    recommended = Game.objects.filter(
        genre=game.genre
    ).exclude(id=game.id)[:4]

    return render(request, 'games/game_detail.html', {
        'game': game,
        'recommended': recommended
    })
