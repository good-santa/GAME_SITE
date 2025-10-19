from django.shortcuts import render, get_object_or_404
from .models import Game

def game_list(request):
    query = request.GET.get('q', '').strip()

    games = Game.objects.all()
    if query:
        games = games.filter(title__icontains=query)

    context = {
        'games': games,
        'query': query,
    }

    return render(request, 'games/game_list.html', context)


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
