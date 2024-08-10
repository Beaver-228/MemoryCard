from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from random import shuffle


app=QApplication([])

from main_window import*
from menu_window import*

text_wrong="Неправильно"
text_correct="Правильно"

frm_question="Яблуко"
frm_right="apple"
frm_wrong1="application"
frm_wrong2="building"
frm_wrong3="caterpillar"

rbtn_list=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
shuffle(rbtn_list)
answer=rbtn_list[0]

wrong_answer1,wrong_answer2,wrong_answer3=rbtn_list[1],rbtn_list[2],rbtn_list[3]

def show_data():
    lb_Question.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)

def check_result():
    correct=answer.isChecked()
    if correct:
        lb_Result.setText(text_correct)
        show_result()
    else:
        incorrect=wrong_answer1.isChecked().isClecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:
            lb_Result.setText(text_wrong)
            show_result()
def click_Ok():
    if btn_OK.text()!="Наступне питання":
        check_result()

btn_OK.clicked.connect(click_Ok)

show_data()
show_question()


app.exec_()