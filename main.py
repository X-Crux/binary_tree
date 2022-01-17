import sys
from tree import Tree


def fill_demo():
    # catalog.insert("Doctor Dulitle, 1995", "300 руб/день")
    # catalog.insert("Terminator 1, 1991", "280 руб/день")
    # catalog.insert("Terminator 2, 1996", "310 руб/день")
    # catalog.insert("Terminator 3, 1998", "330 руб/день")
    # catalog.insert("Trip, 2003", "300 руб/день")
    # catalog.insert("Breaking Bad, 2001", "420 руб/день")
    # catalog.insert("Asus, 2001", "100 руб/день")
    # catalog.insert("Battle, 2005", "210 руб/день")
    # catalog.insert("Ant, 1997", "250 руб/день")
    # catalog.insert("Second chance, 2010", "210 руб/день")
    # catalog.insert("Magic dreams, 2011", "270 руб/день")
    catalog.insert("10", "_10 руб/день")
    catalog.insert("11", "_11 руб/день")
    catalog.insert("7", "_7 руб/день")
    catalog.insert("2", "_2 руб/день")
    catalog.insert("8", "_8 руб/день")
    catalog.insert("14", "_14 руб/день")
    catalog.insert("16", "_16 руб/день")
    catalog.insert("12", "_12 руб/день")
    catalog.insert("5", "_5 руб/день")
    catalog.insert("13", "_13 руб/день")
    catalog.insert("4", "_4 руб/день")
    catalog.insert("3", "_3 руб/день")
    catalog.insert("18", "_18 руб/день")
    catalog.insert("1", "_1 руб/день")
    catalog.insert("17", "_17 руб/день")
    catalog.insert("6", "_6 руб/день")
    catalog.insert("15", "_15 руб/день")
    catalog.insert("9", "_9 руб/день")
    print("Каталог заполнен демо данными")


def func(key: str, value: str):
    return f"Название: {key}, стоимость аренды: {value}"


def to_export(key: str, value: str):
    return f"{key}|{value}\n"


def validate(command) -> bool:
    try:
        command = int(command)

        if command in range(0, 11):
            return True
        else:
            raise Exception

    except Exception:
        return False


text_menu = """Выберите пункт меню:
1. Заполнить каталог демо данными
2. Добавить DVD в каталог
3. Удалить DVD из каталога
4. Найти DVD по названию
5. Показать каталог в виде таблицы
6. Показать весь каталог DVD (infix)
7. Показать весь каталог DVD (prefix)
8. Показать весь каталог DVD (postfix)
9. Экспортировать каталог в файл
10. Импортировать каталог из файла
0. Выход"""


def menu():
    print("Электронный каталог DVD-фильмов в видео-прокате")
    while True:
        print(text_menu)
        command = input("> ")

        if not validate(command):
            print("Не верная команда")
            continue
        else:
            command = int(command)

        if command == 1:
            fill_demo()
        elif command == 2:
            name = input("Название DVD: ")
            price = input("Стоимость аренды: ")
            catalog.insert(name, price)
        elif command == 3:
            name = input("Название DVD: ")
            catalog.remove(name)
        elif command == 4:
            name = input("Название DVD: ")
            print(catalog.find(name))
        elif command == 5:
            catalog.__str__()
        elif command == 6:
            catalog.traverse_infix(func)
        elif command == 7:
            catalog.traverse_prefix(func)
        elif command == 8:
            catalog.traverse_postfix(func)
        elif command == 9:
            name = input("Название файла: ")
            catalog.export(name, to_export)
        elif command == 10:
            name = input("Название файла: ")
            catalog.import_file(name)
        elif command == 0:
            break


if __name__ == '__main__':
    catalog = Tree()
    menu()
    sys.exit(0)
