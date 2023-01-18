# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

the_task = ('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n'
            'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
            'Все конфеты оппонента достаются сделавшему последний ход.\n')


def toss_up():
    toss = random.randint(1, 2)
    if toss == 1:
        print('Жребий определил, что первый игрок начинает.')
        player_one()
    else:
        print('Жребий определил, что второй игрок начинает.')
        player_two()


def player_one():
    global total_candy
    global player1
    global player_take
    print(f'{player1}, Ваш ход. На столе {total_candy} конфет.')
    player_take = int(input('Сколько конфет берете?: '))
    while player_take <= 0 or player_take > 28 or player_take > total_candy:
        player_take = int(input(
            f'Вы берете слишком много, можно взять не более 28 конфет, у нас всего {total_candy} конфет: '))
    total_candy -= player_take

    if total_candy > 0:
        player_two()
    else:
        print(f'{player1}, Вы победили!')


def player_two():
    global total_candy
    global player2
    global player_take
    print(f'{player2}, Ваш ход. На столе {total_candy} конфет.')
    player_take = int(input('Сколько конфет берете?: '))
    while player_take < 0 or player_take > 28 or player_take > total_candy:
        player_take = int(input(
            f'Вы берете слишком много, можно взять не более 28 конфет, у нас всего {total_candy} конфет: '))
    total_candy -= player_take

    if total_candy > 0:
        player_one()
    else:
        print(f'{player2}, Вы победили!')


total_candy = 2021

print(the_task)

player1 = input('Первый игрок, как Ваше имя?\n')
player2 = input('Второй игрок, как Ваше имя?\n')

toss_up()
