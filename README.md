# EN | Test work on design
The test work on the design includes 3 options for 11 questions each. At the end of each option, the total number of points and the score are calculated. The program is written in Python version 3.10.5. Libraries used:
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

# How the code works?
Install the necessary libraries.
```python
from tkinter import *
from tkinter.ttk import *
```
In the first three lines, we create a window, assign it a name and dimensions.
```python
window = Tk()
window.title("Тестовая работа")
window.geometry("1000x500")
```

The whole code repeats, so I'll take the first number of the first option as an example.
In the first line we create a point for scoring, in the second line for the user's response and in the third line the answer itself.
```python
point1 = 0
answers_v1_n1 = []
true_answers_v1_n1 = "1111000" # Ответ на вариант 1, номер 1
```

Next to the code, by pressing the "Вариант №1" button, the user's answers are collected and at the end of the test, scores and grades are calculated.


```python
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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Подсчет обещего балла
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
```

## An example of how the program works:

![image](https://user-images.githubusercontent.com/64695348/235352251-eeae3240-ab51-4fd1-a4d7-32c070179589.png)
![image](https://user-images.githubusercontent.com/64695348/235352232-6ef8d59f-3490-4006-92ca-7ecc7a75f909.png)
![image](https://user-images.githubusercontent.com/64695348/235352294-7bb2209c-2be1-42c9-89b2-5866328c9d75.png)

This work was written under the order for the school CODOLOGIA.
 
# RU | Тестовая работа по дизайну
Тестовая работа по дизайну, включает в себя 3 вариннта по 11 вопросов в каждом. В конце каждого варианта подсчитывается общее количество баллов и оценка. Программа написана на Python версии 3.10.5. Используемые библиотеки:
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

# Как работает код?
Устанавливаем необходимые библиотеки
```python
from tkinter import *
from tkinter.ttk import *
```

В первых трех строках мы создаем окно, присваиваем ему название и размеры.
```python
window = Tk()
window.title("Тестовая работа")
window.geometry("1000x500")
```

Весь код повторяется, поэтому для примера возьму первый номер первого варианта.
В первой строке мы создаем поинт для подсчета балла, во второй строке для ответа пользователя и третьей строке сам ответ.

```python
point1 = 0
answers_v1_n1 = []
true_answers_v1_n1 = "1111000" # Ответ на вариант 1, номер 1
```

Далее к коде по нажатию кнопки "Вариант №1", идет сбор ответов пользователя и по окончанию сдачи теста, идет подсчет баллов и оценки.

```python
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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Подсчет обещего балла
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
```

## Пример того, как работает программа:

![image](https://user-images.githubusercontent.com/64695348/235352251-eeae3240-ab51-4fd1-a4d7-32c070179589.png)
![image](https://user-images.githubusercontent.com/64695348/235352232-6ef8d59f-3490-4006-92ca-7ecc7a75f909.png)
![image](https://user-images.githubusercontent.com/64695348/235352294-7bb2209c-2be1-42c9-89b2-5866328c9d75.png)

Работа написана по заказу школы CODOLOGIA.
