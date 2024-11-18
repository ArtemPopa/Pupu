import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from random import *
from pygame import *
import pygame as pg
import os
from database.dao.dao import UserDAO

reiting = {
    'clicer': 0, 
    'history_1': 0,
    'history_2': 0,
    'history_3': 0,
}



Mg2 = [
    'Викторина 1',
    'Викторина 2',
    'Викторина 3'
]

Mg1 = [
    'Калькулятор Цезаря',
    'Викторина музыка',
    'Кликер'
]

color = [
    'QPushButton {background-color: #ADFF2F}',
    'QPushButton {background-color: #20B2AA}',
    'QPushButton {background-color: #00FF00}',
    'QPushButton {background-color: #FF1493}',
    'QPushButton {background-color: #FF6347}',
    'QPushButton {background-color: #FA8072}',
    'QPushButton {background-color: #FFFF00}',
    'QPushButton {background-color: #EE82EE}',
    'QPushButton {background-color: #FF00FF}',
    'QPushButton {background-color: #4169E1}',
    'QPushButton {background-color: #D2691E}'
]

'''user = {
    'Имя пользователя': None,
    'Кликов в минуту': 0,
    'Музыкальная викторина': 0,
    'Историческая викторина1': 0,
    'Историческая викторина2': 0,
    'Историческая викторина3': 0,
    'Проверка на ловкость': 'Не пройденна',
    'Проверка на дебила': 'Не пройденна'
}
'''
user = {
    'username': None,
    'best_score': 0,
}

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        mixer.init()

        self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("Привет! Введите свой крутой ник-нейм")
        self.setStyleSheet("background-color: #FFFAFA;") 
        
        self.nickname_label = QLabel("Введите крутой ник-нейм", self)
        self.nickname_input = QLineEdit(self) 
        self.nickname_label.setFont(QFont('Arial', 25))
        self.nickname_label.setStyleSheet("color: #FF7F50;")
        
        self.next_button = QPushButton("Далее", self)
        self.next_button.setStyleSheet("width: 100px; height: 50px;")
        self.next_button.clicked.connect(self.open_modal_dialog)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.nickname_label)
        self.layout.addWidget(self.nickname_input)
        self.layout.addWidget(self.next_button)
        self.setLayout(self.layout)
        
        self.modal_dialog = None

        self.music_file = os.path.join('static/sounds/virus.mp3')

        mixer.music.load(self.music_file)

    def open_modal_dialog(self):
        self.nickname = self.nickname_input.text()
        if self.nickname == '':
            self.nickname = 'Player'
            if UserDAO.find_one_or_none(username=self.nickname):
                self.nickname = 'Player1'
            if UserDAO.find_one_or_none(username=self.nickname):
                self.nickname = 'Player2'
            if UserDAO.find_one_or_none(username=self.nickname):
                self.nickname = 'Player3'
            if UserDAO.find_one_or_none(username=self.nickname):
                self.nickname = 'Player4'
            if UserDAO.find_one_or_none(username=self.nickname):
                self.nickname = 'Player5'

        if UserDAO.find_one_or_none(username=self.nickname):
            self.modal_dialog = Window_menu(self)
            self.modal_dialog.setWindowTitle("Модальное окно")
            self.modal_dialog.label.setText(f"Привет, {self.nickname}!")
        else:
            UserDAO.add(username=self.nickname)
            self.modal_dialog = Window_menu(self)
            self.modal_dialog.setWindowTitle("Модальное окно")
            self.modal_dialog.label.setText(f"Привет новый\nпользователь, {self.nickname}!")

        '''self.modal_dialog = Window_menu(self)
        self.modal_dialog.setWindowTitle("Модальное окно")
        self.modal_dialog.label.setText(f"Привет, {self.nickname}!")'''
        global user
        '''user['Имя пользователя'] = self.nickname'''
        user['username'] = self.nickname
        self.next_button.setEnabled(False)

        self.modal_dialog.show()


