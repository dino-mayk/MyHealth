import sys, webbrowser, sqlite3, os, bcrypt
from datetime import datetime
from PIL import Image
from PyQt5.QtGui import QPixmap, QPainter, QPalette, QIcon
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, \
QLabel, QStatusBar, QTableWidgetItem, QInputDialog, QFileDialog
from Functions import password_check, login_check, search_id, \
    proverka_name, proverka_inf, search_coincidence
from PyQt5.Qt import QTime


class Entrance(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("ui-файлы/Начальное меню.ui", self)
        self.setWindowTitle('Начальное меню')
        self.setFixedSize(400, 400)

        self.without_registration.clicked.connect(self.without)
        self.get_out.clicked.connect(self.go_out)
        self.registration.clicked.connect(self.registr)
        self.entrance.clicked.connect(self.login)

        self.without_registration.setStyleSheet(
            'background: rgb(0,0,255); color: '
            'rgb(255, 255, 255);border: rgb(0, 0, 255);')
        self.get_out.setStyleSheet(
            'background: rgb(0,0,255); '
            'color: rgb(255, 255, 255);border: rgb(0, 0, 255);')
        self.registration.setStyleSheet(
            'background: rgb(255,255,255); '
            'color: rgb(0, 0, 255);border: rgb(0, 0, 255);')
        self.entrance.setStyleSheet(
            'background: rgb(0,0,255); '
            'color: rgb(255, 255, 255);border: rgb(0, 0, 255);')
        self.pixmap = QPixmap('Картинки для программы\Заголовок.png')
        self.pixmap2 = QPixmap('Картинки для программы\Версия.png')
        self.label.setPixmap(self.pixmap)
        self.label_2.setPixmap(self.pixmap2)
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.blue)
        self.setPalette(palette)

    def without(self):
        valid = QMessageBox.question(
            self, 'Предупреждение',
            "Вы действительно хотите войти без регистрации? "
            "Тогда часть функций будет не доступна.",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            self.close()
            self.open_m = Main(self, " ")
            self.open_m.show()

    def go_out(self):
        QCoreApplication.instance().quit()

    def login(self):
        self.close()
        self.admission = Admission(self, "")
        self.admission.show()

    def registr(self):
        self.close()
        self.reg = Registration(self, "")
        self.reg.show()


class Main(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):

        uic.loadUi("ui-файлы/Главное меню.ui", self)
        self.setWindowTitle('Главное меню')
        self.setFixedSize(600, 600)

        self.back.clicked.connect(self.ago)
        self.settings.clicked.connect(self.customization)
        self.nutrition.clicked.connect(self.food)
        self.evidence.clicked.connect(self.facts)
        self.exercises.clicked.connect(self.work)
        self.calculator.clicked.connect(self.calculator_open)

        self.back.setStyleSheet(
            'background: rgb(255,57,41); '
            'color: rgb(0, 0, 0);border: rgb(255, 0, 0);')
        self.nutrition.setStyleSheet(
            'background: rgb(255,57,41); '
            'color: rgb(0, 0, 0);border: rgb(255, 0, 0);')
        self.calculator.setStyleSheet(
            'background: rgb(255,57,41); '
            'color: rgb(0, 0, 0);border: rgb(255, 0, 0);')
        self.exercises.setStyleSheet(
            'background: rgb(255,57,41); '
            'color: rgb(0, 0, 0);border: rgb(255, 0, 0);')
        self.settings.setStyleSheet(
            'background: rgb(255,57,41); '
            'color: rgb(0, 0, 0);border: rgb(255, 0, 0);')
        self.evidence.setStyleSheet(
            'background: rgb(255,57,41); '
            'color: rgb(0, 0, 0);border: rgb(255, 0, 0);')

        if args[-1] == ' ':
            self.exercises.hide()
            self.settings.hide()
        self.data = args[-1]

    def calculator_open(self):
        self.close()
        self.open = Calculator(self, self.data)
        self.open.show()

    def work(self):
        self.close()
        self.open = Work(self, self.data)
        self.open.show()

    def facts(self):
        webbrowser.open('https://www.adme.ru/zhizn-nauka/17-nauchno-dokazannyh-'
                    'faktov-o-zdorove-kotorye-mnogie-pochemu-'
                        'to-prodolzhayut-ignorirovat-2152065/', new=2)

    def customization(self):
        self.close()
        self.open = Settings(self, self.data)
        self.open.show()

    def food(self):
        self.close()
        self.open = Food(self, self.data)
        self.open.show()

    def ago(self):
        self.close()
        self.open = Entrance(self, "")
        self.open.show()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = QPixmap("Картинки для программы\Фон.bmp")
        painter.drawPixmap(self.rect(), pixmap)


class Admission(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):

        uic.loadUi("ui-файлы/Вход.ui", self)
        self.setWindowTitle('Вход')
        self.setFixedSize(400, 300)

        self.error = QStatusBar(self)
        self.error.move(10, 165)
        self.error.resize(500, 20)
        self.error.setStyleSheet(
            "QStatusBar{padding-left:8px;background:rgb(0,0,255);color:black;font-weight:bold;}")
        self.pixmap = QPixmap('Картинки для программы\Вход.png')
        self.pixmap1 = QPixmap('Картинки для программы\Введите логин.png')
        self.pixmap2 = QPixmap('Картинки для программы\Введите пароль.png')
        self.priv.setPixmap(self.pixmap)
        self.label_2.setPixmap(self.pixmap1)
        self.label.setPixmap(self.pixmap2)
        self.back.setStyleSheet(
            'background: rgb(0,0,255); color: rgb(255, 255, 255);border: rgb(0, 0, 255);')
        self.ok.setStyleSheet(
            'background: rgb(255,255,255); color: rgb(0, 0, 255);border: rgb(0, 0, 255);')
        self.setStyleSheet('background: rgb(0,0,255);')

        self.back.clicked.connect(self.ago)
        self.ok.clicked.connect(self.run)

        self.args = args

    def run(self):
        # поиск данных
        con = sqlite3.connect('База данных проекта.db')
        cur = con.cursor()
        result = cur.execute("""SELECT login, password FROM Аккаунты""").fetchall()
        con.close()
        # обработка данных
        for i in result:
            if bcrypt.checkpw(self.password.text().encode(), i[0]) is True:
                if bcrypt.checkpw(self.login.text().encode(), i[1]) is True:
                    self.close()
                    self.open = Main(self, f"{self.password.text()} {self.login.text()}")
                    self.open.show()
        self.error.setStyleSheet(
            "QStatusBar{padding-left:8px;background:rgb(255,57,41);color:black;font-weight:bold;}")
        self.error.showMessage('Вы ввели некорректные данные')

    def ago(self):
        self.close()
        if self.args[-1] == 'back':
            self.open = Registration(self, "")
        else:
            self.open = Entrance(self, "")
        self.open.show()


class Registration(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):

        uic.loadUi("ui-файлы/Регистрация.ui", self)
        self.setWindowTitle('Регистрация')
        self.setFixedSize(400, 200)

        self.pixmap1 = QPixmap('Картинки для программы\Введите логин.png')
        self.pixmap2 = QPixmap('Картинки для программы\Введите пароль.png')
        self.pixmap3 = QPixmap('Картинки для программы\Повторно введите пароль.png')
        self.label.setPixmap(self.pixmap1)
        self.label_2.setPixmap(self.pixmap2)
        self.label_3.setPixmap(self.pixmap3)
        self.back.setStyleSheet(
            'background: rgb(255,255,255); color: rgb(0, 0, 255);border: rgb(0, 0, 255);')
        self.ok.setStyleSheet(
            'background: rgb(0,0,255); color: rgb(255, 255, 255);border: rgb(0, 0, 255);')
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.blue)
        self.setPalette(palette)

        self.back.clicked.connect(self.ago)
        self.ok.clicked.connect(self.run)

    def ago(self):
        self.close()
        self.open = Entrance(self, "")
        self.open.show()

    def open(self):
        self.close()
        self.open = Admission(self, "")
        self.open.show()

    def run(self):
        # проверка данных на условия
        if password_check(self.password.text()) is False \
                or login_check(self.login.text()) is False:
            valid = QMessageBox.question(
                self, 'Сообщение об ошибке',
                "Пароль должен  состоять не менее чем из 8 и не более чем из 20 символов, "
                "иметь обязательно только латинские буквы всех регистров, цифры, спецсимволы. "
                "Логин должен начинаться с буквы и состоять не менее чем из 6 и не "
                "более чем из 20 символов, при создании логина можно использовать только "
                "латинские буквы, цифры, символы тире, подчеркивания и точки, логин не может "
                "заканчиваться точкой.",
                QMessageBox.Ok)
        elif self.password.text() != self.password2.text():
            valid = QMessageBox.question(
                self, 'Сообщение об ошибке', "Вы забыли повторно ввести пароль или же пароли не совпадают",
                QMessageBox.Ok)
        else:
            try:
                # поиск совпадений
                search_coincidence(self.login.text())
                # хэширование пароля и логина
                hash_login = bcrypt.hashpw(self.login.text().encode(), bcrypt.gensalt())
                hash_password = bcrypt.hashpw(self.password.text().encode(), bcrypt.gensalt())
                # добавление в БД
                con = sqlite3.connect('База данных проекта.db')
                cur = con.cursor()
                cur.execute(f"""INSERT INTO Аккаунты(login, password) VALUES(?, ?)""",
                            (hash_login, hash_password))
                con.commit()
                con.close()
                self.close()
                self.open = Admission(self, "back")
                self.open.show()
            except:
                valid = QMessageBox.question(
                    self, 'Сообщение об ошибке',
                    "Такой логин уже есть в базе. Попробуйте другой",
                    QMessageBox.Ok)


