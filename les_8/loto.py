import random
import json
import time
import os


class LotoCard:
    def __init__(self, name, computer=False):
        self.numbers_list = [i for i in range(1, 91)]
        self.name = name
        self._computer = computer
        self.numbers_of_card = []
        self.game_card = [
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
            ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        ]
        self.__make_card()

    def __make_card(self):
        index_line = 0
        while len(self.numbers_of_card) != 15:
            check_line = []
            while len(check_line) != 5:
                i = random.randint(1, 90)
                check_first = i // 10
                if i not in self.numbers_of_card and check_first not in check_line:
                    if check_first != 8 and check_first != 9:
                        self.numbers_of_card.append(i)
                        check_line.append(check_first)
                        self.game_card[index_line][check_first] = i
                    elif (check_first == 8 and 9 not in check_line) or (check_first == 9 and 8 not in check_line):
                        self.numbers_of_card.append(i)
                        check_line.append(check_first)
                        if check_first == 9:
                            self.game_card[index_line][check_first - 1] = i
                        else:
                            self.game_card[index_line][check_first] = i
            index_line += 1

    @staticmethod
    def _beautiful_style(n):
        b = str(n)
        if len(b) < 2:
            result = f' {b}'
        else:
            result = b
        return result

    def __str__(self):
        if self._computer:
            top = '-- Карточка компьютера ---'
        else:
            top = '----- Ваша карточка ------'
        return f'''
{top}
{' '.join(map(self._beautiful_style, self.game_card[0]))}
{' '.join(map(self._beautiful_style, self.game_card[1]))}
{' '.join(map(self._beautiful_style, self.game_card[2]))}
--------------------------
'''

    def lot(self, number):
        if number in self.numbers_of_card:
            for i in self.game_card:
                if number in i:
                    index = i.index(number)
                    i[index] = '--'
                    self.numbers_of_card.remove(number)


class LotoGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.numbers_list = [i for i in range(1, 91)]
        self.is_game = True
        self.winner = ''

    def game_progress(self):
        number = random.choice(self.numbers_list)
        self.numbers_list.remove(number)
        print('\n\n')
        print(f'Новый бочонок: {number} (осталось {len(self.numbers_list)})')
        print(player1)
        print(player2)
        if player1._computer:
            player1.lot(number)
        else:
            self._player_choice(number, player1, player2)
        if player2._computer:
            player2.lot(number)
        else:
            self._player_choice(number, player2, player1)

    def start(self):
        time_of_start = time.time()
        while self.is_game:
            self.game_progress()
            if len(player1.numbers_of_card) == 0:
                self.is_game = False
                self.winner = player1
            elif len(player2.numbers_of_card) == 0:
                self.is_game = False
                self.winner = player2
        game_time = round(time.time() - time_of_start, 2)
        self.end_of_game(self.winner, game_time)

    def _player_choice(self, number, player, other_player):
        while True:
            choice = input('Зачеркнуть цифру? (y/n)').lower()
            if choice == 'y':
                if number in player.numbers_of_card:
                    player.lot(number)
                else:
                    self.is_game = False
                    self.winner = other_player
                break
            elif choice == 'n':
                if number in player.numbers_of_card:
                    self.is_game = False
                    self.winner = other_player
                break
            else:
                print('Ошибка ввода')

    def end_of_game(self, winner, time):
        minuts = int(time) // 60
        seconds = round(time % 60, 2)
        print(f'Победил игрок: {winner.name}, за {minuts} минут и {seconds} секунд')
        if winner._computer:
            self.show_rating()
        else:
            self._add_rating(winner, time)

    def _add_rating(self, winner, time):
        new_data = [winner.name, time]
        if os.path.isfile('rating.json'):
            with open('rating.json', encoding='utf-8') as f:
                data_of_rating = json.load(f)
        else:
            data_of_rating = []

        data_of_rating.append(new_data)
        data_of_rating.sort(key=lambda x: x[1])

        with open('rating.json', 'w', encoding='utf-8') as f:
            json.dump(data_of_rating, f)

        self.show_rating()

    def show_rating(self):
        if os.path.isfile('rating.json'):
            with open('rating.json', encoding='utf-8') as f:
                data_of_rating = json.load(f)
            for i, line in enumerate(data_of_rating, start=1):
                print(f'{i}. {line[0]} результат {int(line[1]) // 60} минут и {round(line[1] % 60, 2)} секунд')
        else:
            print('Ещё ни кто не побеждал')
        input('Нажми ENTER для выхода')


player1 = LotoCard(input('Введите имя игрока >>>'), computer=False)
player2 = LotoCard('Computer', computer=True)

game = LotoGame(player1, player2)

game.start()
