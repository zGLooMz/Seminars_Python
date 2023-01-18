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
        print('Жребий определил, что первым начинает игрок .')
        player_one()
    else:
        print('Жребий определил, что первым начинает бот.')
        bot()


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
        bot()
    else:
        print(f'{player1}, Вы победили!')


def bot():
    global total_candy
    global player2
    global bot_take
    bot_take = total_candy % 29 if total_candy %29 != 0 else random.randint(1, 28)
    total_candy -= bot_take
    print (f'Бот взял {bot_take} конфет.')
    if total_candy > 0:
        player_one()
    else:
        print('Бот победил!')


total_candy = 220

print(the_task)

player1 = input('Игрок, как Ваше имя?\n')


toss_up()
