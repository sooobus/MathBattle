from random import randint

from multi_elo import EloPlayer, calc_new_elos

# генерация рандомных игркоов
elo_players = [EloPlayer(place=place, elo=randint(1200, 1800))
               for place in range(1, 5)]
for place, player in enumerate(elo_players, start=1):
    print('{}: {}'.format(place, player.elo))

# Создание коэффициента рейтинга
k = 16

# расчёт новых ЭЛО показателей
new_elos = calc_new_elos(elo_players, k)

for place, new_elo in enumerate(new_elos, start=1):
    print('{}: {}'.format(place, new_elo))