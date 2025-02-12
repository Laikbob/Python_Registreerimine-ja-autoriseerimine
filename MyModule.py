import random
import string

usernames = []
passwords = []

def generate_psword():
    """Генерация случайного пароля."""
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()

    all_chars = str0 + str1 + str2 + str3
    ls = list(all_chars)
    random.shuffle(ls)

    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([random.choice(ls) for _ in range(12)])

    return psword

def is_simple_password(password):
    return len(password) >= 6

def register_user(username, password):
    if username in usernames:
        return False  # Логин уже занят
    else:
        if is_simple_password(password):
            usernames.append(username)
            passwords.append(password)
            return True
        else:
            return False  # Пароль не соответствует требованиям

def authenticate_user(username, password):
    if username in usernames and passwords[usernames.index(username)] == password:
        return True
    else:
        return False

def change_password(username, new_password):
    if username in usernames and is_simple_password(new_password):
        passwords[usernames.index(username)] = new_password
        return True
    else:
        return False 

def reset_password(username):
    if username in usernames:
        new_password = generate_psword()
        passwords[usernames.index(username)] = new_password
        return new_password
    else:
        return None  # Пользователь не найден
