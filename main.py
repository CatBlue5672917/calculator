from tkinter import *

root = Tk()

root.title('Калькулятор')
root.geometry("300x400")
root['bg'] = 'white'

bg_num = "black"
fg_num = "white"
font_num = "Arial 25"
font_num_text = "Arial 20"
error = 'Ошибка!'

data = ''

def buttonOneIsPushed():
    global data
    data = data + "1"
    lbl1.configure(text=data)
def buttonTwoIsPushed():
    global data
    data = data + "2"
    lbl1.configure(text=data)
def buttonThreeIsPushed():
    global data
    data = data + "3"
    lbl1.configure(text=data)
def buttonFourIsPushed():
    global data
    data = data + "4"
    lbl1.configure(text=data)
def buttonFiveIsPushed():
    global data
    data = data + "5"
    lbl1.configure(text=data)
def buttonSixIsPushed():
    global data
    data = data + "6"
    lbl1.configure(text=data)
def buttonSevenIsPushed():
    global data
    data = data + "7"
    lbl1.configure(text=data)
def buttonEightIsPushed():
    global data
    data = data + "8"
    lbl1.configure(text=data)
def buttonNineIsPushed():
    global data
    data = data + "9"
    lbl1.configure(text=data)
def buttonNullIsPushed():
    global data
    data = data + "0"
    lbl1.configure(text=data)
def buttonPlus():
    global data
    data = data + "+"
    lbl1.configure(text=data)
def buttonMinus():
    global data
    data = data + "-"
    lbl1.configure(text=data)
def buttonX():
    global data
    data = data + "x"
    lbl1.configure(text=data)
def buttonD():
    global data
    data = data + "/"
    lbl1.configure(text=data)
def erase():
    data = ''
    lbl1.configure(text='0')

def printR():
    global data, result, lbl1
    if data.__contains__('+'):
        split = data.split('+')
        if len(split) == 2:
            result = int(split[0]) + int(split[1])
        else:
            lbl1.configure(text=error)
            result = 0
    elif data.__contains__('-'):
        split = data.split('-')
        if len(split) == 2:
            result = int(split[0]) - int(split[1])
        else:
            lbl1.configure(text=error)
            result = 0
    elif data.__contains__('x'):
        split = data.split('x')
        if len(split) == 2:
            result = int(split[0]) * int(split[1])
        else:
            lbl1.configure(text=error)
            result = 0
    elif data.__contains__('/'):
        split = data.split('/')
        if len(split) == 2:
            result = int(split[0]) / int(split[1])
        else:
            lbl1.configure(text=error)
            result = 0
    else:
        lbl1.configure(text=error)

    data = str(result)
    result = 0
    lbl1.configure(text=data)
    data = ''


button1 = Button(root, text="1", font=font_num, bg=bg_num, fg=fg_num, command=buttonOneIsPushed)
button2 = Button(root, text="2", font=font_num, bg=bg_num, fg=fg_num, command=buttonTwoIsPushed)
button3 = Button(root, text="3", font=font_num, bg=bg_num, fg=fg_num, command=buttonThreeIsPushed)
button4 = Button(root, text="4", font=font_num, bg=bg_num, fg=fg_num, command=buttonFourIsPushed)
button5 = Button(root, text="5", font=font_num, bg=bg_num, fg=fg_num, command=buttonFiveIsPushed)
button6 = Button(root, text="6", font=font_num, bg=bg_num, fg=fg_num, command=buttonSixIsPushed)
button7 = Button(root, text="7", font=font_num, bg=bg_num, fg=fg_num, command=buttonSevenIsPushed)
button8 = Button(root, text="8", font=font_num, bg=bg_num, fg=fg_num, command=buttonEightIsPushed)
button9 = Button(root, text="9", font=font_num, bg=bg_num, fg=fg_num, command=buttonNineIsPushed)
button0 = Button(root, text="0", font=font_num, bg=bg_num, fg=fg_num, command=buttonNullIsPushed)
buttonX = Button(root, text="* ", font=font_num, bg=bg_num, fg=fg_num, command=buttonX)
buttonD = Button(root, text="/ ", font=font_num, bg=bg_num, fg=fg_num, command=buttonD)
buttonP = Button(root, text="+", font=font_num, bg=bg_num, fg=fg_num, command=buttonPlus)
buttonM = Button(root, text="- ", font=font_num, bg=bg_num, fg=fg_num, command=buttonMinus)
buttonR = Button(root, text="=", font=font_num, bg=bg_num, fg=fg_num, command=printR)
buttonC = Button(root, text="C", font=font_num, bg=bg_num, fg=fg_num, command=erase)
lbl1 = Label(root, text="0", font=font_num_text, bg="white")

lbl1.grid(column=2, row=1)

button1.grid(column=1, row=2)
button2.grid(column=2, row=2)
button3.grid(column=3, row=2)
button4.grid(column=1, row=3)
button5.grid(column=2, row=3)
button6.grid(column=3, row=3)
button7.grid(column=1, row=4)
button8.grid(column=2, row=4)
button9.grid(column=3, row=4)
button0.grid(column=2, row=5)

buttonD.grid(column=4, row=2)
buttonX.grid(column=4,row=3)
buttonM.grid(column=4,row=4)
buttonP.grid(column=4,row=5)
buttonR.grid(column=3,row=5)
buttonC.grid(column=1, row=5)

root.mainloop()