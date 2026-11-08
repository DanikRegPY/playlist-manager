
def ask_nums(songs):
    while True:
        try:
            number = int(input("Номер: "))
        except ValueError:
            print("Нужно ввести число")
            continue
        if not 1 <= number <= len(songs):
            print("Не то число")
            continue
        return number


def remove(songs):
    if not songs:
        print("Пусто")
        return
    show(songs)
    number = ask_nums(songs)
    removed = songs.pop(number - 1)
    print(f"Удалено: {removed}")


def show(songs):
    print(f"Песни: {len(songs)}")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song}")


def add(songs, title):
    songs.append(title)


def main():
    playlist = []
    while True:
        print("1 - Добавить")
        print("2 - Показать")
        print("3 - Удалить")
        print("4 - Выйти")
        choice = input("Выбор: ")
        if choice == "1":
            name = input("Песня: ")
            add(playlist, name)
        elif choice == "2":
            show(playlist)
        elif choice == "3":
            remove(playlist)
        elif choice == "4":
            break
        else:
            print("Нет такого выбора")

if __name__ == "__main__":
    main()