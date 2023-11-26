from qna import RandomFilter, InverseFilter, CMYK
import os
from PIL import Image



My_filters = {
    "1": {"description": "Настоящее искусство",
          "Class": RandomFilter(),
          },
    "2": {"description": "Инверсия",
          "Class": InverseFilter(),
          },
    "3": {"description": "Черно-белая картинка с белыми.",
          "Class": CMYK(),
          }
}


def get_and_validation_path():
    path = input("Вставьте ссылку на фото-файл: \n")
    while not os.path.exists(path):
        print("Введите существующий файл.")
        path = input("Вставьте ссылку на фото-файл: \n")
    return path


def print_menu_filters():
    for i, k in enumerate(My_filters.values()):
        print(f"{i + 1}: {k["description"]}")


def get_and_validation_choice_filters(filter_input):
    choose_filter = My_filters.get(filter_input, False)
    while not choose_filter:
        filter_input = input("Введите корректный номер фильтра:\n")
        choose_filter = My_filters.get(filter_input, False)
    return choose_filter


def validation_da_net(input_):
    while input_ != "да" and input_ != "нет":
        input_ = input("ВВЕДИТЕ ДА ИЛИ НЕТ: ").lower()
    return input_.lower()


def main():
    print("Приветствую в фоторедакторе")
    end = False
    while not end:
        print_menu_filters()
        choice_filter = input("Выберите номер фильтра:\n")
        choice = get_and_validation_choice_filters(choice_filter)
        choice_next = input("Применить выбранный фильтр?\n1) Да\n2) Нет\nВаш выбор: ").lower()
        choice_next = validation_da_net(choice_next)
        if choice_next == "да":
            path_user = get_and_validation_path()
            img = Image.open(path_user).convert("RGB")
            img = choice["Class"].apply_to_image(img)
            final_path = input("Введите путь файла,в который хотите сохранть обработанную картинку:\n")
            img.save(final_path)
            too_many = input("Хотите еще раз:\n1) Да\n2) Нет\nВаш выбор: ").lower()
            too_many = validation_da_net(too_many)
            if too_many == "нет":
                print("ЧАО АМИГОС")
                end = True
        if choice_next == "нет":
            print("Выбирай другое")


if __name__ == '__main__':
    main()