class AboutWindow(QWidget):
    def __init__(self):
        super(AboutWindow, self).__init__()

        self.setWindowTitle('О программе')

        self.text = open("about.txt", 'r', encoding='utf8')
        
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText(f'{self.text.read()}')
        self.layout().addWidget(self.info)
        self.text.close()


class Window_About(QMainWindow):
    def __init__(self):
        super(Window_About, self).__init__()

        self.setWindowTitle("Привет! Введите свой крутой ник-нейм")
        self.setCentralWidget(MainWindow())

        self.about_action = QAction(self)
        self.about_action.setText('О программе')
        self.about_action.triggered.connect(self.about)
        self.menuBar().addAction(self.about_action)

        self.about_window = AboutWindow()

    def about(self):
        self.about_window.show()

class Window_menu(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QLabel(self)

        self.setWindowTitle('Добро пожаловать')
        self.setFixedSize(QSize(400, 300))

        self.layout = QVBoxLayout()
        self.label.move(10, 10)
        self.label.setFont(QFont('Arial', 25))


        self.inp_t = QComboBox(self)
        self.inp_t.move(10, 160)
        self.inp_t.resize(120, 30)
        self.inp_t.addItems(Mg1)


        self.va1 = QLineEdit(self)
        self.va1.setEnabled(False)
        self.va1.setText('Прикалюхи')
        self.va1.move(10, 120)
        self.va1.resize(120, 30)

        self.start_bt1 = QPushButton(self)
        self.start_bt1.setText('Старт')
        self.start_bt1.move(10, 200)
        self.start_bt1.resize(120, 30)
        self.start_bt1.clicked.connect(self.start1)


        self.inp_t2 = QComboBox(self)
        self.inp_t2.move(170, 160)
        self.inp_t2.resize(120, 30)
        self.inp_t2.addItems(Mg2)

        self.va2 = QLineEdit(self)
        self.va2.setEnabled(False)
        self.va2.setText('История')
        self.va2.move(170, 120)
        self.va2.resize(120, 30)

        self.start_bt2 = QPushButton(self)
        self.start_bt2.setText('Старт')
        self.start_bt2.move(170, 200)
        self.start_bt2.resize(120, 30)
        self.start_bt2.clicked.connect(self.start2)

        self.rating_bt2 = QPushButton(self)
        self.rating_bt2.setText('Рейтинг')
        self.rating_bt2.move(170, 260)
        self.rating_bt2.resize(120, 30)
        self.rating_bt2.clicked.connect(self.rating)

        self.poshalko_bt2 = QPushButton(self)
        self.poshalko_bt2.setStyleSheet('QPushButton {background-color: red}')
        self.poshalko_bt2.setText('Не нажимать!!!')
        self.poshalko_bt2.move(10, 260)
        self.poshalko_bt2.resize(120, 30)
        self.poshalko_bt2.clicked.connect(self.poshalko)



    def start1(self):
        self.game_window = self.inp_t.currentText()
        if self.game_window == Mg1[0]:
            calculator_modal = Calculator(self)
            calculator_modal.exec()
        if self.game_window == Mg1[1]:
            mixer.pause()
            self.musicv1 = os.path.join('static/sounds/000.mp3')
            self.music_v1 = pg.mixer.Sound(self.musicv1)
            self.music_v1.play()
            clicker_modal = Music_Viktorin(self)
            clicker_modal.exec()
        if self.game_window == Mg1[2]:
            clicker_modal = Window_Clicker(self)
            clicker_modal.exec()
        

    def start2(self):
        self.history_window1 = self.inp_t2.currentText()
        if self.history_window1 == Mg2[0]:
            history_modal1 = HistoryQuiz_1(self)
            history_modal1.exec()

        if self.history_window1 == Mg2[1]:
            history_modal1 = HistoryQuiz_2(self)
            history_modal1.exec()
        
        if self.history_window1 == Mg2[2]:
            history_modal1 = HistoryQuiz_3(self)
            history_modal1.exec()

    def rating(self):
        rating_modal = Rating_Modal(self)
        rating_modal.exec()

    def poshalko(self):
        global user
        user['Проверка на дебила'] = 'Пройденна'
        mixer.music.play()
        poshalko_modal = Window_Poshalko(self)
        poshalko_modal.exec()

class Window_Clicker(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Кликер 10 секунд")
        self.setFixedSize(QSize(400, 300))

        self.clicks = 0

        self.click_button = QPushButton(str(self.clicks), self)
        self.click_button.resize(220, 140)
        self.click_button.move(90, 80)
        self.click_button.clicked.connect(self.addClick)

        self.timer = QTimer(self)
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.showClicksPerMinute)
        self.timer.start()


    def addClick(self):
        self.clicks += 1
        self.click_button.setText(str(self.clicks))
        self.click_button.setStyleSheet(choice(color))

    def showClicksPerMinute(self):
        clicks_per_minute = int(self.clicks / 10 * 60)
        self.click_button.setText(f"Clicks per minute: {clicks_per_minute}")
        self.click_button.setDisabled(True)
        global user
        '''if user['Кликов в минуту'] > clicks_per_minute:
            pass
        else:
            user['Кликов в минуту'] == clicks_per_minute'''
        

class HistoryQuiz_1(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Историческая викторина1')
        self.flag = True

        self.questions = {
            'Когда была Великая Французская Революция?': {
                'a': '1789-1799',
                'b': '1917',
                'c': '1950'
            },
            'Кто первый президент США?': {
                'a': 'А.Линкольн',
                'b': 'Д.Вашингтон',
                'c': 'Д.Кеннеди'
            },
            'Последний Российский император?': {
                'a': 'Николай II',
                'b': 'Михаил Романов',
                'c': 'Борис Ельцин'
            },
            'Когда началась вторая мировая война?': {
                'a': '1799',
                'b': '1941',
                'c': '1939'
            },
            'Как зовут преподавателя Яндекс Лицея?': {
                'a': 'Дмитрий',
                'b': 'Александр',
                'c': 'Андрей'
            }
            
        }
        
        self.answers = {
            'Когда была Великая Французская Революция?': 'a',
            'Кто первый президент США?': 'b',
            'Последний Российский император?': 'b',
            'Когда началась вторая мировая война?': 'c',
            'Как зовут преподавателя Яндекс Лицея?': 'b'
        }
        
        self.current_question = 0
        self.score = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        self.question_label = QLabel('')
        self.option_a = QRadioButton('')
        self.option_b = QRadioButton('')
        self.option_c = QRadioButton('')
        self.submit_button = QPushButton('Ответить')
        
        self.submit_button.clicked.connect(self.check_answer)
        
        layout = QVBoxLayout()
        
        layout.addWidget(self.question_label)
        layout.addWidget(self.option_a)
        layout.addWidget(self.option_b)
        layout.addWidget(self.option_c)
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)
        
        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            question = list(self.questions.keys())[self.current_question]
            options = self.questions[question]
            
            self.question_label.setText(question)
            self.option_a.setText(options['a'])
            self.option_b.setText(options['b'])
            self.option_c.setText(options['c'])
            
            self.current_question += 1
        else:
            self.show_result()
    
    def check_answer(self):
        current_question = list(self.questions.keys())[self.current_question - 1]
        selected_answer = ''
        
        if self.option_a.isChecked():
            selected_answer = 'a'
        elif self.option_b.isChecked():
            selected_answer = 'b'
        elif self.option_c.isChecked():
            selected_answer = 'c'
        
        correct_answer = self.answers[current_question]
        
        if selected_answer == correct_answer:
            self.score += 1
        if self.flag:
            self.show_question()
    
    def show_result(self):
        self.flag = False
        msg = QMessageBox()
        msg.setWindowTitle('Результаты викторины')
        msg.setText(f'Вы ответили правильно на {self.score} из {len(self.questions)} вопросов.')
        msg.exec()
        global user
        if user['Историческая викторина1'] > self.score:
            pass
        else:
            user['Историческая викторина1'] == self.score
        

class HistoryQuiz_2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Историческая викторина2')
        self.flag1 = True
        
        self.questions = {
            'В каком году открыли Америку?': {
                'a': '1404',
                'b': '1492',
                'c': '1476'
            },
            'В каком году началась Первоя Мипрвая Война': {
                'a': '1914',
                'b': '1941',
                'c': '1918'
            },
            'Последний Российский царь?': {
                'a': 'Николай II',
                'b': 'Алексей Михайлович',
                'c': 'Ленин'
            },
            'В каком году люди впервые побывали в космосе?': {
                'a': '1989',
                'b': '1953',
                'c': '1961'
            },
            'Самая большая страна в истории?': {
                'a': 'Российская империя',
                'b': 'Британская империя.',
                'c': 'Монгольская империя'
            }
            
        }
        
        self.answers = {
            'В каком году открыли Америку?': 'b',
            'В каком году началась Первоя Мипрвая Война': 'a',
            'Последний Российский царь?': 'b',
            'В каком году люди впервые побывали в космосе?': 'c',
            'Самая большая страна в истории?': 'b'
        }
        
        self.current_question = 0
        self.score = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        self.question_label = QLabel('')
        self.option_a = QRadioButton('')
        self.option_b = QRadioButton('')
        self.option_c = QRadioButton('')
        self.submit_button = QPushButton('Ответить')
        
        self.submit_button.clicked.connect(self.check_answer)
        
        layout = QVBoxLayout()
        
        layout.addWidget(self.question_label)
        layout.addWidget(self.option_a)
        layout.addWidget(self.option_b)
        layout.addWidget(self.option_c)
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)
        
        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            question = list(self.questions.keys())[self.current_question]
            options = self.questions[question]
            
            self.question_label.setText(question)
            self.option_a.setText(options['a'])
            self.option_b.setText(options['b'])
            self.option_c.setText(options['c'])
            
            self.current_question += 1
        else:
            self.show_result()
    
    def check_answer(self):
        current_question = list(self.questions.keys())[self.current_question - 1]
        selected_answer = ''
        
        if self.option_a.isChecked():
            selected_answer = 'a'
        elif self.option_b.isChecked():
            selected_answer = 'b'
        elif self.option_c.isChecked():
            selected_answer = 'c'
        
        correct_answer = self.answers[current_question]
        
        if selected_answer == correct_answer:
            self.score += 1
        if self.flag1:
            self.show_question()
    
    def show_result(self):
        self.flag1 = False
        msg = QMessageBox()
        msg.setWindowTitle('Результаты викторины')
        msg.setText(f'Вы ответили правильно на {self.score} из {len(self.questions)} вопросов.')
        msg.exec()
        global user
        if user['Историческая викторина2'] > self.score:
            pass
        else:
            user['Историческая викторина2'] == self.score