class Settings(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):

        uic.loadUi("ui-файлы/Настройки.ui", self)
        self.setWindowTitle('Настройки')
        self.setFixedSize(400, 170)

        self.ok.setStyleSheet('background: rgb(255,0,0);border: rgb(255, 0, 0);')
        self.back.setStyleSheet('background: rgb(255,0,0);border: rgb(255, 0, 0);')
        self.login_label.setStyleSheet('background: rgb(255,57,41);border: 1px solid black;')
        self.password_label.setStyleSheet('background: rgb(255,57,41);border: 1px solid black;')
        self.password2_label.setStyleSheet('background: rgb(255,57,41);border: 1px solid black;')
        self.pixmap = QPixmap('Картинки для программы\Новый логин.png')
        self.pixmap1 = QPixmap('Картинки для программы\Новый пароль.png')
        self.pixmap2 = QPixmap('Картинки для программы\Новый пароль ещё раз.png')
        self.login.setPixmap(self.pixmap)
        self.password.setPixmap(self.pixmap1)
        self.password2.setPixmap(self.pixmap2)

        self.back.clicked.connect(self.ago)
        self.ok.clicked.connect(self.run)

        self.data = args[-1]

    def run(self):
        # проверка на корректность
        if password_check(self.password_label.text()) is False \
                or login_check(self.login_label.text()) is False:
            valid = QMessageBox.question(
                self, 'Сообщение об ошибке',
                "Пароль должен  состоять не менее чем из 8 и не более чем из 20 символов, "
                "иметь обязательно только латинские буквы всех регистров, цифры, спецсимволы. "
                "Логин должен начинаться с буквы и состоять не менее чем из 6 и не "
                "более чем из 20 символов, при создании логина можно использовать только "
                "латинские буквы, цифры, символы тире, подчеркивания и точки, логин не может "
                "заканчиваться точкой.",
                QMessageBox.Ok)
        elif self.password_label.text() != self.password2_label.text():
            valid = QMessageBox.question(self, 'Сообщение об ошибке',
                                "Вы забыли повторно ввести пароль или же пароли не совпадают",
                                 QMessageBox.Ok)
        else:
            try:
                # поиск совпадений
                search_coincidence(self.login_label.text())
                # задаём переменные
                login = self.data.split()[0]
                hash_login = bcrypt.hashpw(self.login_label.text().encode(), bcrypt.gensalt())
                hash_password = bcrypt.hashpw(self.password_label.text().encode(), bcrypt.gensalt())
                # узнаём id нужного нам аккаунта на изменение
                con = sqlite3.connect('База данных проекта.db')
                cur = con.cursor()
                search = cur.execute(f"""SELECT id, login FROM Аккаунты""").fetchall()
                for i in search:
                    if bcrypt.checkpw(login.encode(), i[1]) is True:
                        id_of_l = i[0]
                # изменение
                cur.execute(f"""UPDATE Аккаунты SET login = ?, password = ? WHERE id = {id_of_l}""",
                            (hash_login, hash_password))
                self.data = f'{self.login_label.text()} {self.password_label.text()}'
                con.commit()
                con.close()
                self.ago()
            except IndexError:
                valid = QMessageBox.question(
                    self, 'Сообщение об ошибке',
                    "Такой логин уже есть в базе. Попробуйте другой",
                    QMessageBox.Ok)

    def ago(self):
        self.close()
        self.open = Main(self, self.data)
        self.open.show()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setBrush(Qt.red)
        painter.drawRect(self.rect())


