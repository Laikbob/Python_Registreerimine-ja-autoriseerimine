from MyModule import *
#
def main():
    while True:
        print("\nДоступные действия:")
        print("1. Регистрация")
        print("2. Авторизация")
        print("3. Изменение пароля")
        print("4. Восстановление пароля")
        print("5. Завершение работы")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            print("\nРегистрация:")
            username = input("Введите логин: ")
            password_choice = input("Создать пароль самостоятельно (1) или сгенерировать автоматически (2)? ")
            if password_choice == '1':
                password = input("Введите пароль: ")
                if is_simple_password(password):
                    if register_user(username, password):
                        print("Пользователь успешно зарегистрирован!")
                    else:
                        print("Ошибка регистрации. Логин уже существует.")
                else:
                    print("Пароль не соответствует требованиям.")
            elif password_choice == '2':
                password = generate_psword()
                if register_user(username, password):
                    print(f"Пользователь зарегистрирован! Сгенерированный пароль: {password}")
                    print("ВНИМАНИЕ: Запомните или сохраните этот пароль!")
                else:
                    print("Ошибка регистрации. Логин уже существует.")

        elif choice == '2':
            print("\nАвторизация:")
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            if authenticate_user(username, password):
                print("Авторизация успешна!")
            else:
                print("Неверный логин или пароль.")

        elif choice == '3':
            print("\nИзменение пароля:")
            username = input("Введите логин: ")
            if username in usernames:
                new_password = input("Введите новый пароль: ")
                if is_simple_password(new_password):
                    if change_password(username, new_password):
                        print("Пароль успешно изменён!")
                    else:
                        print("Ошибка изменения пароля.")
                else:
                    print("Новый пароль не соответствует требованиям.")
            else:
                print("Пользователь не найден.")

        elif choice == '4':
            print("\nВосстановление пароля:")
            username = input("Введите логин: ")
            new_password = reset_password(username)
            if new_password:
                print(f"Ваш новый пароль: {new_password}")
                print("ВНИМАНИЕ: Запомните или сохраните этот пароль!")
            else:
                print("Пользователь не найден.")

        elif choice == '5':
            print("Завершение работы программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите число от 1 до 5.")

if __name__ == "__main__":
    main()