class HistoryQuiz_3(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Историческая викторина2')
        self.flag2 = True
        
        self.questions = {
            'Сколько лет прожил черчилль уинстон?': {
                'a': '90',
                'b': '46',
                'c': '72'
            },
            'Сколько лет длилась столетняя война?': {
                'a': '100',
                'b': '116',
                'c': '110'
            },
            'Какого числа СССР напало на Поьшу?': {
                'a': '32 октября 1939',
                'b': '17 сентября 1939',
                'c': '24 марта 2034'
            },
            'Кто считаеться героем Шотландии?': {
                'a': 'Лев Толстой',
                'b': 'Том Круз',
                'c': 'Уильям Уоллес'
            },
            'Когда был основан первый город?': {
                'a': '5400 году до н.э.',
                'b': '12000 лет до н.э.',
                'c': '0001 году н.э.'
            }
            
        }
        
        self.answers = {
            'Сколько лет прожил черчилль уинстон?': 'a',
            'Сколько лет длилась столетняя война?': 'b',
            'Какого числа СССР напало на Поьшу?': 'b',
            'Кто считаеться героем Шотландии?': 'c',
            'Когда был основан первый город?': 'a'
        }
        
        self.current_question = 0
        self.score = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        self.question_label = QLabel('')
        self.option_a = QRadioButton('')
        self.option_b = QRadioButton('')
        self.option_c = QRadioButton('')
        self.submit_button = QPushButton('Ответить')
        
        self.submit_button.clicked.connect(self.check_answer)
        
        layout = QVBoxLayout()
        
        layout.addWidget(self.question_label)
        layout.addWidget(self.option_a)
        layout.addWidget(self.option_b)
        layout.addWidget(self.option_c)
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)
        
        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            question = list(self.questions.keys())[self.current_question]
            options = self.questions[question]
            
            self.question_label.setText(question)
            self.option_a.setText(options['a'])
            self.option_b.setText(options['b'])
            self.option_c.setText(options['c'])
            
            self.current_question += 1
        else:
            self.show_result()
    
    def check_answer(self):
        current_question = list(self.questions.keys())[self.current_question - 1]
        selected_answer = ''
        
        if self.option_a.isChecked():
            selected_answer = 'a'
        elif self.option_b.isChecked():
            selected_answer = 'b'
        elif self.option_c.isChecked():
            selected_answer = 'c'
        
        correct_answer = self.answers[current_question]
        
        if selected_answer == correct_answer:
            self.score += 1
        if self.flag2:
            self.show_question()
    
    def show_result(self):
        self.flag2 = False
        msg = QMessageBox()
        msg.setWindowTitle('Результаты викторины')
        msg.setText(f'Вы ответили правильно на {self.score} из {len(self.questions)} вопросов.')
        msg.exec()
        global user
        if user['Историческая викторина3'] > self.score:
            pass
        else:
            user['Историческая викторина3'] == self.score

