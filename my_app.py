from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QApplication,QWidget,QHBoxLayout,QVBoxLayout,
QGroupBox,QRadioButton,QPushButton,QLabel
)

from random import shuffle

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Кто я ?','R','u','E','P'))
question_list.append(Question('Русский','Q,','W','H','Y'))
question_list.append(Question('L','I','O','N','X'))




app = QApplication([]) #создаём приложение 
window = QWidget()
window.setWindowTitle('Я Не умею печатать') #NAME

btn_ok = QPushButton('Ответить')
Il_Questtion = QLabel('КТО Я')

RadioGroupBox = QGroupBox('Варианты ответа')

rtts_1 = QRadioButton('Дв')
rtts_2 = QRadioButton('Д4')
rtts_3 = QRadioButton('Д3')
rtts_4 = QRadioButton('Д1')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()#Вертикальные линии будут внутри гориз.
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rtts_1)#2 ответа в левый столбец
layout_ans2.addWidget(rtts_2)
layout_ans3.addWidget(rtts_3)#2 ответа в правый
layout_ans3.addWidget(rtts_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)#Разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1)#готовы понели ответов


AnsGroupBox = QGroupBox('')
lb_Result = QLabel('')
lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft | Qt.AlignTop)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_card = QVBoxLayout()
layout_line1.addWidget(Il_Questtion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter) )
layout_line2.addWidget(RadioGroupBox)
layout_line3.addWidget(btn_ok)


layout_line1 = QHBoxLayout()#вопрос
layout_line2 = QHBoxLayout()#Варианты ответов
layout_line3 = QHBoxLayout()#Кнопка 'Ответ'

layout_card = QVBoxLayout()#размещение строк
layout_line1.addWidget(Il_Questtion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter) )
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_card = QVBoxLayout()#размещение строк
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)



window.setLayout(layout_card)

def show_results():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.show()
    btn_ok.setText('Ответить')
    #сбросить радио кнопку
    #RadioGroupBox.setExclusive()
    rtts_1setChecked(False)
    rtts_2setChecked(False)
    rtts_3setChecked(False)
    rtts_4setChecked(False)

answers = [rtts_1,rtts_2,rtts_3,rtts_4]
def ask(q: Question):
    #функция записывает значения вопросов и ответов 
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
    
def show_correct(res):
    lb_Result.setT(res)
    show_results()

def check_answer():
    if answers[0].isChecked():
        show_correct('Праваильно')
    else:
        show_correct('Не правильно')

def next_question():
    '''создает случ вопрос '''
    #этой функции нужна переменная , в которой будет указываться новый текущий вопрос
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0 #Если закончились то по новой
    q = question_list(window.cur_question)#Взяли вопрос
    ask(q)#спросили


def click_OK():
    if btn_ok.text() == 'ответить':
        check_answer()
    else:
        next_question()
        

window.setLayout(layout_card)

window.resize(600,390)

window.cur_question = -1
btn_ok.clicked.connect(click_OK)

window.show()#показать окно
app.exec()#оставляет прил. откр.