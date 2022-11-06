import sqlite3, bcrypt


def password_check(password):
    if len(password) < 8 or len(password) > 20 or password.lower() == password \
            or any(map(str.isdigit, password)) is False \
            or any(char in ".,:;!_*-+()/#¤%&)" for char in password) is False \
            or any(char.lower() in "йцукенгшщзхъфывапролджэячсмитьбюё" for char in password) is True:
        return False
    return True

def login_check(login):
    if len(login) < 6 or len(login) > 20 \
            or any(char.lower() in "йцукенгшщзхъ фывапролджэячсмитьбюё!@#№;$%:^&*()=+[]{}'\"<>?+*/|"
                   for char in login) is True or login[0].lower() not in 'qwertyuiopasdfghjklzxcvbnm' \
            or login[-1] == '.':
        return False
    return True

# Метод нахождения id пользователя в БД в таблице Аккаутны
def search_id(data):
    con = sqlite3.connect('База данных проекта.db')
    cur = con.cursor()
    search = cur.execute(f"""SELECT id, login FROM Аккаунты""").fetchall()
    for i in search:
        if bcrypt.checkpw(data.encode(), i[1]) is True:
            return i[0]

# проверка данных для добавления в продукты
def proverka_name(data):
    if data == '':
        return False
    if any(char.lower() in "qwertyuiopasdfghjklzxcvbnm\t~\"/*-[]{}\'<>.,?/`!@#№$;%:^&*()_-=+1234567890"
           for char in data):
        return False
    if data.capitalize() != data:
        return False
    return True

# метод проверки инф для продуктов
def proverka_inf(data):
    try:
        if data == '':
            return False
        if all(char.lower() in "1234567890,." for char in data.split()[0]) is False:
            return False
        if data.split()[1].strip('\t') != 'ккал' and data.split()[1].strip('\t') != 'г' \
                and data.split()[1].strip('\t') != 'кКал':
            return False
        return True
    except:
        return False

# поиск совпадений в логинах
def search_coincidence(login):
    con = sqlite3.connect('База данных проекта.db')
    cur = con.cursor()
    search = cur.execute(f"""SELECT id, login FROM Аккаунты""").fetchall()
    for i in search:
        if bcrypt.checkpw(login.encode(), i[1]) is True:
            print([][1])