class Music_Viktorin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Музыкальная викторина')
        self.flag5 = True

        self.musicv2 = os.path.join('static/sounds/001.mp3')
        self.musicv3 = os.path.join('static/sounds/002.mp3')
        self.musicv4 = os.path.join('static/sounds/003.mp3')
        self.musicv5 = os.path.join('static/sounds/007.mp3')
        
        self.music_v2 = pg.mixer.Sound(self.musicv2)
        self.music_v3 = pg.mixer.Sound(self.musicv3)
        self.music_v4 = pg.mixer.Sound(self.musicv4)
        self.music_v5 = pg.mixer.Sound(self.musicv5)

        self.questions = {
            'Что это за группа?': {
                'a': 'Зоопарк',
                'b': 'Машина времени',
                'c': 'Аквариум'
            },
            'Что это за песня?': {
                'a': 'ДДТ-Чёрное на Красном',
                'b': 'Алиса-Красное на Чёрном',
                'c': 'Инстасамка-Красный цвет'
            },
            'Что за песня?': {
                'a': 'Крематрий-Шпалер',
                'b': 'Кино-Группа крови',
                'c': 'Ногу свело-Африка'
            },
            'Что же это за песня?': {
                'a': 'Машина времени-День рождение',
                'b': 'Кино-Попробуй спеть вместе со мной',
                'c': 'КИШ-Два вора'
            },
            'Какая это песня?': {
                'a': 'Браво-Этот город',
                'b': 'Аквариум-Лети мой ангел лети',
                'c': 'ДДТ-Родина'
            }
            
        }
        
        self.answers = {
            'Что это за группа?': 'c',
            'Что это за песня?': 'b',
            'Что за песня?': 'a',
            'Что же это за песня?': 'b',
            'Какая это песня?': 'c'
        }
        
        self.current_question = 0
        self.score = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        self.question_label = QLabel('')
        self.option_a = QRadioButton('')
        self.option_b = QRadioButton('')
        self.option_c = QRadioButton('')
        self.submit_button = QPushButton('Ответить')
        
        self.submit_button.clicked.connect(self.check_answer)
        
        layout = QVBoxLayout()
        
        layout.addWidget(self.question_label)
        layout.addWidget(self.option_a)
        layout.addWidget(self.option_b)
        layout.addWidget(self.option_c)
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)

        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            question = list(self.questions.keys())[self.current_question]
            options = self.questions[question]
            
            self.question_label.setText(question)
            self.option_a.setText(options['a'])
            self.option_b.setText(options['b'])
            self.option_c.setText(options['c'])
            
            self.current_question += 1
        else:
            self.show_result()
    
    def check_answer(self):
        current_question = list(self.questions.keys())[self.current_question - 1]
        selected_answer = ''
        
        if self.option_a.isChecked():
            selected_answer = 'a'
        elif self.option_b.isChecked():
            selected_answer = 'b'
        elif self.option_c.isChecked():
            selected_answer = 'c'
        
        correct_answer = self.answers[current_question]
        
        if selected_answer == correct_answer:
            self.score += 1

        if self.current_question == 1:
            mixer.pause()
            self.music_v2.play()
        elif self.current_question == 2:
            mixer.pause()
            self.music_v3.play()
        elif self.current_question == 3:
            mixer.pause()
            self.music_v4.play()
        elif self.current_question == 4:
            mixer.pause()
            self.music_v5.play()
        if self.flag5:
            self.show_question()


    def show_result(self):
        self.flag5 = False
        msg = QMessageBox()
        msg.setWindowTitle('Результаты викторины')
        msg.setText(f'Вы ответили правильно на {self.score} из {len(self.questions)} вопросов.')
        msg.exec()
        global user
        if user['Музыкальная викторина'] > self.score:
            pass
        else:
            user['Музыкальная викторина'] == self.score

    
    def closeEvent(self, e): 
        if self.flag5:
            mixer.pause()
        else:
            close_modal = Close_Modal(self)
            close_modal.exec()

