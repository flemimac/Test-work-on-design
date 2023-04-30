from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Тестовая работа")
window.geometry("1000x500")

point1 = 0
answers_v1_n1 = []
true_answers_v1_n1 = "1111000" # Ответ на вариант 1, номер 1

point2 = 0
answers_v1_n2 = []
true_answers_v1_n2 = "1000" # Ответ на вариант 1, номер 2

point3 = 0
answers_v1_n3 = []
true_answers_v1_n3 = "0100" # Ответ на вариант 1, номер 3

point4 = 0
answers_v1_n4 = []
true_answers_v1_n4 = "0010" # Ответ на вариант 1, номер 4

point5 = 0
answers_v1_n5 = []
true_answers_v1_n5 = "00100" # Ответ на вариант 1, номер 5

point6 = 0
answers_v1_n6 = []
true_answers_v1_n6 = "01000" # Ответ на вариант 1, номер 6

point7 = 0
answers_v1_n7 = []
true_answers_v1_n7 = "11100" # Ответ на вариант 1, номер 7

point8 = 0
answers_v1_n8 = []
true_answers_v1_n8 = "10000" # Ответ на вариант 1, номер 8

point9 = 0
answers_v1_n9 = []
true_answers_v1_n9 = "1000" # Ответ на вариант 1, номер 9

point10 = 0
answers_v1_n10 = []
true_answers_v1_n10 = "100" # Ответ на вариант 1, номер 10

point11 = 0
answers_v1_n11 = []
true_answers_v1_n11 = "0001" # Ответ на вариант 1, номер 11

label = LabelFrame(text='Основы компьютерной графики')
def first(el):
    Button(el, text='Вариант №1', command=lambda e=el: question_v1_n1(e)).pack()
    
def check_v1(el): # Проверка варианта 1
    # Вызов очков
    global point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11
    
    # Проверка ответов номера 1
    for t, a in zip(true_answers_v1_n1, answers_v1_n1):
        if bool(int(t)) and bool(int(t)) == a.get():
            point1 += 1
            if point1 == 4:
                point1 = 1
            else:
                point1 = 0
        else:
            point1 = point1

    # Проверка ответов номера 2
    for t, a in zip(true_answers_v1_n2, answers_v1_n2):
        if bool(int(t)) and bool(int(t)) == a.get():
            point2 += 1
        else:
            point2 = point2  

    # Проверка ответов номера 3
    for t, a in zip(true_answers_v1_n3, answers_v1_n3):
        if bool(int(t)) and bool(int(t)) == a.get():
            point3 += 1
        else:
            point3 = point3

    # Проверка ответов номера 4
    for t, a in zip(true_answers_v1_n4, answers_v1_n4):
        if bool(int(t)) and bool(int(t)) == a.get():
            point4 += 1
        else:
            point4 = point4

    # Проверка ответов номера 5
    for t, a in zip(true_answers_v1_n5, answers_v1_n5):
        if bool(int(t)) and bool(int(t)) == a.get():
            point5 += 1
        else:
            point5 = point5

    # Проверка ответов номера 6
    for t, a in zip(true_answers_v1_n6, answers_v1_n6):
        if bool(int(t)) and bool(int(t)) == a.get():
            point6 += 1
        else:
            point6 = point6
    
    # Проверка ответов номера 7
    for t, a in zip(true_answers_v1_n7, answers_v1_n7):
        if bool(int(t)) and bool(int(t)) == a.get():
            point7 += 1
            if point7 == 3:
                point7 = 1
            else:
                point7 = 0
        else:
            point7 = point7
    
    # Проверка ответов номера 8
    for t, a in zip(true_answers_v1_n8, answers_v1_n8):
        if bool(int(t)) and bool(int(t)) == a.get():
            point8 += 1
        else:
            point8 = point8
    
    # Проверка ответов номера 9
    for t, a in zip(true_answers_v1_n9, answers_v1_n9):
        if bool(int(t)) and bool(int(t)) == a.get():
            point9 += 1
        else:
            point9 = point9

    # Проверка ответов номера 10
    for t, a in zip(true_answers_v1_n10, answers_v1_n10):
        if bool(int(t)) and bool(int(t)) == a.get():
            point10 += 1
        else:
            point10 = point10
    
    # Проверка ответов номера 11
    for t, a in zip(true_answers_v1_n11, answers_v1_n11):
        if bool(int(t)) and bool(int(t)) == a.get():
            point11 += 1
        else:
            point11 = point11

    # Подсчет обещго балла
    a = point1 + point2 + point3 + point4 + point5 + point6 + point7 + point8 + point9 + point10 + point11
 
    # Подсчет оценки
    if a >= 0 and a <= 3:
        score = 2
    elif a >= 4 and a <= 6:
        score = 3
    elif a >= 7 and a <= 9:
        score = 4
    else:
        score = 5

    # Удаление прошлой таблички и вывод балла/оценки
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text=f"Ваш балл: {a}").pack()
    Label(el, text=f"Ваша оценка: {score}").pack()