class Food(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        uic.loadUi("ui-файлы/Контроль питания.ui", self)
        self.setWindowTitle('Контроль питания(сведения о продукте в 100г)')
        self.setFixedSize(720, 600)

        self.abc.addItems(['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И',
                           'Й', 'К','Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                           'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Ъ', 'Ь', 'Щ', 'Ы', 'Э', 'Ю', 'Я'])

        self.back.clicked.connect(self.ago)
        self.ok.clicked.connect(self.update_result)
        self.add.clicked.connect(self.add_new)
        self.update.clicked.connect(self.update_res)
        self.deleted.clicked.connect(self.deleted_res)

        self.ok.setStyleSheet('background: rgb(0,255,0);border: rgb(0, 255, 0);')
        self.back.setStyleSheet('background: rgb(0,255,0);border: rgb(0, 255, 0);')
        self.add.setStyleSheet('background: rgb(0,255,0);border: rgb(0, 255, 0);')
        self.abc.setStyleSheet('background: rgb(255,255,255);border: rgb(255, 255, 255);')
        self.search.setStyleSheet('background: rgb(255,255,255);border: rgb(255, 255, 255);')
        self.update.setStyleSheet('background: rgb(0,255,0);border: rgb(0, 255, 0);')
        self.deleted.setStyleSheet('background: rgb(0,255,0);border: rgb(0, 255, 0);')
        self.pixmap = QPixmap('Картинки для программы\Поиск продуктов.png')
        self.pixmap1 = QPixmap('Картинки для программы\Поиск продуктов по азбуке.png')
        self.search1.setPixmap(self.pixmap)
        self.search2.setPixmap(self.pixmap1)

        self.data = args[-1]

        self.update_result()

    def deleted_res(self):
        if len(self.result) > 0:
            number, ok_pressed = QInputDialog.getInt(
                self, "Введите номер строки", "Введите номер строки, которую хотите удалить",
                1, 1, len(self.result), 1)
            if ok_pressed:
                # удаление данных из БД
                con = sqlite3.connect('База данных проекта.db')
                cur = con.cursor()
                cur.execute(f"""DELETE FROM Продукты 
                    WHERE link = '{self.result[number - 1][0]}' and food = '{self.result[number - 1][1]}' and 
                    caloric = '{self.result[number - 1][2]}' and squirrels = '{self.result[number - 1][3]}' and 
                    fats = '{self.result[number - 1][4]}' and carbohydrates = '{self.result[number - 1][5]}'""")
                con.commit()
                con.close()
                # удаление фотографии
                if self.result[number - 1][0] != 'Картинки\без изображения.png':
                    os.remove(f'C:\Programmer\Python\PythonProjects\Проект\{self.result[number - 1][0]}')
                self.update_result()

    def update_res(self):
        if len(self.result) > 0:
            number, ok_pressed = QInputDialog.getInt(
                self, "Введите номер строки", "Введите номер строки, которую хотите изменить",
                1, 1, len(self.result), 1)
            if ok_pressed:
                self.close()
                self.open = Update_food(self, (self.data, self.search.text(), self.abc.currentText(), number))
                self.open.show()

    def add_new(self):
        self.close()
        self.open = Add_food(self, self.data)
        self.open.show()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setBrush(Qt.green)
        painter.drawRect(self.rect())

    def ago(self):
        self.close()
        self.open = Main(self, self.data)
        self.open.show()

    def update_result(self):
        # поиск данных
        con = sqlite3.connect('База данных проекта.db')
        cur = con.cursor()
        if self.search.text() != '' and self.search.text() != 'Ничего не найдено':
            self.result = cur.execute(f"""SELECT * FROM Продукты WHERE food like 
            '{self.search.text().strip().capitalize()}%'""").fetchall()
        else:
            self.result = cur.execute(f"""SELECT * FROM Продукты WHERE food like 
            '{self.abc.currentText()}%'""").fetchall()
        con.close()
        # отображение данных
        if len(self.result) == 0:
            self.search.setText('Ничего не найдено')
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)
        else:
            self.search.setText('')
            self.tableWidget.setRowCount(len(self.result))
            self.tableWidget.setColumnCount(len(self.result[0]))
            self.tableWidget.setHorizontalHeaderLabels(["Фото продукта", "Название продукта", "Калорийность",
                                                        "Белки", "Жиры", "Углеводы"])
            self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
            self.tableWidget.verticalHeader().setDefaultSectionSize(200)
            self.tableWidget.horizontalHeader().setMaximumSectionSize(200)
            self.tableWidget.verticalHeader().setMaximumSectionSize(200)
            self.tableWidget.verticalHeader().setMinimumSectionSize(200)
            self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
            for i, elem in enumerate(self.result):
                for j, val in enumerate(elem):
                    if type(val) == str and 'Картинки' in val and '.png' in val:
                        # сжатие изображения под определённый размер
                        im = Image.open(val)
                        im2 = im.resize((200, 200))
                        im2.save(val)
                        # применение изображения
                        self.label = QLabel('Типо картинка', self)
                        self.label.resize(200, 200)
                        self.pixmap = QPixmap(val)
                        self.label.setPixmap(self.pixmap)
                        self.tableWidget.setCellWidget(i, j, self.label)
                    else:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.tableWidget.resizeColumnsToContents()


class Add_food(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        uic.loadUi("ui-файлы/Добавление нового продукта.ui", self)
        self.setWindowTitle('Добавление нового продукта')
        self.setFixedSize(350, 420)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.name_image = 'Картинки\без изображения.png'
        self.pixmap = QPixmap('Картинки\без изображения.png')
        self.pixmap1 = QPixmap('Картинки для программы\Название продукта.png')
        self.pixmap2 = QPixmap('Картинки для программы\Калорийность.png')
        self.pixmap3 = QPixmap('Картинки для программы\Кол-во белков.png')
        self.pixmap4 = QPixmap('Картинки для программы\Кол-во жиров.png')
        self.pixmap5 = QPixmap('Картинки для программы\Кол-во углеводов.png')
        self.pixmap6 = QPixmap('Картинки для программы\Фото продукта.png')
        self.image_label.setPixmap(self.pixmap)
        self.label.setPixmap(self.pixmap1)
        self.label_2.setPixmap(self.pixmap2)
        self.label_3.setPixmap(self.pixmap3)
        self.label_4.setPixmap(self.pixmap4)
        self.label_5.setPixmap(self.pixmap5)
        self.label_6.setPixmap(self.pixmap6)
        self.setStyleSheet('background: rgb(255,127,39)')
        self.ok.setStyleSheet('background: rgb(255,127,39);border: rgb(255, 127, 39)')
        self.add.setStyleSheet('background: rgb(255,127,39);border: rgb(255, 127, 39)')
        self.deleted.setStyleSheet('background: rgb(255,127,39);border: rgb(255, 127, 39)')
        self.back.setStyleSheet('background: rgb(255,127,39);border: rgb(255, 127, 39)')
        self.reference.setStyleSheet('background: rgb(255,127,39);border: rgb(255, 127, 39)')

        self.back.clicked.connect(self.ago)
        self.add.clicked.connect(self.add_image)
        self.deleted.clicked.connect(self.deleted_image)
        self.ok.clicked.connect(self.add_product)
        self.reference.clicked.connect(self.open_reference)

        self.error = QStatusBar(self)
        self.error.move(10, 395)
        self.error.resize(500, 20)

        self.data = args[-1]

    def add_image(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
            link = f'Картинки\{fname.split("/")[-1]}'
            # поиск на индивидуальность картинки
            con = sqlite3.connect('База данных проекта.db')
            cur = con.cursor()
            links = cur.execute(f"""SELECT link FROM Продукты""").fetchall()
            con.close()
            # изменение links для чтения
            for i in range(len(links)):
                links[i] = links[i][0]
            # проверка
            if fname == '':
                pass
            if link in links:
                self.error.setStyleSheet(
                    "QStatusBar{padding-left:8px;background:rgb(255,0,0);color:black;font-weight:bold;}")
                self.error.showMessage('Картинка с таким же названием уже используется')
            else:
                # сжатие изображения под определённый размер
                im = Image.open(fname)
                im2 = im.resize((200, 200))
                im2.save(link)
                # удаление старой картинки
                if self.name_image != 'Картинки\без изображения.png' \
                        and self.name_image != link:
                    os.remove(self.name_image)
                # применение картинки
                self.name_image = link
                self.pixmap = QPixmap(link)
                self.image_label.setPixmap(self.pixmap)
        except:
            self.error.setStyleSheet(
                "QStatusBar{padding-left:8px;background:rgb(255,0,0);color:black;font-weight:bold;}")
            self.error.showMessage('Неподдерживаемый формат файла')

    def open_reference(self):
        valid = QMessageBox.question(
            self, 'Справка', "Название продукта должно быть представлено русскими буквами и с заглавной буквы.\n "
                      "Информация о продукте должна быть представлена в виде числа и меры измерения(ккал, кКал, г)\n"
                      "Информация в строках не должна привышать 25 символов",
            QMessageBox.Ok)

    def add_product(self):
        # назначение пременных
        name = self.food_label.text()
        caloric = self.caloric_label.text()
        squirrels = self.squirrels_label.text()
        fats = self.fats_label.text()
        carbohydrates = self.carbohydrates_label.text()
        # проверка
        if proverka_name(name) is False or len(name) > 25 \
                or proverka_inf(caloric) is False \
                or len(caloric) > 25 \
                or proverka_inf(squirrels) is False \
                or len(squirrels) > 25 \
                or proverka_inf(fats) is False \
                or len(fats) > 25  \
                or proverka_inf(carbohydrates) is False \
                or len(carbohydrates) > 25:
            self.error.setStyleSheet(
                "QStatusBar{padding-left:8px;background:rgb(255,0,0);color:black;font-weight:bold;}")
            self.error.showMessage('Ошибка оформления данных')
        else:
            try:
                # добавление
                con = sqlite3.connect('База данных проекта.db')
                cur = con.cursor()
                cur.execute(f"""INSERT INTO Продукты(link, food, caloric, squirrels, fats, carbohydrates) 
                    VALUES('{self.name_image}', '{name}', '{caloric}', '{squirrels}', '{fats}', '{carbohydrates}')""")
                con.commit()
                con.close()
                self.ago()
            except:
                self.error.setStyleSheet(
                    "QStatusBar{padding-left:8px;background:rgb(255,0,0);color:black;font-weight:bold;}")
                self.error.showMessage('Такой продукт уже есть')

    def deleted_image(self):
        # удаление старой картинки
        if self.name_image != 'Картинки\без изображения.png':
            os.remove(self.name_image)
        # применение обычной картинки
        self.name_image = 'Картинки\без изображения.png'
        self.pixmap = QPixmap('Картинки\без изображения.png')
        self.image_label.setPixmap(self.pixmap)

    def ago(self):
        if self.sender() == self.back:
            if self.name_image != 'Картинки\без изображения.png':
                os.remove(self.name_image)
        self.close()
        self.open = Food(self, self.data)
        self.open.show()


class Update_food(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        uic.loadUi("ui-файлы/Изменение продукта.ui", self)
        self.setWindowTitle('Изменение продукта')
        self.setFixedSize(350, 420)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.pixmap = QPixmap('Картинки\без изображения.png')
        self.pixmap1 = QPixmap('Картинки для программы\Название продукта.png')
        self.pixmap2 = QPixmap('Картинки для программы\Калорийность.png')
        self.pixmap3 = QPixmap('Картинки для программы\Кол-во белков.png')
        self.pixmap4 = QPixmap('Картинки для программы\Кол-во жиров.png')
        self.pixmap5 = QPixmap('Картинки для программы\Кол-во углеводов.png')
        self.pixmap6 = QPixmap('Картинки для программы\Фото продукта.png')
        self.image_label.setPixmap(self.pixmap)
        self.label.setPixmap(self.pixmap1)
        self.label_2.setPixmap(self.pixmap2)
        self.label_3.setPixmap(self.pixmap3)
        self.label_4.setPixmap(self.pixmap4)
        self.label_5.setPixmap(self.pixmap5)
        self.label_6.setPixmap(self.pixmap6)
        self.setStyleSheet('background: rgb(255,127,39)')
        self.ok.setStyleSheet('background: rgb(255,127,39);border: rgb(255, 127, 39)')
        self.add.setStyleSheet('background: rgb(255,127,39);border: rgb(255, 127, 39)')
        self.deleted.setStyleSheet('background: rgb(255,127,39);border: rgb(255, 127, 39)')
        self.back.setStyleSheet('background: rgb(255,127,39);border: rgb(255, 127, 39)')
        self.reference.setStyleSheet('background: rgb(255,127,39);border: rgb(255, 127, 39)')

        self.back.clicked.connect(self.ago)
        self.add.clicked.connect(self.add_image)
        self.deleted.clicked.connect(self.deleted_image)
        self.ok.clicked.connect(self.update_product)
        self.reference.clicked.connect(self.open_reference)

        self.error = QStatusBar(self)
        self.error.move(10, 395)
        self.error.resize(500, 20)

        # назначение переменных
        self.data = args[-1][0]
        self.search = args[-1][1]
        self.combo = args[-1][2]
        self.number = args[-1][3]
        # поиск данных
        con = sqlite3.connect('База данных проекта.db')
        cur = con.cursor()
        if self.search != '' and self.search != 'Ничего не найдено':
            self.result = cur.execute(f"""SELECT * FROM Продукты 
            WHERE food like '{self.search.capitalize()}%'""").fetchall()
        else:
            self.result = cur.execute(f"""SELECT * FROM Продукты 
            WHERE food like '{self.combo}%'""").fetchall()
        con.close()
        # распределение информации на виджеты
        self.unknown = self.result[self.number - 1]
        self.food_label.setText(self.unknown[1])
        self.caloric_label.setText(self.unknown[2])
        self.squirrels_label.setText(self.unknown[3])
        self.fats_label.setText(self.unknown[4])
        self.carbohydrates_label.setText(self.unknown[5])
        self.pixmap7 = QPixmap(self.unknown[0])
        self.name_image = self.unknown[0]
        self.image_label.setPixmap(self.pixmap7)
        # список с картинками на случай, если будет нажата кнопка назад
        self.images = []
        self.images.append(self.unknown[0])

    def open_reference(self):
        valid = QMessageBox.question(
            self, 'Справка', "Название продукта должно быть представлено русскими буквами и с заглавной буквы.\n "
            "Информация о продукте должна быть представлена в виде числа и меры измерения(ккал, кКал, г)\n"
            "Информация в строках не должна привышать 25 символов",
            QMessageBox.Ok)

    def add_image(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
            link = f'Картинки\{fname.split("/")[-1]}'
            # поиск на индивидуальность картинки
            con = sqlite3.connect('База данных проекта.db')
            cur = con.cursor()
            links = cur.execute(f"""SELECT link FROM Продукты""").fetchall()
            con.close()
            # изменение links для чтения
            for i in range(len(links)):
                links[i] = links[i][0]
            # проверка
            if fname == '':
                pass
            elif link in links:
                self.error.setStyleSheet(
                    "QStatusBar{padding-left:8px;background:rgb(255,0,0);color:black;font-weight:bold;}")
                self.error.showMessage('Картинка с таким же названием уже используется')
            else:
                # сжатие изображения под определённый размер
                im = Image.open(fname)
                im2 = im.resize((200, 200))
                im2.save(link)
                # применение картинки
                self.name_image = link
                self.pixmap = QPixmap(link)
                self.image_label.setPixmap(self.pixmap)
                self.images.append(link)
        except:
            self.error.setStyleSheet(
                "QStatusBar{padding-left:8px;background:rgb(255,0,0);color:black;font-weight:bold;}")
            self.error.showMessage('Неподдерживаемый формат файла')

    def update_product(self):
        # назначение переменных
        name = self.food_label.text()
        caloric = self.caloric_label.text()
        squirrels = self.squirrels_label.text()
        fats = self.fats_label.text()
        carbohydrates = self.carbohydrates_label.text()
        # проверка
        if proverka_name(name) is False or len(name) > 25 \
                or proverka_inf(caloric) is False \
                or len(caloric) > 25 \
                or proverka_inf(squirrels) is False \
                or len(squirrels) > 25 \
                or proverka_inf(fats) is False \
                or len(fats) > 25 \
                or proverka_inf(carbohydrates) is False \
                or len(carbohydrates) > 25:
            self.error.setStyleSheet(
                "QStatusBar{padding-left:8px;background:rgb(255,0,0);color:black;font-weight:bold;}")
            self.error.showMessage('Ошибка оформления данных')
        else:
            try:
                # удаление ненужных фотографий
                self.images.insert(1, 'Картинки\без изображения.png')
                if len(self.images) > 1:
                    for i in self.images[0:-1]:
                        if i != 'Картинки\без изображения.png' and i != self.name_image:
                            os.remove(i)
                # изменение
                con = sqlite3.connect('База данных проекта.db')
                cur = con.cursor()
                cur.execute(f"""UPDATE Продукты SET link = '{self.name_image}', food = '{name}', 
                    caloric = '{caloric}', squirrels = '{squirrels}', 
                    fats = '{fats}', carbohydrates = '{carbohydrates}' 
                    WHERE link = '{self.unknown[0]}' and 
                    food = '{self.unknown[1]}' and caloric = '{self.unknown[2]}' and 
                    squirrels = '{self.unknown[3]}' and 
                    fats = '{self.unknown[4]}' and carbohydrates = '{self.unknown[5]}'""")
                con.commit()
                con.close()
                self.ago()
            except:
                self.error.setStyleSheet(
                    "QStatusBar{padding-left:8px;background:rgb(255,0,0);color:black;font-weight:bold;}")
                self.error.showMessage('Такой продукт уже есть')

    def deleted_image(self):
        self.name_image = 'Картинки\без изображения.png'
        self.pixmap = QPixmap('Картинки\без изображения.png')
        self.image_label.setPixmap(self.pixmap)

    def ago(self):
        if self.sender() == self.back and len(self.images) > 1:
            # удаление ненужных фотографий
            self.new_list = []
            [self.new_list.append(item) for item in self.images if item not in self.new_list]
            for i in self.new_list[1:]:
                os.remove(i)
        self.close()
        self.open = Food(self, self.data)
        self.open.show()


class Work(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        uic.loadUi("ui-файлы/Тренировки.ui", self)
        self.setWindowTitle('Мои тренировки(расписание)')
        self.setFixedSize(600, 600)

        self.add.clicked.connect(self.add_workout)
        self.back.clicked.connect(self.ago)
        self.update.clicked.connect(self.update_workout)
        self.deleted.clicked.connect(self.del_workout)
        self.search.clicked.connect(self.update_result)

        self.error = QStatusBar(self)
        self.error.move(10, 35)
        self.error.resize(600, 20)

        self.back.setStyleSheet('background: rgb(255,255,0);border: rgb(255, 255, 0);')
        self.search.setStyleSheet('background: rgb(255,255,0);border: rgb(255, 255, 0);')
        self.add.setStyleSheet('background: rgb(255,255,0);border: rgb(255, 255, 0);')
        self.update.setStyleSheet('background: rgb(255,255,0);border: rgb(255, 255, 0);')
        self.deleted.setStyleSheet('background: rgb(255,255,0);border: rgb(255, 255, 0);')
        self.pixmap = QPixmap('Картинки для программы\Поиск.png')
        self.label.setPixmap(self.pixmap)

        self.data = args[-1]

        self.update_result()

    def update_result(self):
        # поиск данных
        con = sqlite3.connect('База данных проекта.db')
        cur = con.cursor()
        if self.sender() != self.search:
            self.result = cur.execute(f"""SELECT workout, description, time, date FROM Тренировки WHERE user = 
                                {search_id(self.data.split()[0])}""").fetchall()
        else:
            self.result = cur.execute(f"""SELECT workout, description, time, date 
                                FROM Тренировки WHERE workout like '{self.search_label.text()}%' 
                                and user = {search_id(self.data.split()[0])}""").fetchall()
        con.close()
        self.result = sorted(self.result, key=lambda x: (x[3], x[2]))
        # отображение данных
        if len(self.result) > 0:
            self.tableWidget.setRowCount(len(self.result))
            self.tableWidget.setColumnCount(len(self.result[0]))
            self.tableWidget.setHorizontalHeaderLabels(["Название тренировки", "Описание", "Время", "Дата"])
            self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
            self.tableWidget.horizontalHeader().setMinimumSectionSize(150)
            self.tableWidget.horizontalHeader().setMaximumSectionSize(150)
            for i, elem in enumerate(self.result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.tableWidget.resizeColumnsToContents()
        else:
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setBrush(Qt.yellow)
        painter.drawRect(self.rect())

    def add_workout(self):
        self.close()
        self.add_window = Work_process(self, self.data, 'add')
        self.add_window.show()

    def del_workout(self):
        if len(self.result) > 0:
            number, ok_pressed = QInputDialog.getInt(
                self, "Введите номер строки", "Введите номер строки, которую хотите удалить",
                1, 1, len(self.result), 1)
            if ok_pressed:
                # определение переменных
                user = search_id(self.data.split()[0])
                workout = self.result[number - 1][0]
                description = self.result[number - 1][1]
                time = self.result[number - 1][2]
                date = self.result[number - 1][3]
                # удаление
                con = sqlite3.connect('База данных проекта.db')
                cur = con.cursor()
                cur.execute(f"""DELETE from Тренировки WHERE (user, workout, description,
                 time, date) = ('{user}', '{workout}', '{description}', '{time}', '{date}')""")
                con.commit()
                con.close()
                self.update_result()
        else:
            self.error.setStyleSheet(
                "QStatusBar{padding-left:8px;background:rgb(255,0,0);color:black;font-weight:bold;}")
            self.error.showMessage('У вас нет записей на удаление')


    def update_workout(self):
        if len(self.result) > 0:
            number, ok_pressed = QInputDialog.getInt(
                self, "Введите номер строки", "Введите номер строки, которую хотите изменить",
                1, 1, len(self.result), 1)
            if ok_pressed:
                self.close()
                self.open = Work_process(self, (self.data, number))
                self.open.show()
        else:
            self.error.setStyleSheet("QStatusBar{padding-left:8px;background:"
                                     "rgb(255,0,0);color:black;font-weight:bold;}")
            self.error.showMessage('У вас нет записей на изменение')

    def ago(self):
        self.close()
        self.open = Main(self, self.data)
        self.open.show()


class Work_process(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = args
        self.initUI()

    def initUI(self):
        uic.loadUi("ui-файлы/Добавление  и изменение тренировки.ui", self)
        if self.args[-1] == 'add':
            self.setWindowTitle('Добавление тренировки')
        else:
            self.setWindowTitle('Изменение тренировки')
        self.setFixedSize(600, 320)

        self.agoo.clicked.connect(self.ago)
        self.go.clicked.connect(self.run)

        self.error = QStatusBar(self)
        self.error.move(10, 300)
        self.error.resize(600, 20)

        self.calendarik.setStyleSheet('background: rgb(0,128,128);border: rgb(0, 255, 255);')
        self.go.setStyleSheet('background: rgb(0,255,255);border: rgb(0, 255, 255);')
        self.agoo.setStyleSheet('background: rgb(0,255,255);border: rgb(0, 255, 255);')
        self.pixmap = QPixmap('Картинки для программы\Дата тренировки.png')
        self.pixmap1 = QPixmap('Картинки для программы\Описание тренировки.png')
        self.pixmap2 = QPixmap('Картинки для программы\Время тренировки.png')
        self.pixmap3 = QPixmap('Картинки для программы\Название тренировки.png')
        self.date_label.setPixmap(self.pixmap)
        self.inf_label.setPixmap(self.pixmap1)
        self.time_label.setPixmap(self.pixmap2)
        self.name_label.setPixmap(self.pixmap3)

        self.data = self.args[1]
        if self.args[-1] == 'add':
            date = datetime.today()
            self.time_of_tr.setTime(QTime(date.hour, date.minute))
        else:
            # поиск данных
            con = sqlite3.connect('База данных проекта.db')
            cur = con.cursor()
            self.result = cur.execute(
                f"""SELECT workout, description, time, date FROM Тренировки WHERE user 
                                        = {search_id(self.data[0].split()[0])}""").fetchall()
            con.close()
            # сортировка данных
            self.result = sorted(self.result, key=lambda x: (x[3], x[2]))
            # добавление на виджеты данных
            coord = int(self.data[1]) - 1
            hour = int(self.result[coord][2].split(':')[0])
            minute = int(self.result[coord][2].split(':')[1])
            inf = self.result[coord][1]
            name = self.result[coord][0]
            self.time_of_tr.setTime(QTime(hour, minute))
            self.info.setText(str(inf))
            self.name_of_tr.setText(str(name))

    def run(self):
        self.error.setStyleSheet(
            "QStatusBar{padding-left:8px;background:rgb(255,255,255);color:black;font-weight:bold;}")
        self.error.showMessage('')
        # задаём переменные
        user = search_id(self.data[0].split()[0])
        workout_new = self.name_of_tr.text()
        time_new = self.time_of_tr.text()
        inf_new = self.info.text()
        date_new = f'{self.calendarik.selectedDate().toString("dd/MM/yyyy")}' \
            .replace('(', '').replace(')', '').replace("'", '')
        date_new = datetime.strptime(date_new, "%d/%m/%Y").strftime("%Y-%m-%d")
        if self.args[-1] != 'add':
            number = self.data[1] - 1
            workout = self.result[number][0]
            inf = self.result[number][1]
            time = self.result[number][2]
            date = self.result[number][3]
        # проверка
        if len(workout_new) > 45:
            self.error.setStyleSheet(
                "QStatusBar{padding-left:8px;background:rgb(255,57,41);color:black;font-weight:bold;}")
            self.error.showMessage('Слишком большое название.Описание не должно привышать 45 символов')
        elif len(inf_new) > 75:
            self.error.setStyleSheet(
                "QStatusBar{padding-left:8px;background:rgb(255,57,41);color:black;font-weight:bold;}")
            self.error.showMessage('Слишком большое описание.Описание не должно привышать 110 символов')
        else:
            con = sqlite3.connect('База данных проекта.db')
            cur = con.cursor()
            if self.args[-1] == 'add':
                # поиск id пользователя
                user = search_id(self.data.split()[0])
                # добавление тренировки
                cur.execute(f"""INSERT INTO Тренировки(user, workout, description, time, 
                    date) VALUES('{user}', '{workout_new}', '{inf_new}', '{time_new}', '{date_new}')""")
            else:
                # изменение
                cur.execute(f"""UPDATE Тренировки SET workout = '{workout_new}', description = '{inf_new}', 
                                time = '{time_new}', date = '{date_new}' WHERE user = {user} and workout = '{workout}' 
                                and description = '{inf}' and time = '{time}' and date = '{date}'""")
            con.commit()
            con.close()
            self.ago()

    def ago(self):
        if self.args[-1] == 'add':
            self.close()
            self.open = Work(self, self.data)
            self.open.show()
        else:
            self.close()
            self.open = Work(self, self.data[0])
            self.open.show()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setBrush(Qt.cyan)
        painter.drawRect(self.rect())


class Calculator(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        uic.loadUi("ui-файлы/Калькулятор каллорий.ui", self)
        self.setWindowTitle('Калькулятор каллорий')
        self.setFixedSize(600, 130)

        self.back.clicked.connect(self.ago)
        self.ok.clicked.connect(self.run)

        self.ok.setStyleSheet('background: rgb(255;0;255);border: rgb(255;0;255);')
        self.back.setStyleSheet('background: rgb(255;0;255);border: rgb(255;0;255);')
        self.box_exercises.setStyleSheet('background: rgb(255;255;255);border: rgb(255;255;255);')
        self.line_time.setStyleSheet('background: rgb(255;255;255);border: rgb(255;255;255);')
        self.box_meal.setStyleSheet('background: rgb(255;255;255);border: rgb(255;255;255);')
        self.portions.setStyleSheet('background: rgb(255;255;255);border: rgb(255;255;255);')
        self.itogo.setStyleSheet('background: rgb(128;0;128);border: rgb(128;0;128);')
        self.pixmap = QPixmap('Картинки для программы\Итого.png')
        self.pixmap1 = QPixmap('Картинки для программы\ккал.png')
        self.pixmap2 = QPixmap('Картинки для программы\Вид деятельности.png')
        self.pixmap3 = QPixmap('Картинки для программы\Время .png')
        self.pixmap4 = QPixmap('Картинки для программы\Пища.png')
        self.pixmap5 = QPixmap('Картинки для программы\Количество порций.png')
        self.pixmap6 = QPixmap('Картинки для программы\Итого вы приобрели.png')
        self.itogo_label.setPixmap(self.pixmap)
        self.label_kkal.setPixmap(self.pixmap1)
        self.work.setPixmap(self.pixmap2)
        self.time.setPixmap(self.pixmap3)
        self.food.setPixmap(self.pixmap4)
        self.count_food.setPixmap(self.pixmap5)
        self.error = QStatusBar(self)
        self.error.move(5, 110)
        self.error.resize(600, 20)
        self.error.setStyleSheet("QStatusBar{padding-left:8px;background:rgb(255,0,255);"
                                 "color:black;font-weight:bold;}")
        self.line_time.setText('0')

        self.activitys = {'отсутствует': '0 ккал',
                          'Прогулка': '200 ккал',
                          'Бег': '600 ккал',
                          'Плаванье': '500 ккал',
                          'Йога': '300 ккал',
                          'Езда на велосипеде': '630 ккал',
                          'Умственная деятельность': '90 ккал',
                          'Игра в компьютер': '90 ккал',
                          'Гимнастика': '350 ккал',
                          'Игра в футбол': '490 ккал',
                          'Игра в баскетбол': '300 ккал',
                          'Игра в тенис': '360 ккал',
                          'Игра в бадминтон': '250 ккал',
                          'Игра в волейбол': '240 ккал'}

        self.box_exercises.addItems(['отсутствует', 'Прогулка', 'Бег', 'Плаванье', 'Йога', 'Езда на велосипеде',
                                     'Умственная деятельность', 'Игра в компьютер', 'Гимнастика',
                                     'Игра в футбол', 'Игра в баскетбол', 'Игра в тенис', 'Игра в бадминтон',
                                     'Игра в волейбол'])

        self.portions.setMaximum(5)

        self.data = args[-1]

        # добавление списка продуктов на виджет и создания словаря для вычисления
        con = sqlite3.connect('База данных проекта.db')
        cur = con.cursor()
        new_food = cur.execute("""SELECT food, caloric from Продукты""")
        self.food = {'отсутствует': '0 ккал'}
        food_list = ['отсутствует']
        for i in new_food:
            self.food[i[0]] = i[1]
            food_list.append(i[0])
        con.close()
        self.box_meal.addItems(sorted(food_list))

    def ago(self):
        self.close()
        self.open = Main(self, self.data)
        self.open.show()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setBrush(Qt.magenta)
        painter.drawRect(self.rect())

    def run(self):
        self.error.setStyleSheet("QStatusBar{padding-left:8px;background:rgb(255,0,255);"
                                 "color:black;font-weight:bold;}")
        self.error.showMessage('')
        try:
            # задаём переменные
            activi = float(self.activitys[self.box_exercises.currentText()].split()[0])
            count_activi = float(self.line_time.text())
            food = float(self.food[self.box_meal.currentText()].split()[0])
            count_food = float(self.portions.value())
            # проверка
            if len(self.line_time.text()) > 4 or '-' in self.line_time.text():
                raise Error_of_input()
            # меняем название label на соответствующее
            if (food * count_food) - (activi * (count_activi / 60)) > 0:
                self.itogo_label.setPixmap(self.pixmap6)
            if (food * count_food) - (activi * count_activi) <= 0:
                self.itogo_label.setPixmap(self.pixmap)
            # выводим ответ
            self.itogo.display((food * count_food) - (activi * (count_activi / 60)))
        except:
            self.error.setStyleSheet("QStatusBar{padding-left:8px;background:"
                        "rgb(255,0,0);color:black;font-weight:bold;}")
            self.error.showMessage('Ошибка.Видимо вы ввели '
                        'слишком большое число или недопустимое значение.')


class Error_of_input(Exception):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Картинки для программы/иконка.png'))
    ex = Entrance('')
    ex.show()
    sys.exit(app.exec())