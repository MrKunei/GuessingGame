from random import sample

def create_file_words():
# Создание файла и запись в него списка слов
    with open("words.txt", "w", encoding='utf-8') as f:
        f.write("python\n")
        f.write("squirrel\n")
        f.write("flask\n")
        f.write("cucumbers\n")


def formation_word_list():
# Чтение файла и выгрузка списка слов
    words_list = []
    with open("words.txt", encoding='utf-8') as f:
        for words in f:
            words_list.append(words.strip())
    return words_list


def random_word(word):
# Перемешивание букв в слове
    return ''.join(sample(word, len(word)))


def guessing_game(words_list):
# Угадайка. Проверка правильности ответа
    total_points = 0
    for word in words_list:
        word_rand = random_word(word)
        print(f"Угадайте слово:{word_rand}")
        answer = input("Введите ваш ответ: ")
        if answer == word:
            print(f"Верно! Вы получаете 10 очков.\n")
            total_points += 10
        else:
            print(f"Неверно! Верный ответ – {word}.\n")
    return total_points


def formation_statistics(name, sum_stat):
# Сбор статистики и добавление в файл
    with open("history.txt", "a", encoding='utf-8') as f:
        f.write(f"{name} {sum_stat}\n")


def show_statistics():
# Чтение файла и вывод кол-ва игр и лучший результат
    with open("history.txt", encoding='utf-8') as f:
        quantity_games = []
        max_points = []
        for items in f:
            name, points = items.strip().rsplit(" ")
            quantity_games.append(name)
            max_points.append(points)
    print(f"Всего игр сыграно:{len(quantity_games)}")
    print(f"Максимальный рекорд: {max(max_points)}")


def main():
    while True:
        start_game = input("Хотите сыграть в угадайку? (Y/N) ")
        if start_game.upper() != "Y":
            show_statistics()
            break

        create_file_words()
        name = input("Введите ваше имя: ")
        words_list = formation_word_list()
        random_word(words_list)
        sum_stat = guessing_game(words_list)
        formation_statistics(name, sum_stat)
        print("*"*20 + " GAME OVER " + "*"*20)


if __name__ == '__main__':
    main()