# Вопрос варианта 1 номера 1
def question_v1_n1(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="Какие виды компьютерной графики существуют?\nВыберите несколько вариантов ответа.").pack()

    answers_v1_n1.append(BooleanVar())
    Checkbutton(el, text="Векторная", variable=answers_v1_n1[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n1.append(BooleanVar())
    Checkbutton(el, text="Растровая", variable=answers_v1_n1[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n1.append(BooleanVar())
    Checkbutton(el, text="Фрактальная", variable=answers_v1_n1[2], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n1.append(BooleanVar())
    Checkbutton(el, text="Трехмерная", variable=answers_v1_n1[3], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n1.append(BooleanVar())
    Checkbutton(el, text="Двухуровневая", variable=answers_v1_n1[4], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n1.append(BooleanVar())
    Checkbutton(el, text="Фактическая", variable=answers_v1_n1[5], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n1.append(BooleanVar())
    Checkbutton(el, text="Практическая", variable=answers_v1_n1[6], onvalue=1, offvalue=0).pack(anchor=W)
    
    Button(el, text="Следующий", command=lambda e=el: question_v1_n2(e)).pack()
        
# Вопрос варианта 1 номера 2
def question_v1_n2(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="Что такое компьютерная графика?\nВыберите один из вариантов ответа.").pack()
    answers_v1_n2.append(BooleanVar())
    Checkbutton(el, text="Специальная область информатики, которая изучает методы и способы создания и обработки изображений", variable=answers_v1_n2[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n2.append(BooleanVar())
    Checkbutton(el, text="Комплекс программного обеспечения для подготовки иллюстрированного материала", variable=answers_v1_n2[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n2.append(BooleanVar())
    Checkbutton(el, text="Специальная область информатики, изучающая способы и методы кодирования информации", variable=answers_v1_n2[2], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n2.append(BooleanVar())
    Checkbutton(el, text="Способ кодирования графической информации с использованием вычислительной техники", variable=answers_v1_n2[3], onvalue=1, offvalue=0).pack(anchor=W)

    Button(el, text="Следующий", command=lambda e=el: question_v1_n3(e)).pack()

# Вопрос варианта 1 номера 3
def question_v1_n3(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="Какую форму имеет пиксель\nВыберите один из вариантов ответа.").pack()

    answers_v1_n3.append(BooleanVar())
    Checkbutton(el, text="Круг", variable=answers_v1_n3[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n3.append(BooleanVar())
    Checkbutton(el, text="Квадрат", variable=answers_v1_n3[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n3.append(BooleanVar())
    Checkbutton(el, text="Овал", variable=answers_v1_n3[2], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n3.append(BooleanVar())
    Checkbutton(el, text="Треугольник", variable=answers_v1_n3[3], onvalue=1, offvalue=0).pack(anchor=W)

    Button(el, text="Следующий", command=lambda e=el: question_v1_n4(e)).pack()

# Вопрос варианта 1 номера 4
def question_v1_n4(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="От какого словосочетания образовалось слово 'пискель'?\nВыберите один из вариантов ответа.").pack()

    answers_v1_n4.append(BooleanVar())
    Checkbutton(el, text="Разрешение", variable=answers_v1_n4[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n4.append(BooleanVar())
    Checkbutton(el, text="Линия", variable=answers_v1_n4[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n4.append(BooleanVar())
    Checkbutton(el, text="Элемент картинки", variable=answers_v1_n4[2], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n4.append(BooleanVar())
    Checkbutton(el, text="Формат картинки", variable=answers_v1_n4[3], onvalue=1, offvalue=0).pack(anchor=W)

    Button(el, text="Следующий", command=lambda e=el: question_v1_n5(e)).pack()

# Вопрос варианта 1 номера 5
def question_v1_n5(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="Как называется эффект, который наблюдается при увеличении масштаба растрового изображения?\nВыберите один из вариантов ответа.").pack()

    answers_v1_n5.append(BooleanVar())
    Checkbutton(el, text="Деформация", variable=answers_v1_n5[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n5.append(BooleanVar())
    Checkbutton(el, text="Растеризация", variable=answers_v1_n5[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n5.append(BooleanVar())
    Checkbutton(el, text="Пикселизация", variable=answers_v1_n5[2], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n5.append(BooleanVar())
    Checkbutton(el, text="Векторизация", variable=answers_v1_n5[3], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n5.append(BooleanVar())
    Checkbutton(el, text="Визуализация", variable=answers_v1_n5[4], onvalue=1, offvalue=0).pack(anchor=W)

    Button(el, text="Следующий", command=lambda e=el: question_v1_n6(e)).pack()

# Вопрос варианта 1 номера 6
def question_v1_n6(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="Что такое разрешение?\nВыберите один из вариантов ответа.").pack()

    answers_v1_n6.append(BooleanVar())
    Checkbutton(el, text="Это количество точек в изображении", variable=answers_v1_n6[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n6.append(BooleanVar())
    Checkbutton(el, text="Это количество точек, приходящееся на единицу длины", variable=answers_v1_n6[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n6.append(BooleanVar())
    Checkbutton(el, text="Это количество пикселей по горизонтали и вертикали", variable=answers_v1_n6[2], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n6.append(BooleanVar())
    Checkbutton(el, text="Это минимальный элемент растрового изображения", variable=answers_v1_n6[3], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n6.append(BooleanVar())
    Checkbutton(el, text="Это минимальный элемент векторного изображения", variable=answers_v1_n6[4], onvalue=1, offvalue=0).pack(anchor=W)
    
    Button(el, text="Следующий", command=lambda e=el: question_v1_n7(e)).pack()

# Вопрос варианта 1 номера 7
def question_v1_n7(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="Какие различают виды разрешений?\nВыберите один из вариантов ответа.").pack()

    answers_v1_n7.append(BooleanVar())
    Checkbutton(el, text="Разрешение оригинала", variable=answers_v1_n7[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n7.append(BooleanVar())
    Checkbutton(el, text="Разрешение печатного изображения ", variable=answers_v1_n7[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n7.append(BooleanVar())
    Checkbutton(el, text="Разрешение экранного изображения", variable=answers_v1_n7[2], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n7.append(BooleanVar())
    Checkbutton(el, text="Разрешение сканированного изображения", variable=answers_v1_n7[3], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n7.append(BooleanVar())
    Checkbutton(el, text="Разрешение бумажного изображения", variable=answers_v1_n7[4], onvalue=1, offvalue=0).pack(anchor=W)
    
    Button(el, text="Следующий", command=lambda e=el: question_v1_n8(e)).pack()

# Вопрос варианта 1 номера 8
def question_v1_n8(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="Какой вид разрешения важен при сканирования изображения?\nВыберите несколько вариантов ответа.").pack()

    answers_v1_n8.append(BooleanVar())
    Checkbutton(el, text="Разрешение оригинала", variable=answers_v1_n8[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n8.append(BooleanVar())
    Checkbutton(el, text="Разрешение печатного изображения ", variable=answers_v1_n8[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n8.append(BooleanVar())
    Checkbutton(el, text="Разрешение экранного изображения", variable=answers_v1_n8[2], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n8.append(BooleanVar())
    Checkbutton(el, text="Разрешение сканированного изображения", variable=answers_v1_n8[3], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n8.append(BooleanVar())
    Checkbutton(el, text="Разрешение бумажного изображения", variable=answers_v1_n8[4], onvalue=1, offvalue=0).pack(anchor=W)
    
    Button(el, text="Следующий", command=lambda e=el: question_v1_n9(e)).pack()

# Вопрос варианта 1 номера 9
def question_v1_n9(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="Что такое DPI?\nВыберите один из вариантов ответа.").pack()

    answers_v1_n9.append(BooleanVar())
    Checkbutton(el, text="Количество точек на дюйм, в них измеряется разрешение оригинала", variable=answers_v1_n9[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n9.append(BooleanVar())
    Checkbutton(el, text="Количество пикселей на экране по горизонтали и вертикали, в них измеряется разрешение экранного", variable=answers_v1_n9[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n9.append(BooleanVar())
    Checkbutton(el, text="Количество линий на дюйм, в них измеряется разрешение оригинала", variable=answers_v1_n9[2], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n9.append(BooleanVar())
    Checkbutton(el, text="Количество линий на дюйм. в них измеряется разрешение печатного изображений", variable=answers_v1_n9[3], onvalue=1, offvalue=0).pack(anchor=W)
    
    Button(el, text="Следующий", command=lambda e=el: question_v1_n10(e)).pack()

# Вопрос варианта 1 номера 10
def question_v1_n10(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="Экранное разрешение указывает.\nВыберите один из вариантов ответа.").pack()

    answers_v1_n10.append(BooleanVar())
    Checkbutton(el, text="Количество точек на экране, приходящееся на один дюйм изображения", variable=answers_v1_n10[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n10.append(BooleanVar())
    Checkbutton(el, text="Количество точек на экране, приходящееся на один дюйм изображения", variable=answers_v1_n10[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n10.append(BooleanVar())
    Checkbutton(el, text="Количество точек на экране, приходящееся на один дюйм изображения", variable=answers_v1_n10[2], onvalue=1, offvalue=0).pack(anchor=W)

    Button(el, text="Следующий", command=lambda e=el: question_v1_n11(e)).pack()

# Вопрос варианта 1 номера 11
def question_v1_n11(el):
    for widget in el.winfo_children():
        widget.destroy()
    Label(el, text="Что такое LPI?\nВыберите один из вариантов ответа.").pack()

    answers_v1_n11.append(BooleanVar())
    Checkbutton(el, text="Количество точек на дюйм, в них измеряется разрешение оригинала", variable=answers_v1_n11[0], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n11.append(BooleanVar())
    Checkbutton(el, text="Количество пикселей на экране по горизонтали и вертикали, в них измеряется разрешение экранного", variable=answers_v1_n11[1], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n11.append(BooleanVar())
    Checkbutton(el, text="Количество линий на дюйм, в них измеряется разрешение оригинала", variable=answers_v1_n11[2], onvalue=1, offvalue=0).pack(anchor=W)
    answers_v1_n11.append(BooleanVar())
    Checkbutton(el, text="Количество линий на дюйм. в них измеряется разрешение печатного изображений", variable=answers_v1_n11[3], onvalue=1, offvalue=0).pack(anchor=W)

    Button(el, text="Закончить", command=lambda e=el: check_v1(e)).pack()

first(label)
label.pack()
window.mainloop()