class Calculator(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setGeometry(600, 300, 200, 200)

        self.expr_line = QLineEdit()
        self.expr_line.setPlaceholderText("Enter expression")

        self.result_line = QLineEdit()
        self.result_line.setReadOnly(True)

        self.buttons = []
        grid_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        layout = QVBoxLayout()
        layout.addWidget(self.expr_line)
        layout.addWidget(self.result_line)

        for row in grid_layout:
            h_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.on_button_click)
                h_layout.addWidget(button)
                self.buttons.append(button)
            layout.addLayout(h_layout)

        self.setLayout(layout)

    def on_button_click(self):
        sender = self.sender()
        button_text = sender.text()
        if button_text == '=':
            try:
                result = (eval(self.expr_line.text()) + 3) * 2 
                self.result_line.setText(str(result))
            except Exception as e:
                self.result_line.setText("Error")
        elif button_text == 'C':
            self.expr_line.clear()
            self.result_line.clear()
        else:
            self.expr_line.setText(self.expr_line.text() + button_text)

class Window_Poshalko(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.showFullScreen()

        self.background_image = QPixmap(os.path.join('static/img/cat_screamer.jpg')) 

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background_image)

class Close_Modal(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Убегающая кнопка")
        self.showFullScreen()
        self.setStyleSheet("background-color: #AFEEEE;")

        self.button_C = QPushButton("Нажми меня!", self)
        self.button_C.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button_C.setFixedSize(200, 100)

        layout = QVBoxLayout()
        layout.addWidget(self.button_C)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_button)
        self.timer.start(150)
        self.button_C.clicked.connect(self.button_clicked)

    def move_button(self):
        if self.button_C.underMouse():
            button_width = self.button_C.width()
            button_height = self.button_C.height()
            window_width = self.width()
            window_height = self.height()

            new_x = randint(0, window_width - button_width)
            new_y = randint(0, window_height - button_height)

            self.button_C.move(new_x, new_y)
            self.button_C.setStyleSheet(choice(color))

    def button_clicked(self):
        global user
        user['Проверка на ловкость'] = 'Пройденна'
        mixer.pause()
        self.close()

class Rating_Modal(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Rating')
        self.setGeometry(600, 300, 200, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window_About()
    wnd.show()
    sys.exit(app.exec())

