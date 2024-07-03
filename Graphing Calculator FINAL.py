from math import *
import sympy as smp
from tkinter import *
import ctypes
from tkinter.font import Font

root = Tk()
root.title("Graphing Calculator")
root.iconbitmap('Assets/Icon.ico')
root.state('zoomed')
root.attributes("-fullscreen", True)

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

titleFont = Font(family="Cambria Math", size=44, weight="bold")
headingFont = Font(family="Cambria Math", size=36, weight="bold")
buttonFont = Font(family="Times New Roman")
boldFont = Font(family="Times New Roman", weight="bold")

diffImage = PhotoImage(file='Assets/Differentiation.png')
intImage = PhotoImage(file='Assets/Integration.png')
darkDiffImage = PhotoImage(file='Assets/darkDifferentiation.png')
darkIntImage = PhotoImage(file='Assets/darkIntegration.png')

ddxImage = PhotoImage(file='Assets/thinDifferentiation.png')
intgrlImage = PhotoImage(file='Assets/thinIntegration.png')
dxImage = PhotoImage(file='Assets/dx.png')
darkDdxImage = PhotoImage(file='Assets/thinDarkDifferentiation.png')
darkIntgrlImage = PhotoImage(file='Assets/thinDarkIntegration.png')
darkDxImage = PhotoImage(file='Assets/darkDx.png')

darkMode = False
language = 0

numberPressed = False
closingBracketPressed = False
zoom = 1.0
counter = 0

colour=['', '#ff0000', '#0000ff', '#00bb00', '#ff00ff', '#ff9900', '#ff0000', '#0000ff', '#00bb00', '#ff00ff', '#ff9900', '#ff0000', '#0000ff', '#00bb00', '#ff00ff', '#ff9900', '#ff0000', '#0000ff', '#00bb00', '#ff00ff', '#ff9900']
lineExists = [False] * 21
equation1 = ""

def changecolour1():
    global colour
    global colourButton1
    if colour[1] == '#ff0000':
        colour[1] = '#0000ff'
    elif colour[1] == '#0000ff':
        colour[1] = '#00bb00'
    elif colour[1] == '#00bb00':
        colour[1] = '#ff00ff'
    elif colour[1] == '#ff00ff':
        colour[1] = '#ff9900'
    elif colour[1] == '#ff9900':
        colour[1] = '#ff0000'
    colourButton1.configure(fg=colour[1], activeforeground=colour[1])

def changecolour2():
    global colour
    global colourButton2
    if colour[2] == '#ff0000':
        colour[2] = '#0000ff'
    elif colour[2] == '#0000ff':
        colour[2] = '#00bb00'
    elif colour[2] == '#00bb00':
        colour[2] = '#ff00ff'
    elif colour[2] == '#ff00ff':
        colour[2] = '#ff9900'
    elif colour[2] == '#ff9900':
        colour[2] = '#ff0000'
    colourButton2.configure(fg=colour[2], activeforeground=colour[2])

def changecolour3():
    global colour
    global colourButton3
    if colour[3] == '#ff0000':
        colour[3] = '#0000ff'
    elif colour[3] == '#0000ff':
        colour[3] = '#00bb00'
    elif colour[3] == '#00bb00':
        colour[3] = '#ff00ff'
    elif colour[3] == '#ff00ff':
        colour[3] = '#ff9900'
    elif colour[3] == '#ff9900':
        colour[3] = '#ff0000'
    colourButton3.configure(fg=colour[3], activeforeground=colour[3])

def changecolour4():
    global colour
    global colourButton4
    if colour[4] == '#ff0000':
        colour[4] = '#0000ff'
    elif colour[4] == '#0000ff':
        colour[4] = '#00bb00'
    elif colour[4] == '#00bb00':
        colour[4] = '#ff00ff'
    elif colour[4] == '#ff00ff':
        colour[4] = '#ff9900'
    elif colour[4] == '#ff9900':
        colour[4] = '#ff0000'
    colourButton4.configure(fg=colour[4], activeforeground=colour[4])

def changecolour5():
    global colour
    global colourButton5
    if colour[5] == '#ff0000':
        colour[5] = '#0000ff'
    elif colour[5] == '#0000ff':
        colour[5] = '#00bb00'
    elif colour[5] == '#00bb00':
        colour[5] = '#ff00ff'
    elif colour[5] == '#ff00ff':
        colour[5] = '#ff9900'
    elif colour[5] == '#ff9900':
        colour[5] = '#ff0000'
    colourButton5.configure(fg=colour[5], activeforeground=colour[5])

def changecolour6():
    global colour
    global colourButton6
    if colour[6] == '#ff0000':
        colour[6] = '#0000ff'
    elif colour[6] == '#0000ff':
        colour[6] = '#00bb00'
    elif colour[6] == '#00bb00':
        colour[6] = '#ff00ff'
    elif colour[6] == '#ff00ff':
        colour[6] = '#ff9900'
    elif colour[6] == '#ff9900':
        colour[6] = '#ff0000'
    colourButton6.configure(fg=colour[6], activeforeground=colour[6])

def changecolour7():
    global colour
    global colourButton7
    if colour[7] == '#ff0000':
        colour[7] = '#0000ff'
    elif colour[7] == '#0000ff':
        colour[7] = '#00bb00'
    elif colour[7] == '#00bb00':
        colour[7] = '#ff00ff'
    elif colour[7] == '#ff00ff':
        colour[7] = '#ff9900'
    elif colour[7] == '#ff9900':
        colour[7] = '#ff0000'
    colourButton7.configure(fg=colour[7], activeforeground=colour[7])

def changecolour8():
    global colour
    global colourButton8
    if colour[8] == '#ff0000':
        colour[8] = '#0000ff'
    elif colour[8] == '#0000ff':
        colour[8] = '#00bb00'
    elif colour[8] == '#00bb00':
        colour[8] = '#ff00ff'
    elif colour[8] == '#ff00ff':
        colour[8] = '#ff9900'
    elif colour[8] == '#ff9900':
        colour[8] = '#ff0000'
    colourButton8.configure(fg=colour[8], activeforeground=colour[8])

def changecolour9():
    global colour
    global colourButton9
    if colour[9] == '#ff0000':
        colour[9] = '#0000ff'
    elif colour[9] == '#0000ff':
        colour[9] = '#00bb00'
    elif colour[9] == '#00bb00':
        colour[9] = '#ff00ff'
    elif colour[9] == '#ff00ff':
        colour[9] = '#ff9900'
    elif colour[9] == '#ff9900':
        colour[9] = '#ff0000'
    colourButton9.configure(fg=colour[9], activeforeground=colour[9])

def changecolour10():
    global colour
    global colourButton10
    if colour[10] == '#ff0000':
        colour[10] = '#0000ff'
    elif colour[10] == '#0000ff':
        colour[10] = '#00bb00'
    elif colour[10] == '#00bb00':
        colour[10] = '#ff00ff'
    elif colour[10] == '#ff00ff':
        colour[10] = '#ff9900'
    elif colour[10] == '#ff9900':
        colour[10] = '#ff0000'
    colourButton10.configure(fg=colour[10], activeforeground=colour[10])

def changecolour11():
    global colour
    global colourButton11
    if colour[11] == '#ff0000':
        colour[11] = '#0000ff'
    elif colour[11] == '#0000ff':
        colour[11] = '#00bb00'
    elif colour[11] == '#00bb00':
        colour[11] = '#ff00ff'
    elif colour[11] == '#ff00ff':
        colour[11] = '#ff9900'
    elif colour[11] == '#ff9900':
        colour[11] = '#ff0000'
    colourButton11.configure(fg=colour[11], activeforeground=colour[11])

def changecolour12():
    global colour
    global colourButton12
    if colour[12] == '#ff0000':
        colour[12] = '#0000ff'
    elif colour[12] == '#0000ff':
        colour[12] = '#00bb00'
    elif colour[12] == '#00bb00':
        colour[12] = '#ff00ff'
    elif colour[12] == '#ff00ff':
        colour[12] = '#ff9900'
    elif colour[12] == '#ff9900':
        colour[12] = '#ff0000'
    colourButton12.configure(fg=colour[12], activeforeground=colour[12])

def changecolour13():
    global colour
    global colourButton13
    if colour[13] == '#ff0000':
        colour[13] = '#0000ff'
    elif colour[13] == '#0000ff':
        colour[13] = '#00bb00'
    elif colour[13] == '#00bb00':
        colour[13] = '#ff00ff'
    elif colour[13] == '#ff00ff':
        colour[13] = '#ff9900'
    elif colour[13] == '#ff9900':
        colour[13] = '#ff0000'
    colourButton13.configure(fg=colour[13], activeforeground=colour[13])

def changecolour14():
    global colour
    global colourButton14
    if colour[14] == '#ff0000':
        colour[14] = '#0000ff'
    elif colour[14] == '#0000ff':
        colour[14] = '#00bb00'
    elif colour[14] == '#00bb00':
        colour[14] = '#ff00ff'
    elif colour[14] == '#ff00ff':
        colour[14] = '#ff9900'
    elif colour[14] == '#ff9900':
        colour[14] = '#ff0000'
    colourButton14.configure(fg=colour[14], activeforeground=colour[14])

def changecolour15():
    global colour
    global colourButton15
    if colour[15] == '#ff0000':
        colour[15] = '#0000ff'
    elif colour[15] == '#0000ff':
        colour[15] = '#00bb00'
    elif colour[15] == '#00bb00':
        colour[15] = '#ff00ff'
    elif colour[15] == '#ff00ff':
        colour[15] = '#ff9900'
    elif colour[15] == '#ff9900':
        colour[15] = '#ff0000'
    colourButton15.configure(fg=colour[15], activeforeground=colour[15])

def changecolour16():
    global colour
    global colourButton16
    if colour[16] == '#ff0000':
        colour[16] = '#0000ff'
    elif colour[16] == '#0000ff':
        colour[16] = '#00bb00'
    elif colour[16] == '#00bb00':
        colour[16] = '#ff00ff'
    elif colour[16] == '#ff00ff':
        colour[16] = '#ff9900'
    elif colour[16] == '#ff9900':
        colour[16] = '#ff0000'
    colourButton16.configure(fg=colour[16], activeforeground=colour[16])

def changecolour17():
    global colour
    global colourButton17
    if colour[17] == '#ff0000':
        colour[17] = '#0000ff'
    elif colour[17] == '#0000ff':
        colour[17] = '#00bb00'
    elif colour[17] == '#00bb00':
        colour[17] = '#ff00ff'
    elif colour[17] == '#ff00ff':
        colour[17] = '#ff9900'
    elif colour[17] == '#ff9900':
        colour[17] = '#ff0000'
    colourButton17.configure(fg=colour[17], activeforeground=colour[17])

def changecolour18():
    global colour
    global colourButton18
    if colour[18] == '#ff0000':
        colour[18] = '#0000ff'
    elif colour[18] == '#0000ff':
        colour[18] = '#00bb00'
    elif colour[18] == '#00bb00':
        colour[18] = '#ff00ff'
    elif colour[18] == '#ff00ff':
        colour[18] = '#ff9900'
    elif colour[18] == '#ff9900':
        colour[18] = '#ff0000'
    colourButton18.configure(fg=colour[18], activeforeground=colour[18])

def changecolour19():
    global colour
    global colourButton19
    if colour[19] == '#ff0000':
        colour[19] = '#0000ff'
    elif colour[19] == '#0000ff':
        colour[19] = '#00bb00'
    elif colour[19] == '#00bb00':
        colour[19] = '#ff00ff'
    elif colour[19] == '#ff00ff':
        colour[19] = '#ff9900'
    elif colour[19] == '#ff9900':
        colour[19] = '#ff0000'
    colourButton19.configure(fg=colour[19], activeforeground=colour[19])

def changecolour20():
    global colour
    global colourButton20
    if colour[20] == '#ff0000':
        colour[20] = '#0000ff'
    elif colour[20] == '#0000ff':
        colour[20] = '#00bb00'
    elif colour[20] == '#00bb00':
        colour[20] = '#ff00ff'
    elif colour[20] == '#ff00ff':
        colour[20] = '#ff9900'
    elif colour[20] == '#ff9900':
        colour[20] = '#ff0000'
    colourButton20.configure(fg=colour[20], activeforeground=colour[20])

graphFrame = Frame(root, width=screensize[0], height=screensize[1])

backButton = Button(graphFrame, text="Back", command=lambda:[graphFrame.place_forget(), mainMenu()])
backButton.place(relx=0.025, rely=0.05, anchor=NW)
backButton.config(font=buttonFont)

equationsLabel = Label(graphFrame, text="Equations")
equationsLabel.place(relx=0.25, rely=0.09, anchor=CENTER)
equationsLabel.config(font=headingFont)


def output1():
    global line1
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line1[i])
    equation1 = expression1.get()
    lineExists[1] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = ((i - screensize[0]/4)/(screensize[0]/40))/zoom
        try:
            y = (eval(equation1, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line1[i] = graph.create_line(prevx, prevy, i, y, fill=colour[1], width=4)
            else:
                line1[i] = graph.create_line(prevx, prevy, i, y, fill=colour[1], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression2.place(relx=0.21, rely=0.2, anchor=E)
    expression2.focus_set()
    yLabel2.place(relx=0.055, rely=0.2, anchor=CENTER)
    expressionButton2.place(relx=0.25, rely=0.2, anchor=E)
    colourButton2.place(relx=0.23, rely=0.2, anchor=E)

expression1 = Entry(graphFrame, width=30)
expression1.place(relx=0.21, rely=0.15, anchor=E)

yLabel1 = Label(graphFrame, text="y =")
yLabel1.place(relx=0.055, rely=0.15, anchor=CENTER)
yLabel1.config(font=buttonFont)

colourButton1 = Button(graphFrame, text="■", fg=colour[1], activeforeground=colour[1], width=2, command=changecolour1)
colourButton1.place(relx=0.23, rely=0.15, anchor=E)

expressionButton1 = Button(graphFrame, text="✓", command=output1)
expressionButton1.place(relx=0.25, rely=0.15, anchor=E)

def output2():
    global line2
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line2[i])
    equation2 = expression2.get()
    lineExists[2] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation2, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line2[i] = graph.create_line(prevx, prevy, i, y, fill=colour[2], width=4)
            else:
                line2[i] = graph.create_line(prevx, prevy, i, y, fill=colour[2], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression3.place(relx=0.21, rely=0.25, anchor=E)
    expression3.focus_set()
    yLabel3.place(relx=0.055, rely=0.25, anchor=CENTER)
    expressionButton3.place(relx=0.25, rely=0.25, anchor=E)
    colourButton3.place(relx=0.23, rely=0.25, anchor=E)



expression2 = Entry(graphFrame, width=30)

colourButton2 = Button(graphFrame, text="■", fg=colour[2], activeforeground=colour[2], width=2, command=changecolour2)

expressionButton2 = Button(graphFrame, text="✓", command=output2)

yLabel2 = Label(graphFrame, text="y =")
yLabel2.config(font=buttonFont)


def output3():
    global line3
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line3[i])
    equation3 = expression3.get()
    lineExists[3] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation3, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line3[i] = graph.create_line(prevx, prevy, i, y, fill=colour[3], width=4)
            else:
                line3[i] = graph.create_line(prevx, prevy, i, y, fill=colour[3], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression4.place(relx=0.21, rely=0.3, anchor=E)
    expression4.focus_set()
    yLabel4.place(relx=0.055, rely=0.3, anchor=CENTER)
    expressionButton4.place(relx=0.25, rely=0.3, anchor=E)
    colourButton4.place(relx=0.23, rely=0.3, anchor=E)


expression3 = Entry(graphFrame, width=30)

colourButton3 = Button(graphFrame, text="■", fg=colour[3], activeforeground=colour[3], width=2, command=changecolour3)

expressionButton3 = Button(graphFrame, text="✓", command=output3)

yLabel3 = Label(graphFrame, text="y =")
yLabel3.config(font=buttonFont)

def output4():
    global line4
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line4[i])
    equation4 = expression4.get()
    lineExists[4] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation4, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line4[i] = graph.create_line(prevx, prevy, i, y, fill=colour[4], width=4)
            else:
                line4[i] = graph.create_line(prevx, prevy, i, y, fill=colour[4], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression5.place(relx=0.21, rely=0.35, anchor=E)
    expression5.focus_set()
    yLabel5.place(relx=0.055, rely=0.35, anchor=CENTER)
    expressionButton5.place(relx=0.25, rely=0.35, anchor=E)
    colourButton5.place(relx=0.23, rely=0.35, anchor=E)


expression4 = Entry(graphFrame, width=30)

colourButton4 = Button(graphFrame, text="■", fg=colour[4], activeforeground=colour[4], width=2, command=changecolour4)

expressionButton4 = Button(graphFrame, text="✓", command=output4)

yLabel4 = Label(graphFrame, text="y =")
yLabel4.config(font=buttonFont)

def output5():
    global line5
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line5[i])
    equation5 = expression5.get()
    lineExists[5] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation5, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line5[i] = graph.create_line(prevx, prevy, i, y, fill=colour[5], width=4)
            else:
                line5[i] = graph.create_line(prevx, prevy, i, y, fill=colour[5], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression6.place(relx=0.21, rely=0.4, anchor=E)
    expression6.focus_set()
    yLabel6.place(relx=0.055, rely=0.4, anchor=CENTER)
    expressionButton6.place(relx=0.25, rely=0.4, anchor=E)
    colourButton6.place(relx=0.23, rely=0.4, anchor=E)


expression5 = Entry(graphFrame, width=30)

colourButton5 = Button(graphFrame, text="■", fg=colour[5], activeforeground=colour[5], width=2, command=changecolour5)

expressionButton5 = Button(graphFrame, text="✓", command=output5)

yLabel5 = Label(graphFrame, text="y =")
yLabel5.config(font=buttonFont)

def output6():
    global line6
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line6[i])
    equation6 = expression6.get()
    lineExists[6] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation6, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line6[i] = graph.create_line(prevx, prevy, i, y, fill=colour[6], width=4)
            else:
                line6[i] = graph.create_line(prevx, prevy, i, y, fill=colour[6], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression7.place(relx=0.21, rely=0.45, anchor=E)
    expression7.focus_set()
    yLabel7.place(relx=0.055, rely=0.45, anchor=CENTER)
    expressionButton7.place(relx=0.25, rely=0.45, anchor=E)
    colourButton7.place(relx=0.23, rely=0.45, anchor=E)


expression6 = Entry(graphFrame, width=30)

colourButton6 = Button(graphFrame, text="■", fg=colour[6], activeforeground=colour[6], width=2, command=changecolour6)

expressionButton6 = Button(graphFrame, text="✓", command=output6)

yLabel6 = Label(graphFrame, text="y =")
yLabel6.config(font=buttonFont)

def output7():
    global line7
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line7[i])
    equation7 = expression7.get()
    lineExists[7] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation7, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line7[i] = graph.create_line(prevx, prevy, i, y, fill=colour[7], width=4)
            else:
                line7[i] = graph.create_line(prevx, prevy, i, y, fill=colour[7], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression8.place(relx=0.21, rely=0.5, anchor=E)
    expression8.focus_set()
    yLabel8.place(relx=0.055, rely=0.5, anchor=CENTER)
    expressionButton8.place(relx=0.25, rely=0.5, anchor=E)
    colourButton8.place(relx=0.23, rely=0.5, anchor=E)


expression7 = Entry(graphFrame, width=30)

colourButton7 = Button(graphFrame, text="■", fg=colour[7], activeforeground=colour[7], width=2, command=changecolour7)

expressionButton7 = Button(graphFrame, text="✓", command=output7)

yLabel7 = Label(graphFrame, text="y =")
yLabel7.config(font=buttonFont)

def output8():
    global line8
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line8[i])
    equation8 = expression8.get()
    lineExists[8] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation8, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line8[i] = graph.create_line(prevx, prevy, i, y, fill=colour[8], width=4)
            else:
                line8[i] = graph.create_line(prevx, prevy, i, y, fill=colour[8], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression9.place(relx=0.21, rely=0.55, anchor=E)
    expression9.focus_set()
    yLabel9.place(relx=0.055, rely=0.55, anchor=CENTER)
    expressionButton9.place(relx=0.25, rely=0.55, anchor=E)
    colourButton9.place(relx=0.23, rely=0.55, anchor=E)


expression8 = Entry(graphFrame, width=30)

colourButton8 = Button(graphFrame, text="■", fg=colour[8], activeforeground=colour[8], width=2, command=changecolour8)

expressionButton8 = Button(graphFrame, text="✓", command=output8)

yLabel8 = Label(graphFrame, text="y =")
yLabel8.config(font=buttonFont)

def output9():
    global line9
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line9[i])
    equation9 = expression9.get()
    lineExists[9] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation9, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line9[i] = graph.create_line(prevx, prevy, i, y, fill=colour[9], width=4)
            else:
                line9[i] = graph.create_line(prevx, prevy, i, y, fill=colour[9], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression10.place(relx=0.21, rely=0.6, anchor=E)
    expression10.focus_set()
    yLabel10.place(relx=0.055, rely=0.6, anchor=CENTER)
    expressionButton10.place(relx=0.25, rely=0.6, anchor=E)
    colourButton10.place(relx=0.23, rely=0.6, anchor=E)

expression9 = Entry(graphFrame, width=30)

colourButton9 = Button(graphFrame, text="■", fg=colour[9], activeforeground=colour[9], width=2, command=changecolour9)

expressionButton9 = Button(graphFrame, text="✓", command=output9)

yLabel9 = Label(graphFrame, text="y =")
yLabel9.config(font=buttonFont)

def output10():
    global line10
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line10[i])
    equation10 = expression10.get()
    lineExists[10] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation10, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line10[i] = graph.create_line(prevx, prevy, i, y, fill=colour[10], width=4)
            else:
                line10[i] = graph.create_line(prevx, prevy, i, y, fill=colour[10], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression11.place(relx=0.43, rely=0.15, anchor=E)
    expression11.focus_set()
    yLabel11.place(relx=0.275, rely=0.15, anchor=CENTER)
    expressionButton11.place(relx=0.47, rely=0.15, anchor=E)
    colourButton11.place(relx=0.45, rely=0.15, anchor=E)


expression10 = Entry(graphFrame, width=30)

colourButton10 = Button(graphFrame, text="■", fg=colour[10], activeforeground=colour[10], width=2, command=changecolour10)

expressionButton10 = Button(graphFrame, text="✓", command=output10)

yLabel10 = Label(graphFrame, text="y =")
yLabel10.config(font=buttonFont)

def output11():
    global line11
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line11[i])
    equation11 = expression11.get()
    lineExists[11] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation11, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line11[i] = graph.create_line(prevx, prevy, i, y, fill=colour[11], width=4)
            else:
                line11[i] = graph.create_line(prevx, prevy, i, y, fill=colour[11], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression12.place(relx=0.43, rely=0.2, anchor=E)
    expression12.focus_set()
    yLabel12.place(relx=0.275, rely=0.2, anchor=CENTER)
    expressionButton12.place(relx=0.47, rely=0.2, anchor=E)
    colourButton12.place(relx=0.45, rely=0.2, anchor=E)


expression11 = Entry(graphFrame, width=30)

colourButton11 = Button(graphFrame, text="■", fg=colour[11], activeforeground=colour[11], width=2, command=changecolour11)

expressionButton11 = Button(graphFrame, text="✓", command=output11)

yLabel11 = Label(graphFrame, text="y =")
yLabel11.config(font=buttonFont)

def output12():
    global line12
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line12[i])
    equation12 = expression12.get()
    lineExists[12] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation12, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line12[i] = graph.create_line(prevx, prevy, i, y, fill=colour[12], width=4)
            else:
                line12[i] = graph.create_line(prevx, prevy, i, y, fill=colour[12], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression13.place(relx=0.43, rely=0.25, anchor=E)
    expression13.focus_set()
    yLabel13.place(relx=0.275, rely=0.25, anchor=CENTER)
    expressionButton13.place(relx=0.47, rely=0.25, anchor=E)
    colourButton13.place(relx=0.45, rely=0.25, anchor=E)


expression12 = Entry(graphFrame, width=30)

colourButton12 = Button(graphFrame, text="■", fg=colour[12], activeforeground=colour[12], width=2, command=changecolour12)

expressionButton12 = Button(graphFrame, text="✓", command=output12)

yLabel12 = Label(graphFrame, text="y =")
yLabel12.config(font=buttonFont)

def output13():
    global line13
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line13[i])
    equation13 = expression13.get()
    lineExists[13] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation13, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line13[i] = graph.create_line(prevx, prevy, i, y, fill=colour[13], width=4)
            else:
                line13[i] = graph.create_line(prevx, prevy, i, y, fill=colour[13], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression14.place(relx=0.43, rely=0.3, anchor=E)
    expression14.focus_set()
    yLabel14.place(relx=0.275, rely=0.3, anchor=CENTER)
    expressionButton14.place(relx=0.47, rely=0.3, anchor=E)
    colourButton14.place(relx=0.45, rely=0.3, anchor=E)


expression13 = Entry(graphFrame, width=30)

colourButton13 = Button(graphFrame, text="■", fg=colour[13], activeforeground=colour[13], width=2, command=changecolour13)

expressionButton13 = Button(graphFrame, text="✓", command=output13)

yLabel13 = Label(graphFrame, text="y =")
yLabel13.config(font=buttonFont)

def output14():
    global line14
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line14[i])
    equation14 = expression14.get()
    lineExists[14] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation14, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line14[i] = graph.create_line(prevx, prevy, i, y, fill=colour[14], width=4)
            else:
                line14[i] = graph.create_line(prevx, prevy, i, y, fill=colour[14], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression15.place(relx=0.43, rely=0.35, anchor=E)
    expression15.focus_set()
    yLabel15.place(relx=0.275, rely=0.35, anchor=CENTER)
    expressionButton15.place(relx=0.47, rely=0.35, anchor=E)
    colourButton15.place(relx=0.45, rely=0.35, anchor=E)


expression14 = Entry(graphFrame, width=30)

colourButton14 = Button(graphFrame, text="■", fg=colour[14], activeforeground=colour[14], width=2, command=changecolour14)

expressionButton14 = Button(graphFrame, text="✓", command=output14)

yLabel14 = Label(graphFrame, text="y =")
yLabel14.config(font=buttonFont)

def output15():
    global line15
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line15[i])
    equation15 = expression15.get()
    lineExists[15] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation15, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line15[i] = graph.create_line(prevx, prevy, i, y, fill=colour[15], width=4)
            else:
                line15[i] = graph.create_line(prevx, prevy, i, y, fill=colour[15], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression16.place(relx=0.43, rely=0.4, anchor=E)
    expression16.focus_set()
    yLabel16.place(relx=0.275, rely=0.4, anchor=CENTER)
    expressionButton16.place(relx=0.47, rely=0.4, anchor=E)
    colourButton16.place(relx=0.45, rely=0.4, anchor=E)


expression15 = Entry(graphFrame, width=30)

colourButton15 = Button(graphFrame, text="■", fg=colour[15], activeforeground=colour[15], width=2, command=changecolour15)

expressionButton15 = Button(graphFrame, text="✓", command=output15)

yLabel15 = Label(graphFrame, text="y =")
yLabel15.config(font=buttonFont)

def output16():
    global line16
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line16[i])
    equation16 = expression16.get()
    lineExists[16] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation16, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line16[i] = graph.create_line(prevx, prevy, i, y, fill=colour[16], width=4)
            else:
                line16[i] = graph.create_line(prevx, prevy, i, y, fill=colour[16], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression17.place(relx=0.43, rely=0.45, anchor=E)
    expression17.focus_set()
    yLabel17.place(relx=0.275, rely=0.45, anchor=CENTER)
    expressionButton17.place(relx=0.47, rely=0.45, anchor=E)
    colourButton17.place(relx=0.45, rely=0.45, anchor=E)


expression16 = Entry(graphFrame, width=30)

colourButton16 = Button(graphFrame, text="■", fg=colour[16], activeforeground=colour[16], width=2, command=changecolour16)

expressionButton16 = Button(graphFrame, text="✓", command=output16)

yLabel16 = Label(graphFrame, text="y =")
yLabel16.config(font=buttonFont)

def output17():
    global line17
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line17[i])
    equation17 = expression17.get()
    lineExists[17] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation17, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line17[i] = graph.create_line(prevx, prevy, i, y, fill=colour[17], width=4)
            else:
                line17[i] = graph.create_line(prevx, prevy, i, y, fill=colour[17], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression18.place(relx=0.43, rely=0.5, anchor=E)
    expression18.focus_set()
    yLabel18.place(relx=0.275, rely=0.5, anchor=CENTER)
    expressionButton18.place(relx=0.47, rely=0.5, anchor=E)
    colourButton18.place(relx=0.45, rely=0.5, anchor=E)


expression17 = Entry(graphFrame, width=30)

colourButton17 = Button(graphFrame, text="■", fg=colour[17], activeforeground=colour[17], width=2, command=changecolour17)

expressionButton17 = Button(graphFrame, text="✓", command=output17)

yLabel17 = Label(graphFrame, text="y =")
yLabel17.config(font=buttonFont)

def output18():
    global line18
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line18[i])
    equation18 = expression18.get()
    lineExists[18] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation18, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line18[i] = graph.create_line(prevx, prevy, i, y, fill=colour[18], width=4)
            else:
                line18[i] = graph.create_line(prevx, prevy, i, y, fill=colour[18], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression19.place(relx=0.43, rely=0.55, anchor=E)
    expression19.focus_set()
    yLabel19.place(relx=0.275, rely=0.55, anchor=CENTER)
    expressionButton19.place(relx=0.47, rely=0.55, anchor=E)
    colourButton19.place(relx=0.45, rely=0.55, anchor=E)


expression18 = Entry(graphFrame, width=30)

colourButton18 = Button(graphFrame, text="■", fg=colour[18], activeforeground=colour[18], width=2, command=changecolour18)

expressionButton18 = Button(graphFrame, text="✓", command=output18)

yLabel18 = Label(graphFrame, text="y =")
yLabel18.config(font=buttonFont)

def output19():
    global line19
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line19[i])
    equation19 = expression19.get()
    lineExists[19] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation19, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line19[i] = graph.create_line(prevx, prevy, i, y, fill=colour[19], width=4)
            else:
                line19[i] = graph.create_line(prevx, prevy, i, y, fill=colour[19], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

    expression20.place(relx=0.43, rely=0.6, anchor=E)
    expression20.focus_set()
    yLabel20.place(relx=0.275, rely=0.6, anchor=CENTER)
    expressionButton20.place(relx=0.47, rely=0.6, anchor=E)
    colourButton20.place(relx=0.45, rely=0.6, anchor=E)

expression19 = Entry(graphFrame, width=30)

colourButton19 = Button(graphFrame, text="■", fg=colour[19], activeforeground=colour[19], width=2, command=changecolour19)

expressionButton19 = Button(graphFrame, text="✓", command=output19)

yLabel19 = Label(graphFrame, text="y =")
yLabel19.config(font=buttonFont)

def output20():
    global line20
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line20[i])
    equation20 = expression20.get()
    lineExists[20] = True

    prevx = 0
    prevy = 0
    error = False
    for i in range(0, int(round(screensize[0] / 2))):
        x = (i - screensize[0]/4)/(screensize[0]/40)/zoom
        try:
            y = (eval(equation20, {'x':x}, globals()))*zoom
        except ZeroDivisionError:
            error = True
        except ValueError:
            error = True
        except SyntaxError:
            pass
        else:
            y = (screensize[0]/4) - ((screensize[0]/40) * y)
            if i == 0:
                prevx = x
                prevy = y
            if error == False:
                line20[i] = graph.create_line(prevx, prevy, i, y, fill=colour[20], width=4)
            else:
                line20[i] = graph.create_line(prevx, prevy, i, y, fill=colour[20], width=0, state='hidden')
                error = False
            prevx = i
            prevy = y

expression20 = Entry(graphFrame, width=30)

colourButton20 = Button(graphFrame, text="■", fg=colour[20], activeforeground=colour[20], width=2, command=changecolour20)

expressionButton20 = Button(graphFrame, text="✓", command=output20)

yLabel20 = Label(graphFrame, text="y =")
yLabel20.config(font=buttonFont)

def callback_expression1_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression1
    numberPressed = False
    closingBracketPressed = False


def callback_expression2_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression2
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression3_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression3
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression4_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression4
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression5_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression5
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression6_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression6
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression7_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression7
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression8_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression8
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression9_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression9
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression10_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression10
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression11_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression11
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression12_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression12
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression13_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression13
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression14_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression14
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression15_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression15
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression16_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression16
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression17_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression17
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression18_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression18
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression19_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression19
    numberPressed = False
    closingBracketPressed = False
    

def callback_expression20_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = expression20
    numberPressed = False
    closingBracketPressed = False

def mouse_wheel(event):
    global zoomOutButton
    global zoomInButton
    global counter
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        counter -= 1
        if counter % 3 == 0:
            zoomOutButton.invoke()
    if event.num == 4 or event.delta == 120:
        counter -=1
        if counter % 3 == 0:
            zoomInButton.invoke()
    

def insertsymbol(text):
    global currentEntry
    currentEntry.insert(currentEntry.index(INSERT), text)

def inserttimes():
    global currentEntry
    global numberPressed
    if numberPressed == True:
        currentEntry.insert(currentEntry.index(INSERT)-1, "*")

def insertBracketTimes():
    global currentEntry
    global closingBracketPressed
    if closingBracketPressed == True:
        currentEntry.insert(currentEntry.index(INSERT)-1, "*")

def deletesymbol():
    global currentEntry
    currentEntry.delete(currentEntry.index(INSERT)-1)

def pressnumber(truth):
    global numberPressed
    if truth == 1:
        numberPressed = True
    elif truth == 0:
        numberPressed = False

def pressclosingBracket(truth):
    global closingBracketPressed
    if truth == 1:
        closingBracketPressed = True
    elif truth == 0:
        closingBracketPressed = False

def zoomIn():
    global zoom
    global zoomOutButton
    global darkMode
    if zoom < 10:
        zoom = zoom * 2
    else:
        zoomInButton["state"] = DISABLED
        zoomInButton["fg"] = "#dfdfdf"
    if zoomOutButton["state"] == DISABLED:
        zoomOutButton["state"] = ACTIVE
        if darkMode == False:
            zoomOutButton["fg"] = "#000000"
        else:
            zoomOutButton["fg"] = "#ffffff"

def zoomOut():
    global zoom
    global zoomOutButton
    if zoom > 0.0625:
        zoom = zoom / 2
    else:
        zoomOutButton["state"] = DISABLED
        zoomOutButton["fg"] = "#dfdfdf"
    if zoomInButton["state"] == DISABLED:
        zoomInButton["state"] = ACTIVE
        if  darkMode == False:
            zoomInButton["fg"] = "#000000"
        else:
            zoomInButton["fg"] = "#ffffff"
    
    
expression1.bind("<FocusIn>", callback_expression1_focus)
expression2.bind("<FocusIn>", callback_expression2_focus)
expression3.bind("<FocusIn>", callback_expression3_focus)
expression4.bind("<FocusIn>", callback_expression4_focus)
expression5.bind("<FocusIn>", callback_expression5_focus)
expression6.bind("<FocusIn>", callback_expression6_focus)
expression7.bind("<FocusIn>", callback_expression7_focus)
expression8.bind("<FocusIn>", callback_expression8_focus)
expression9.bind("<FocusIn>", callback_expression9_focus)
expression10.bind("<FocusIn>", callback_expression10_focus)
expression11.bind("<FocusIn>", callback_expression11_focus)
expression12.bind("<FocusIn>", callback_expression12_focus)
expression13.bind("<FocusIn>", callback_expression13_focus)
expression14.bind("<FocusIn>", callback_expression14_focus)
expression15.bind("<FocusIn>", callback_expression15_focus)
expression16.bind("<FocusIn>", callback_expression16_focus)
expression17.bind("<FocusIn>", callback_expression17_focus)
expression18.bind("<FocusIn>", callback_expression18_focus)
expression19.bind("<FocusIn>", callback_expression19_focus)
expression20.bind("<FocusIn>", callback_expression20_focus)



def cleargraph():
    global line1
    global line2
    global line3
    global line4
    global line5
    global line6
    global line7
    global line8
    global line9
    global line10
    global line11
    global line12
    global line13
    global line14
    global line15
    global line16
    global line17
    global line18
    global line19
    global line20
    global lineExists

    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line1[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line2[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line3[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line4[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line5[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line6[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line7[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line8[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line9[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line10[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line11[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line12[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line13[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line14[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line15[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line16[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line17[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line18[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line19[i])
    for i in range(0, int(round(screensize[0] / 2))):
        graph.delete(line20[i])

    expression1.delete(0, END)
    expression2.delete(0, END)
    expression3.delete(0, END)
    expression4.delete(0, END)
    expression5.delete(0, END)
    expression6.delete(0, END)
    expression7.delete(0, END)
    expression8.delete(0, END)
    expression9.delete(0, END)
    expression10.delete(0, END)
    expression11.delete(0, END)
    expression12.delete(0, END)
    expression13.delete(0, END)
    expression14.delete(0, END)
    expression15.delete(0, END)
    expression16.delete(0, END)
    expression17.delete(0, END)
    expression18.delete(0, END)
    expression19.delete(0, END)
    expression20.delete(0, END)

    expression2.place_forget()
    yLabel2.place_forget()
    expressionButton2.place_forget()
    colourButton2.place_forget()

    expression3.place_forget()
    yLabel3.place_forget()
    expressionButton3.place_forget()
    colourButton3.place_forget()

    expression4.place_forget()
    yLabel4.place_forget()
    expressionButton4.place_forget()
    colourButton4.place_forget()

    expression5.place_forget()
    yLabel5.place_forget()
    expressionButton5.place_forget()
    colourButton5.place_forget()

    expression6.place_forget()
    yLabel6.place_forget()
    expressionButton6.place_forget()
    colourButton6.place_forget()

    expression7.place_forget()
    yLabel7.place_forget()
    expressionButton7.place_forget()
    colourButton7.place_forget()

    expression8.place_forget()
    yLabel8.place_forget()
    expressionButton8.place_forget()
    colourButton8.place_forget()

    expression9.place_forget()
    yLabel9.place_forget()
    expressionButton9.place_forget()
    colourButton9.place_forget()

    expression10.place_forget()
    yLabel10.place_forget()
    expressionButton10.place_forget()
    colourButton10.place_forget()

    expression11.place_forget()
    yLabel11.place_forget()
    expressionButton11.place_forget()
    colourButton11.place_forget()

    expression12.place_forget()
    yLabel12.place_forget()
    expressionButton12.place_forget()
    colourButton12.place_forget()

    expression13.place_forget()
    yLabel13.place_forget()
    expressionButton13.place_forget()
    colourButton13.place_forget()

    expression14.place_forget()
    yLabel14.place_forget()
    expressionButton14.place_forget()
    colourButton14.place_forget()

    expression15.place_forget()
    yLabel15.place_forget()
    expressionButton15.place_forget()
    colourButton15.place_forget()

    expression16.place_forget()
    yLabel16.place_forget()
    expressionButton16.place_forget()
    colourButton16.place_forget()

    expression17.place_forget()
    yLabel17.place_forget()
    expressionButton17.place_forget()
    colourButton17.place_forget()

    expression18.place_forget()
    yLabel18.place_forget()
    expressionButton18.place_forget()
    colourButton18.place_forget()

    expression19.place_forget()
    yLabel19.place_forget()
    expressionButton19.place_forget()
    colourButton19.place_forget()

    expression20.place_forget()
    yLabel20.place_forget()
    expressionButton20.place_forget()
    colourButton20.place_forget()

    lineExists = [False] * 21

    expression1.focus_set()

    

graph = Canvas(graphFrame, width=screensize[0] / 2, height=screensize[0] / 2, bg='#ffffff', highlightthickness=0)
graph.place(relx=0.5, rely=0.5, anchor=W)

line1 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line2 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line3 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line4 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line5 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line6 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line7 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line8 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line9 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line10 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line11 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line12 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line13 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line14 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line15 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line16 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line17 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line18 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line19 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))
line20 = [graph.create_line(0, 0, 0, 0, width=0, state='hidden')] * int(round(screensize[0] / 2))

def redrawgraph():
    global line1
    global equation1
    graph.delete("all")
    if zoom >= 0.125:
        for i in range(0-int(round(6*screensize[0] / 40)), int(round(screensize[0] / 2)), int(round((screensize[0] / 40)*zoom))):
            if darkMode == False:
                graph.create_line(0, i, screensize[0] / 2, i, fill='#dfdfdf', width=1)
            else:
                graph.create_line(0, i, screensize[0] / 2, i, fill='#707070', width=1)

        for i in range(0-int(round(6*screensize[0] / 40)), int(round(screensize[0] / 2)), int(round((screensize[0] / 40)*zoom))):
            if darkMode == False:
                graph.create_line(i, 0, i, screensize[0] / 2, fill='#dfdfdf', width=1)
            else:
                graph.create_line(i, 0, i, screensize[0] / 2, fill='#707070', width=1)

    if darkMode == False:
        graph.create_line(0, screensize[0] / 4, screensize[0] / 2, screensize[0] / 4, fill='#000000', width=3, arrow='both')
        graph.create_line(screensize[0] / 4, 0, screensize[0] / 4, screensize[0] / 2, fill='#000000', width=3, arrow='both')
    else:
        graph.create_line(0, screensize[0] / 4, screensize[0] / 2, screensize[0] / 4, fill='#dfdfdf', width=3, arrow='both')
        graph.create_line(screensize[0] / 4, 0, screensize[0] / 4, screensize[0] / 2, fill='#dfdfdf', width=3, arrow='both')
        
    for i in range(0-int(round(6*screensize[0] / 40)), int(round(screensize[0] / 2))+1, int(round((screensize[0] / 40)*zoom))):
        if (zoom*(i - screensize[0]/4)/(screensize[0]/40)) % 1 == 0:
            label = int(round((i - screensize[0]/4)/(screensize[0]/40), 0)/zoom)
            if darkMode == False:
                graph.create_text(i - (screensize[0]) / 220, (33*screensize[0]) / 128, text=label, fill='#000000')
            else:
                graph.create_text(i - (screensize[0]) / 220, (33*screensize[0]) / 128, text=label, fill='#ffffff')

    for i in range(0-int(round(6*screensize[0] / 40)), int(round(screensize[0] / 2))+1, int(round((screensize[0] / 40)*zoom))):
        if (zoom*(i - screensize[0]/4)/(screensize[0]/40)) % 1 == 0:
            label = int(round(-(i - screensize[0]/4)/(screensize[0]/40), 0)/zoom)
            if label != 0:
                if darkMode == False:
                    graph.create_text((31*screensize[0]) / 128, i + (screensize[0]) / 200, text=label, fill='#000000')
                else:
                    graph.create_text((31*screensize[0]) / 128, i + (screensize[0]) / 200, text=label, fill='#ffffff')

    if lineExists[1] == True:
        expressionButton1.invoke()
    if lineExists[2] == True:
        expressionButton2.invoke()
    if lineExists[3] == True:
        expressionButton3.invoke()
    if lineExists[4] == True:
        expressionButton4.invoke()
    if lineExists[5] == True:
        expressionButton5.invoke()
    if lineExists[6] == True:
        expressionButton6.invoke()
    if lineExists[7] == True:
        expressionButton7.invoke()
    if lineExists[8] == True:
        expressionButton8.invoke()
    if lineExists[9] == True:
        expressionButton9.invoke()
    if lineExists[10] == True:
        expressionButton10.invoke()
    if lineExists[11] == True:
        expressionButton11.invoke()
    if lineExists[12] == True:
        expressionButton12.invoke()
    if lineExists[13] == True:
        expressionButton13.invoke()
    if lineExists[14] == True:
        expressionButton14.invoke()
    if lineExists[15] == True:
        expressionButton15.invoke()
    if lineExists[16] == True:
        expressionButton16.invoke()
    if lineExists[17] == True:
        expressionButton17.invoke()
    if lineExists[18] == True:
        expressionButton18.invoke()
    if lineExists[19] == True:
        expressionButton19.invoke()
    if lineExists[20] == True:
        expressionButton20.invoke()

    
redrawgraph()

#Bind Mouse Wheel
graph.bind("<MouseWheel>", mouse_wheel)
graphFrame.bind("<MouseWheel>", mouse_wheel)

graph.bind("<Button-4>", mouse_wheel)
graph.bind("<Button-5>", mouse_wheel)
graphFrame.bind("<Button-4>", mouse_wheel)
graphFrame.bind("<Button-5>", mouse_wheel)

clearButton = Button(graphFrame, text="Clear Graph", bg="#fee0e0", activebackground="#fee0e0", command=lambda:[cleargraph(), pressnumber(0)])
clearButton.place(relx=0.47, rely=0.1, anchor=E)

zoomInButton = Button(graphFrame, text="+", width=2, command=lambda:[zoomIn(), redrawgraph()])
zoomInButton.place(relx=0.9975, rely=0.077, anchor=E)

zoomOutButton = Button(graphFrame, text="–", width=2, command=lambda:[zoomOut(), redrawgraph()])
zoomOutButton.place(relx=0.9975, rely=0.119, anchor=E)

sevenButton = Button(graphFrame, text="7", width=3, command=lambda:[insertsymbol("7"), pressnumber(1), pressclosingBracket(0)])
sevenButton.place(relx=0.23, rely=0.7, anchor=E)

eightButton = Button(graphFrame, text="8", width=3, command=lambda:[insertsymbol("8"), pressnumber(1), pressclosingBracket(0)])
eightButton.place(relx=0.255, rely=0.7, anchor=E)

nineButton = Button(graphFrame, text="9", width=3, command=lambda:[insertsymbol("9"), pressnumber(1), pressclosingBracket(0)])
nineButton.place(relx=0.28, rely=0.7, anchor=E)

fourButton = Button(graphFrame, text="4", width=3, command=lambda:[insertsymbol("4"), pressnumber(1), pressclosingBracket(0)])
fourButton.place(relx=0.23, rely=0.74, anchor=E)

fiveButton = Button(graphFrame, text="5", width=3, command=lambda:[insertsymbol("5"), pressnumber(1), pressclosingBracket(0)])
fiveButton.place(relx=0.255, rely=0.74, anchor=E)

sixButton = Button(graphFrame, text="6", width=3, command=lambda:[insertsymbol("6"), pressnumber(1), pressclosingBracket(0)])
sixButton.place(relx=0.28, rely=0.74, anchor=E)

oneButton = Button(graphFrame, text="1", width=3, command=lambda:[insertsymbol("1"), pressnumber(1), pressclosingBracket(0)])
oneButton.place(relx=0.23, rely=0.78, anchor=E)

twoButton = Button(graphFrame, text="2", width=3, command=lambda:[insertsymbol("2"), pressnumber(1), pressclosingBracket(0)])
twoButton.place(relx=0.255, rely=0.78, anchor=E)

threeButton = Button(graphFrame, text="3", width=3, command=lambda:[insertsymbol("3"), pressnumber(1), pressclosingBracket(0)])
threeButton.place(relx=0.28, rely=0.78, anchor=E)

xButton = Button(graphFrame, text="𝑥", width=3, bg='#dddddd', activebackground='#dddddd', command=lambda:[insertsymbol("x"), inserttimes(), pressclosingBracket(0)])
xButton.place(relx=0.23, rely=0.82, anchor=E)

zeroButton = Button(graphFrame, text="0", width=3, command=lambda:[insertsymbol("0"), pressnumber(1), pressclosingBracket(0)])
zeroButton.place(relx=0.255, rely=0.82, anchor=E)

decimalButton = Button(graphFrame, text=".", width=3, command=lambda:[insertsymbol("."), pressnumber(0), pressclosingBracket(0)])
decimalButton.place(relx=0.28, rely=0.82, anchor=E)

plusButton = Button(graphFrame, text="+", width=2, command=lambda:[insertsymbol("+"), pressnumber(0), pressclosingBracket(0)])
plusButton.place(relx=0.305, rely=0.7, anchor=E)

minusButton = Button(graphFrame, text="–", width=2, command=lambda:[insertsymbol("-"), pressnumber(0), pressclosingBracket(0)])
minusButton.place(relx=0.305, rely=0.74, anchor=E)

timesButton = Button(graphFrame, text="×", width=2, command=lambda:[insertsymbol("*"), pressnumber(0), pressclosingBracket(0)])
timesButton.place(relx=0.305, rely=0.78, anchor=E)

divideButton = Button(graphFrame, text="÷", width=2, command=lambda:[insertsymbol("/"), pressnumber(0), pressclosingBracket(0)])
divideButton.place(relx=0.305, rely=0.82, anchor=E)

powerButton = Button(graphFrame, text="^", width=3, command=lambda:[insertsymbol("**"), pressnumber(0), pressclosingBracket(0)])
powerButton.place(relx=0.1, rely=0.7, anchor=E)

rootButton = Button(graphFrame, text="√", width=3, command=lambda:[insertsymbol("sqrt("), pressnumber(0), pressclosingBracket(0)])
rootButton.place(relx=0.125, rely=0.7, anchor=E)

modulusButton = Button(graphFrame, text="|  |", width=3, command=lambda:[insertsymbol("abs("), pressnumber(0), pressclosingBracket(0)])
modulusButton.place(relx=0.15, rely=0.7, anchor=E)

commaButton = Button(graphFrame, text=",", width=3, command=lambda:[insertsymbol(","), pressnumber(0), pressclosingBracket(0)])
commaButton.place(relx=0.175, rely=0.7, anchor=E)

leftbraceButton = Button(graphFrame, text="(", width=3, command=lambda:[insertsymbol("("), pressnumber(0),insertBracketTimes(), pressclosingBracket(0)])
leftbraceButton.place(relx=0.1, rely=0.74, anchor=E)

rightbraceButton = Button(graphFrame, text=")", width=3, command=lambda:[insertsymbol(")"), pressnumber(0), pressclosingBracket(1)])
rightbraceButton.place(relx=0.125, rely=0.74, anchor=E)

eButton = Button(graphFrame, text="e", width=3, command=lambda:[insertsymbol("e"), pressnumber(1), pressclosingBracket(0)])
eButton.place(relx=0.15, rely=0.74, anchor=E)

piButton = Button(graphFrame, text="π", width=3, command=lambda:[insertsymbol("pi"), pressnumber(1), pressclosingBracket(0)])
piButton.place(relx=0.175, rely=0.74, anchor=E)

naturalButton = Button(graphFrame, text="ln", width=3, command=lambda:[insertsymbol("log("), pressnumber(0), pressclosingBracket(0)])
naturalButton.place(relx=0.125, rely=0.78, anchor=E)

logButton = Button(graphFrame, text="log", width=3, command=lambda:[insertsymbol("log(,"), pressnumber(0), pressclosingBracket(0)])
logButton.place(relx=0.15, rely=0.78, anchor=E)

deleteButton = Button(graphFrame, text="←", width=10, bg="#fee0e0", activebackground="#fee0e0", command=lambda:[deletesymbol(), pressnumber(0), pressclosingBracket(0)])
deleteButton.place(relx=0.425, rely=0.66, anchor=E)

sinButton = Button(graphFrame, text="sin", width=4, command=lambda:[insertsymbol("sin("), pressnumber(0), pressclosingBracket(0)])
sinButton.place(relx=0.365, rely=0.7, anchor=E)

cosButton = Button(graphFrame, text="cos", width=4, command=lambda:[insertsymbol("cos("), pressnumber(0), pressclosingBracket(0)])
cosButton.place(relx=0.395, rely=0.7, anchor=E)

tanButton = Button(graphFrame, text="tan", width=4, command=lambda:[insertsymbol("tan("), pressnumber(0), pressclosingBracket(0)])
tanButton.place(relx=0.425, rely=0.7, anchor=E)

asinButton = Button(graphFrame, text="arcsin", width=4, command=lambda:[insertsymbol("asin("), pressnumber(0), pressclosingBracket(0)])
asinButton.place(relx=0.365, rely=0.74, anchor=E)

acosButton = Button(graphFrame, text="arccos", width=4, command=lambda:[insertsymbol("acos("), pressnumber(0), pressclosingBracket(0)])
acosButton.place(relx=0.395, rely=0.74, anchor=E)

atanButton = Button(graphFrame, text="arctan", width=4, command=lambda:[insertsymbol("atan("), pressnumber(0), pressclosingBracket(0)])
atanButton.place(relx=0.425, rely=0.74, anchor=E)

sinhButton = Button(graphFrame, text="sinh", width=4, command=lambda:[insertsymbol("sinh("), pressnumber(0), pressclosingBracket(0)])
sinhButton.place(relx=0.365, rely=0.78, anchor=E)

coshButton = Button(graphFrame, text="cosh", width=4, command=lambda:[insertsymbol("cosh("), pressnumber(0), pressclosingBracket(0)])
coshButton.place(relx=0.395, rely=0.78, anchor=E)

tanhButton = Button(graphFrame, text="tanh", width=4, command=lambda:[insertsymbol("tanh("), pressnumber(0), pressclosingBracket(0)])
tanhButton.place(relx=0.425, rely=0.78, anchor=E)

asinhButton = Button(graphFrame, text="arsinh", width=4, command=lambda:[insertsymbol("asinh("), pressnumber(0), pressclosingBracket(0)])
asinhButton.place(relx=0.365, rely=0.82, anchor=E)

acoshButton = Button(graphFrame, text="arcosh", width=4, command=lambda:[insertsymbol("acosh("), pressnumber(0), pressclosingBracket(0)])
acoshButton.place(relx=0.395, rely=0.82, anchor=E)

atanhButton = Button(graphFrame, text="artanh", width=4, command=lambda:[insertsymbol("atanh("), pressnumber(0), pressclosingBracket(0)])
atanhButton.place(relx=0.425, rely=0.82, anchor=E)


cleargraph()

def mainMenu():

    menu = Frame(root, width=screensize[0], height=screensize[1])

    if language == 0:
        Title = Label(menu, text="Graphing Calculator")
    elif language == 1:
        Title = Label(menu, text="حاسب الرسوم البيانية")
    elif language == 2:
        Title = Label(menu, text="圖形計算器")
    elif language == 3:
        Title = Label(menu, text="Calculatrice graphique")
    elif language == 4:
        Title = Label(menu, text="Grafikrechner")
    elif language == 5:
        Title = Label(menu, text="Υπολογιστής γραφικών")
    elif language == 6:
        Title = Label(menu, text="ग्राफिंग कैलकुलेटर")
    elif language == 7:
        Title = Label(menu, text="Calcolatrice grafica")
    elif language == 8:
        Title = Label(menu, text="Calculadora gráfica")
    elif language == 9:
        Title = Label(menu, text="Графический калькулятор")
    elif language == 10:
        Title = Label(menu, text="Calculadora gráfica")
    
    Title.place(relx=0.5, rely=0.2, anchor=CENTER)
    Title.config(font=titleFont)

    if language == 0:
        Button1 = Button(menu, text="Graphing Calculator", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    elif language == 1:
        Button1 = Button(menu, text="حاسب الرسوم البيانية", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    elif language == 2:
        Button1 = Button(menu, text="圖形計算器", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    elif language == 3:
        Button1 = Button(menu, text="Calculatrice graphique", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    elif language == 4:
        Button1 = Button(menu, text="Grafikrechner", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    elif language == 5:
        Button1 = Button(menu, text="Υπολογιστής γραφικών", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    elif language == 6:
        Button1 = Button(menu, text="ग्राफिंग कैलकुलेटर", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    elif language == 7:
        Button1 = Button(menu, text="Calcolatrice grafica", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    elif language == 8:
        Button1 = Button(menu, text="Calculadora gráfica", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    elif language == 9:
        Button1 = Button(menu, text="Графический калькулятор", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    elif language == 10:
        Button1 = Button(menu, text="Calculadora gráfica", command=lambda:[menu.place_forget(), graphFrame.place(relx=0.48, rely=0.5, anchor=CENTER)], width=25, height=2)
    Button1.place(relx=0.5, rely=0.4, anchor=CENTER)
    Button1.config(font=buttonFont)

    if language == 0:
        Button2 = Button(menu, text="Calculus Problem Solver", command=lambda:[menu.destroy(), calcProbSolver()], width=25, height=2)
    elif language == 1:
        Button2 = Button(menu, text="حل مسائل التفاضل والتكامل", command=lambda:[menu.destroy(), calcProbSolver()], width=25, height=2)
    elif language == 2:
        Button2 = Button(menu, text="圖形計算器", command=lambda:[menu.destroy(), calcProbSolver()], width=25, height=2)
    elif language == 9:
        Button2 = Button(menu, text="Решатель задач исчисления", command=lambda:[menu.destroy(), calcProbSolver()], width=25, height=2)
    elif language == 10:
        Button2 = Button(menu, text="Solucionador de problemas de cálculo", command=lambda:[menu.destroy(), calcProbSolver()], width=25, height=2)
        
    Button2.place(relx=0.5, rely=0.5, anchor=CENTER)
    Button2.config(font=buttonFont)

    if language == 0:
        Button3 = Button(menu, text="Settings", command=lambda:[menu.destroy(), settingsMenu()], width=25, height=2)
    elif language == 1:
        Button3 = Button(menu, text="إعدادات", command=lambda:[menu.destroy(), settingsMenu()], width=25, height=2)
    elif language == 2:
        Button3 = Button(menu, text="設置", command=lambda:[menu.destroy(), settingsMenu()], width=25, height=2)
    elif language == 9:
        Button3 = Button(menu, text="Настройки", command=lambda:[menu.destroy(), settingsMenu()], width=25, height=2)
    elif language == 10:
        Button3 = Button(menu, text="Ajustes", command=lambda:[menu.destroy(), settingsMenu()], width=25, height=2)
    Button3.place(relx=0.5, rely=0.6, anchor=CENTER)
    Button3.config(font=buttonFont)

    if language == 0:
        exitButton = Button(menu, text="Exit", command=root.destroy, width=20, height=2)
    elif language == 1:
        exitButton = Button(menu, text="مخرج", command=root.destroy, width=20, height=2)
    elif language == 2:
        exitButton = Button(menu, text="退出", command=root.destroy, width=20, height=2)
    elif language == 9:
        exitButton = Button(menu, text="Выход", command=root.destroy, width=20, height=2)
    elif language == 10:
        exitButton = Button(menu, text="Salir", command=root.destroy, width=20, height=2)
    exitButton.place(relx=0.5, rely=0.7, anchor=CENTER)
    exitButton.config(font=buttonFont)

    if darkMode == True:
        Title.config(fg='#ffffff', bg='#212121')
        Button1.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        Button2.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        Button3.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        exitButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        menu.config(bg='#212121')

    menu.place(relx=0.5, rely=0.5, anchor=CENTER)

def settingsMenu():

    settings = Frame(root, width=screensize[0], height=screensize[1])

    settingsTitle = Label(settings, text="Settings")
    settingsTitle.place(relx=0.5, rely=0.2, anchor=CENTER)
    settingsTitle.config(font=titleFont)

    Button4 = Button(settings, text="Toggle Dark Mode", command=lambda:[toggleDarkMode(), settings.destroy(), settingsMenu()], width=25, height=2)
    Button4.place(relx=0.5, rely=0.4, anchor=CENTER)
    Button4.config(font=buttonFont)

    Button5 = Button(settings, text="Languages", command=lambda:[settings.destroy(), languagesMenu()], width=25, height=2)
    Button5.place(relx=0.5, rely=0.5, anchor=CENTER)
    Button5.config(font=buttonFont)

    Button6 = Button(settings, text="Fullscreen Mode", command=fullscreen, width=25, height=2)
    Button6.place(relx=0.5, rely=0.6, anchor=CENTER)
    Button6.config(font=buttonFont)

    backButton = Button(settings, text="Back", command=lambda:[settings.destroy(), mainMenu()])
    backButton.place(relx=0.005, rely=0.05, anchor=NW)
    backButton.config(font=buttonFont)

    if darkMode == True:
        settingsTitle.config(fg='#ffffff', bg='#212121')
        Button4.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        Button5.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        Button6.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        backButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        settings.config(bg='#212121')

    settings.place(relx=0.5, rely=0.5, anchor=CENTER)

def fullscreen():
    if (root.attributes('-fullscreen')) == False:
        root.attributes("-fullscreen", True)
    elif (root.attributes('-fullscreen')) == True:
        root.attributes("-fullscreen", False)

def languagesMenu():
    languages = Frame(root, width=screensize[0], height=screensize[1])

    languagesTitle = Label(languages, text="Languages")
    languagesTitle.place(relx=0.5, rely=0.15, anchor=CENTER)
    languagesTitle.config(font=titleFont)

    arabicButton = Button(languages, text="عربى", width=30, height=1, command=lambda:[changeLanguage(1)])
    arabicButton.place(relx=0.5, rely=0.27, anchor=CENTER)
    arabicButton.config(font=buttonFont)

    chineseButton = Button(languages, text="中國人", width=30, height=1, command=lambda:[changeLanguage(2)])
    chineseButton.place(relx=0.5, rely=0.33, anchor=CENTER)
    chineseButton.config(font=buttonFont)

    englishButton = Button(languages, text="English", width=30, height=1, command=lambda:[changeLanguage(0)])
    englishButton.place(relx=0.5, rely=0.39, anchor=CENTER)
    englishButton.config(font=buttonFont)

    frenchButton = Button(languages, text="Français", width=30, height=1, command=lambda:[changeLanguage(3)])
    frenchButton.place(relx=0.5, rely=0.45, anchor=CENTER)
    frenchButton.config(font=buttonFont)

    germanButton = Button(languages, text="Deutsch", width=30, height=1, command=lambda:[changeLanguage(4)])
    germanButton.place(relx=0.5, rely=0.51, anchor=CENTER)
    germanButton.config(font=buttonFont)

    greekButton = Button(languages, text="Ελληνικά", width=30, height=1, command=lambda:[changeLanguage(5)])
    greekButton.place(relx=0.5, rely=0.57, anchor=CENTER)
    greekButton.config(font=buttonFont)

    hindiButton = Button(languages, text="हिन्दी", width=30, height=1, command=lambda:[changeLanguage(6)])
    hindiButton.place(relx=0.5, rely=0.63, anchor=CENTER)
    hindiButton.config(font=buttonFont)

    italianButton = Button(languages, text="Italiano", width=30, height=1, command=lambda:[changeLanguage(7)])
    italianButton.place(relx=0.5, rely=0.69, anchor=CENTER)
    italianButton.config(font=buttonFont)

    portugeseButton = Button(languages, text="Português", width=30, height=1, command=lambda:[changeLanguage(8)])
    portugeseButton.place(relx=0.5, rely=0.75, anchor=CENTER)
    portugeseButton.config(font=buttonFont)

    russianButton = Button(languages, text="Русский", width=30, height=1, command=lambda:[changeLanguage(9)])
    russianButton.place(relx=0.5, rely=0.81, anchor=CENTER)
    russianButton.config(font=buttonFont)

    spanishButton = Button(languages, text="Español", width=30, height=1, command=lambda:[changeLanguage(10)])
    spanishButton.place(relx=0.5, rely=0.87, anchor=CENTER)
    spanishButton.config(font=buttonFont)

    backButton = Button(languages, text="Back", command=lambda:[languages.destroy(), settingsMenu()])
    backButton.place(relx=0.005, rely=0.05, anchor=NW)
    backButton.config(font=buttonFont)

    if darkMode == True:
        languagesTitle.config(fg='#ffffff', bg='#212121')
        arabicButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        chineseButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        englishButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        frenchButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        germanButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        greekButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        hindiButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        italianButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        portugeseButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        russianButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        spanishButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        backButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        languages.config(bg='#212121')

    languages.place(relx=0.5, rely=0.5, anchor=CENTER)

def changeLanguage(lang):
    global language
    language = lang
    
def toggleDarkMode():
    global darkMode
    if darkMode == False:
        darkMode = True
        
        equationsLabel["fg"] = '#ffffff'
        equationsLabel["bg"] = '#212121'
        graphFrame["bg"] = '#212121'
        root["bg"] = '#212121'
        
        backButton["fg"] = '#ffffff'
        backButton["bg"] = '#212121'
        backButton["activeforeground"] = '#ffffff'
        backButton["activebackground"] = '#212121'

        clearButton["fg"] = '#ffffff'
        clearButton["bg"] = '#402828'
        clearButton["activeforeground"] = '#ffffff'
        clearButton["activebackground"] = '#402828'

        yLabel1["fg"] = '#ffffff'
        yLabel1["bg"] = '#212121'
        yLabel2["fg"] = '#ffffff'
        yLabel2["bg"] = '#212121'
        yLabel3["fg"] = '#ffffff'
        yLabel3["bg"] = '#212121'
        yLabel4["fg"] = '#ffffff'
        yLabel4["bg"] = '#212121'
        yLabel5["fg"] = '#ffffff'
        yLabel5["bg"] = '#212121'
        yLabel6["fg"] = '#ffffff'
        yLabel6["bg"] = '#212121'
        yLabel7["fg"] = '#ffffff'
        yLabel7["bg"] = '#212121'
        yLabel8["fg"] = '#ffffff'
        yLabel8["bg"] = '#212121'
        yLabel9["fg"] = '#ffffff'
        yLabel9["bg"] = '#212121'
        yLabel10["fg"] = '#ffffff'
        yLabel10["bg"] = '#212121'
        yLabel11["fg"] = '#ffffff'
        yLabel11["bg"] = '#212121'
        yLabel12["fg"] = '#ffffff'
        yLabel12["bg"] = '#212121'
        yLabel13["fg"] = '#ffffff'
        yLabel13["bg"] = '#212121'
        yLabel14["fg"] = '#ffffff'
        yLabel14["bg"] = '#212121'
        yLabel15["fg"] = '#ffffff'
        yLabel15["bg"] = '#212121'
        yLabel16["fg"] = '#ffffff'
        yLabel16["bg"] = '#212121'
        yLabel17["fg"] = '#ffffff'
        yLabel17["bg"] = '#212121'
        yLabel18["fg"] = '#ffffff'
        yLabel18["bg"] = '#212121'
        yLabel19["fg"] = '#ffffff'
        yLabel19["bg"] = '#212121'
        yLabel20["fg"] = '#ffffff'
        yLabel20["bg"] = '#212121'

        expression1["fg"] = '#ffffff'
        expression1["insertbackground"] = '#dfdfdf'
        expression1["bg"] = '#303030'
        expression2["fg"] = '#ffffff'
        expression2["insertbackground"] = '#dfdfdf'
        expression2["bg"] = '#303030'
        expression3["fg"] = '#ffffff'
        expression3["insertbackground"] = '#dfdfdf'
        expression3["bg"] = '#303030'
        expression4["fg"] = '#ffffff'
        expression4["insertbackground"] = '#dfdfdf'
        expression4["bg"] = '#303030'
        expression5["fg"] = '#ffffff'
        expression5["insertbackground"] = '#dfdfdf'
        expression5["bg"] = '#303030'
        expression6["fg"] = '#ffffff'
        expression6["insertbackground"] = '#dfdfdf'
        expression6["bg"] = '#303030'
        expression7["fg"] = '#ffffff'
        expression7["insertbackground"] = '#dfdfdf'
        expression7["bg"] = '#303030'
        expression8["fg"] = '#ffffff'
        expression8["insertbackground"] = '#dfdfdf'
        expression8["bg"] = '#303030'
        expression9["fg"] = '#ffffff'
        expression9["insertbackground"] = '#dfdfdf'
        expression9["bg"] = '#303030'
        expression10["fg"] = '#ffffff'
        expression10["insertbackground"] = '#dfdfdf'
        expression10["bg"] = '#303030'
        expression11["fg"] = '#ffffff'
        expression11["insertbackground"] = '#dfdfdf'
        expression11["bg"] = '#303030'
        expression12["fg"] = '#ffffff'
        expression12["insertbackground"] = '#dfdfdf'
        expression12["bg"] = '#303030'
        expression13["fg"] = '#ffffff'
        expression13["insertbackground"] = '#dfdfdf'
        expression13["bg"] = '#303030'
        expression14["fg"] = '#ffffff'
        expression14["insertbackground"] = '#dfdfdf'
        expression14["bg"] = '#303030'
        expression15["fg"] = '#ffffff'
        expression15["insertbackground"] = '#dfdfdf'
        expression15["bg"] = '#303030'
        expression16["fg"] = '#ffffff'
        expression16["insertbackground"] = '#dfdfdf'
        expression16["bg"] = '#303030'
        expression17["fg"] = '#ffffff'
        expression17["insertbackground"] = '#dfdfdf'
        expression17["bg"] = '#303030'
        expression18["fg"] = '#ffffff'
        expression18["insertbackground"] = '#dfdfdf'
        expression18["bg"] = '#303030'
        expression19["fg"] = '#ffffff'
        expression19["insertbackground"] = '#dfdfdf'
        expression19["bg"] = '#303030'
        expression20["fg"] = '#ffffff'
        expression20["insertbackground"] = '#dfdfdf'
        expression20["bg"] = '#303030'

        colourButton1["bg"] = '#212121'
        colourButton1["activebackground"] = '#212121'
        colourButton2["bg"] = '#212121'
        colourButton2["activebackground"] = '#212121'
        colourButton3["bg"] = '#212121'
        colourButton3["activebackground"] = '#212121'
        colourButton4["bg"] = '#212121'
        colourButton4["activebackground"] = '#212121'
        colourButton5["bg"] = '#212121'
        colourButton5["activebackground"] = '#212121'
        colourButton6["bg"] = '#212121'
        colourButton6["activebackground"] = '#212121'
        colourButton7["bg"] = '#212121'
        colourButton7["activebackground"] = '#212121'
        colourButton8["bg"] = '#212121'
        colourButton8["activebackground"] = '#212121'
        colourButton9["bg"] = '#212121'
        colourButton9["activebackground"] = '#212121'
        colourButton10["bg"] = '#212121'
        colourButton10["activebackground"] = '#212121'
        colourButton11["bg"] = '#212121'
        colourButton11["activebackground"] = '#212121'
        colourButton12["bg"] = '#212121'
        colourButton12["activebackground"] = '#212121'
        colourButton13["bg"] = '#212121'
        colourButton13["activebackground"] = '#212121'
        colourButton14["bg"] = '#212121'
        colourButton14["activebackground"] = '#212121'
        colourButton15["bg"] = '#212121'
        colourButton15["activebackground"] = '#212121'
        colourButton16["bg"] = '#212121'
        colourButton16["activebackground"] = '#212121'
        colourButton17["bg"] = '#212121'
        colourButton17["activebackground"] = '#212121'
        colourButton18["bg"] = '#212121'
        colourButton18["activebackground"] = '#212121'
        colourButton19["bg"] = '#212121'
        colourButton19["activebackground"] = '#212121'
        colourButton20["bg"] = '#212121'
        colourButton20["activebackground"] = '#212121'
        
        expressionButton1["fg"] = '#ffffff'
        expressionButton1["bg"] = '#212121'
        expressionButton1["activeforeground"] = '#ffffff'
        expressionButton1["activebackground"] = '#212121'
        expressionButton2["fg"] = '#ffffff'
        expressionButton2["bg"] = '#212121'
        expressionButton2["activeforeground"] = '#ffffff'
        expressionButton2["activebackground"] = '#212121'
        expressionButton3["fg"] = '#ffffff'
        expressionButton3["bg"] = '#212121'
        expressionButton3["activeforeground"] = '#ffffff'
        expressionButton3["activebackground"] = '#212121'
        expressionButton4["fg"] = '#ffffff'
        expressionButton4["bg"] = '#212121'
        expressionButton4["activeforeground"] = '#ffffff'
        expressionButton4["activebackground"] = '#212121'
        expressionButton5["fg"] = '#ffffff'
        expressionButton5["bg"] = '#212121'
        expressionButton5["activeforeground"] = '#ffffff'
        expressionButton5["activebackground"] = '#212121'
        expressionButton6["fg"] = '#ffffff'
        expressionButton6["bg"] = '#212121'
        expressionButton6["activeforeground"] = '#ffffff'
        expressionButton6["activebackground"] = '#212121'
        expressionButton7["fg"] = '#ffffff'
        expressionButton7["bg"] = '#212121'
        expressionButton7["activeforeground"] = '#ffffff'
        expressionButton7["activebackground"] = '#212121'
        expressionButton8["fg"] = '#ffffff'
        expressionButton8["bg"] = '#212121'
        expressionButton8["activeforeground"] = '#ffffff'
        expressionButton8["activebackground"] = '#212121'
        expressionButton9["fg"] = '#ffffff'
        expressionButton9["bg"] = '#212121'
        expressionButton9["activeforeground"] = '#ffffff'
        expressionButton9["activebackground"] = '#212121'
        expressionButton10["fg"] = '#ffffff'
        expressionButton10["bg"] = '#212121'
        expressionButton10["activeforeground"] = '#ffffff'
        expressionButton10["activebackground"] = '#212121'
        expressionButton11["fg"] = '#ffffff'
        expressionButton11["bg"] = '#212121'
        expressionButton11["activeforeground"] = '#ffffff'
        expressionButton11["activebackground"] = '#212121'
        expressionButton12["fg"] = '#ffffff'
        expressionButton12["bg"] = '#212121'
        expressionButton12["activeforeground"] = '#ffffff'
        expressionButton12["activebackground"] = '#212121'
        expressionButton13["fg"] = '#ffffff'
        expressionButton13["bg"] = '#212121'
        expressionButton13["activeforeground"] = '#ffffff'
        expressionButton13["activebackground"] = '#212121'
        expressionButton14["fg"] = '#ffffff'
        expressionButton14["bg"] = '#212121'
        expressionButton14["activeforeground"] = '#ffffff'
        expressionButton14["activebackground"] = '#212121'
        expressionButton15["fg"] = '#ffffff'
        expressionButton15["bg"] = '#212121'
        expressionButton15["activeforeground"] = '#ffffff'
        expressionButton15["activebackground"] = '#212121'
        expressionButton16["fg"] = '#ffffff'
        expressionButton16["bg"] = '#212121'
        expressionButton16["activeforeground"] = '#ffffff'
        expressionButton16["activebackground"] = '#212121'
        expressionButton17["fg"] = '#ffffff'
        expressionButton17["bg"] = '#212121'
        expressionButton17["activeforeground"] = '#ffffff'
        expressionButton17["activebackground"] = '#212121'
        expressionButton18["fg"] = '#ffffff'
        expressionButton18["bg"] = '#212121'
        expressionButton18["activeforeground"] = '#ffffff'
        expressionButton18["activebackground"] = '#212121'
        expressionButton19["fg"] = '#ffffff'
        expressionButton19["bg"] = '#212121'
        expressionButton19["activeforeground"] = '#ffffff'
        expressionButton19["activebackground"] = '#212121'
        expressionButton20["fg"] = '#ffffff'
        expressionButton20["bg"] = '#212121'
        expressionButton20["activeforeground"] = '#ffffff'
        expressionButton20["activebackground"] = '#212121'

        powerButton["fg"] = '#ffffff'
        powerButton["bg"] = '#212121'
        powerButton["activeforeground"] = '#ffffff'
        powerButton["activebackground"] = '#212121'

        rootButton["fg"] = '#ffffff'
        rootButton["bg"] = '#212121'
        rootButton["activeforeground"] = '#ffffff'
        rootButton["activebackground"] = '#212121'

        modulusButton["fg"] = '#ffffff'
        modulusButton["bg"] = '#212121'
        modulusButton["activeforeground"] = '#ffffff'
        modulusButton["activebackground"] = '#212121'

        commaButton["fg"] = '#ffffff'
        commaButton["bg"] = '#212121'
        commaButton["activeforeground"] = '#ffffff'
        commaButton["activebackground"] = '#212121'

        leftbraceButton["fg"] = '#ffffff'
        leftbraceButton["bg"] = '#212121'
        leftbraceButton["activeforeground"] = '#ffffff'
        leftbraceButton["activebackground"] = '#212121'

        rightbraceButton["fg"] = '#ffffff'
        rightbraceButton["bg"] = '#212121'
        rightbraceButton["activeforeground"] = '#ffffff'
        rightbraceButton["activebackground"] = '#212121'

        eButton["fg"] = '#ffffff'
        eButton["bg"] = '#212121'
        eButton["activeforeground"] = '#ffffff'
        eButton["activebackground"] = '#212121'

        piButton["fg"] = '#ffffff'
        piButton["bg"] = '#212121'
        piButton["activeforeground"] = '#ffffff'
        piButton["activebackground"] = '#212121'

        naturalButton["fg"] = '#ffffff'
        naturalButton["bg"] = '#212121'
        naturalButton["activeforeground"] = '#ffffff'
        naturalButton["activebackground"] = '#212121'

        logButton["fg"] = '#ffffff'
        logButton["bg"] = '#212121'
        logButton["activeforeground"] = '#ffffff'
        logButton["activebackground"] = '#212121'

        sevenButton["fg"] = '#ffffff'
        sevenButton["bg"] = '#212121'
        sevenButton["activeforeground"] = '#ffffff'
        sevenButton["activebackground"] = '#212121'

        eightButton["fg"] = '#ffffff'
        eightButton["bg"] = '#212121'
        eightButton["activeforeground"] = '#ffffff'
        eightButton["activebackground"] = '#212121'

        nineButton["fg"] = '#ffffff'
        nineButton["bg"] = '#212121'
        nineButton["activeforeground"] = '#ffffff'
        nineButton["activebackground"] = '#212121'

        fourButton["fg"] = '#ffffff'
        fourButton["bg"] = '#212121'
        fourButton["activeforeground"] = '#ffffff'
        fourButton["activebackground"] = '#212121'

        fiveButton["fg"] = '#ffffff'
        fiveButton["bg"] = '#212121'
        fiveButton["activeforeground"] = '#ffffff'
        fiveButton["activebackground"] = '#212121'

        sixButton["fg"] = '#ffffff'
        sixButton["bg"] = '#212121'
        sixButton["activeforeground"] = '#ffffff'
        sixButton["activebackground"] = '#212121'

        oneButton["fg"] = '#ffffff'
        oneButton["bg"] = '#212121'
        oneButton["activeforeground"] = '#ffffff'
        oneButton["activebackground"] = '#212121'

        twoButton["fg"] = '#ffffff'
        twoButton["bg"] = '#212121'
        twoButton["activeforeground"] = '#ffffff'
        twoButton["activebackground"] = '#212121'

        threeButton["fg"] = '#ffffff'
        threeButton["bg"] = '#212121'
        threeButton["activeforeground"] = '#ffffff'
        threeButton["activebackground"] = '#212121'

        xButton["fg"] = '#ffffff'
        xButton["bg"] = '#303030'
        xButton["activeforeground"] = '#ffffff'
        xButton["activebackground"] = '#303030'

        zeroButton["fg"] = '#ffffff'
        zeroButton["bg"] = '#212121'
        zeroButton["activeforeground"] = '#ffffff'
        zeroButton["activebackground"] = '#212121'

        decimalButton["fg"] = '#ffffff'
        decimalButton["bg"] = '#212121'
        decimalButton["activeforeground"] = '#ffffff'
        decimalButton["activebackground"] = '#212121'

        plusButton["fg"] = '#ffffff'
        plusButton["bg"] = '#212121'
        plusButton["activeforeground"] = '#ffffff'
        plusButton["activebackground"] = '#212121'

        minusButton["fg"] = '#ffffff'
        minusButton["bg"] = '#212121'
        minusButton["activeforeground"] = '#ffffff'
        minusButton["activebackground"] = '#212121'

        timesButton["fg"] = '#ffffff'
        timesButton["bg"] = '#212121'
        timesButton["activeforeground"] = '#ffffff'
        timesButton["activebackground"] = '#212121'

        divideButton["fg"] = '#ffffff'
        divideButton["bg"] = '#212121'
        divideButton["activeforeground"] = '#ffffff'
        divideButton["activebackground"] = '#212121'

        deleteButton["fg"] = '#ffffff'
        deleteButton["bg"] = '#402828'
        deleteButton["activeforeground"] = '#ffffff'
        deleteButton["activebackground"] = '#402828'

        sinButton["fg"] = '#ffffff'
        sinButton["bg"] = '#212121'
        sinButton["activeforeground"] = '#ffffff'
        sinButton["activebackground"] = '#212121'

        cosButton["fg"] = '#ffffff'
        cosButton["bg"] = '#212121'
        cosButton["activeforeground"] = '#ffffff'
        cosButton["activebackground"] = '#212121'

        tanButton["fg"] = '#ffffff'
        tanButton["bg"] = '#212121'
        tanButton["activeforeground"] = '#ffffff'
        tanButton["activebackground"] = '#212121'

        asinButton["fg"] = '#ffffff'
        asinButton["bg"] = '#212121'
        asinButton["activeforeground"] = '#ffffff'
        asinButton["activebackground"] = '#212121'

        acosButton["fg"] = '#ffffff'
        acosButton["bg"] = '#212121'
        acosButton["activeforeground"] = '#ffffff'
        acosButton["activebackground"] = '#212121'

        atanButton["fg"] = '#ffffff'
        atanButton["bg"] = '#212121'
        atanButton["activeforeground"] = '#ffffff'
        atanButton["activebackground"] = '#212121'

        sinhButton["fg"] = '#ffffff'
        sinhButton["bg"] = '#212121'
        sinhButton["activeforeground"] = '#ffffff'
        sinhButton["activebackground"] = '#212121'

        coshButton["fg"] = '#ffffff'
        coshButton["bg"] = '#212121'
        coshButton["activeforeground"] = '#ffffff'
        coshButton["activebackground"] = '#212121'

        tanhButton["fg"] = '#ffffff'
        tanhButton["bg"] = '#212121'
        tanhButton["activeforeground"] = '#ffffff'
        tanhButton["activebackground"] = '#212121'

        asinhButton["fg"] = '#ffffff'
        asinhButton["bg"] = '#212121'
        asinhButton["activeforeground"] = '#ffffff'
        asinhButton["activebackground"] = '#212121'

        acoshButton["fg"] = '#ffffff'
        acoshButton["bg"] = '#212121'
        acoshButton["activeforeground"] = '#ffffff'
        acoshButton["activebackground"] = '#212121'

        atanhButton["fg"] = '#ffffff'
        atanhButton["bg"] = '#212121'
        atanhButton["activeforeground"] = '#ffffff'
        atanhButton["activebackground"] = '#212121'

        zoomInButton["fg"] = '#ffffff'
        zoomInButton["bg"] = '#212121'
        zoomInButton["activeforeground"] = '#ffffff'
        zoomInButton["activebackground"] = '#212121'

        zoomOutButton["fg"] = '#ffffff'
        zoomOutButton["bg"] = '#212121'
        zoomOutButton["activeforeground"] = '#ffffff'
        zoomOutButton["activebackground"] = '#212121'

        graph["bg"] = '#303030'

        intpowerButton["fg"] = '#ffffff'
        intpowerButton["bg"] = '#212121'
        intpowerButton["activeforeground"] = '#ffffff'
        intpowerButton["activebackground"] = '#212121'

        introotButton["fg"] = '#ffffff'
        introotButton["bg"] = '#212121'
        introotButton["activeforeground"] = '#ffffff'
        introotButton["activebackground"] = '#212121'

        intmodulusButton["fg"] = '#ffffff'
        intmodulusButton["bg"] = '#212121'
        intmodulusButton["activeforeground"] = '#ffffff'
        intmodulusButton["activebackground"] = '#212121'

        intcommaButton["fg"] = '#ffffff'
        intcommaButton["bg"] = '#212121'
        intcommaButton["activeforeground"] = '#ffffff'
        intcommaButton["activebackground"] = '#212121'

        intleftbraceButton["fg"] = '#ffffff'
        intleftbraceButton["bg"] = '#212121'
        intleftbraceButton["activeforeground"] = '#ffffff'
        intleftbraceButton["activebackground"] = '#212121'

        intrightbraceButton["fg"] = '#ffffff'
        intrightbraceButton["bg"] = '#212121'
        intrightbraceButton["activeforeground"] = '#ffffff'
        intrightbraceButton["activebackground"] = '#212121'

        inteButton["fg"] = '#ffffff'
        inteButton["bg"] = '#212121'
        inteButton["activeforeground"] = '#ffffff'
        inteButton["activebackground"] = '#212121'

        intpiButton["fg"] = '#ffffff'
        intpiButton["bg"] = '#212121'
        intpiButton["activeforeground"] = '#ffffff'
        intpiButton["activebackground"] = '#212121'

        intnaturalButton["fg"] = '#ffffff'
        intnaturalButton["bg"] = '#212121'
        intnaturalButton["activeforeground"] = '#ffffff'
        intnaturalButton["activebackground"] = '#212121'

        intlogButton["fg"] = '#ffffff'
        intlogButton["bg"] = '#212121'
        intlogButton["activeforeground"] = '#ffffff'
        intlogButton["activebackground"] = '#212121'

        intsevenButton["fg"] = '#ffffff'
        intsevenButton["bg"] = '#212121'
        intsevenButton["activeforeground"] = '#ffffff'
        intsevenButton["activebackground"] = '#212121'

        inteightButton["fg"] = '#ffffff'
        inteightButton["bg"] = '#212121'
        inteightButton["activeforeground"] = '#ffffff'
        inteightButton["activebackground"] = '#212121'

        intnineButton["fg"] = '#ffffff'
        intnineButton["bg"] = '#212121'
        intnineButton["activeforeground"] = '#ffffff'
        intnineButton["activebackground"] = '#212121'

        intfourButton["fg"] = '#ffffff'
        intfourButton["bg"] = '#212121'
        intfourButton["activeforeground"] = '#ffffff'
        intfourButton["activebackground"] = '#212121'

        intfiveButton["fg"] = '#ffffff'
        intfiveButton["bg"] = '#212121'
        intfiveButton["activeforeground"] = '#ffffff'
        intfiveButton["activebackground"] = '#212121'

        intsixButton["fg"] = '#ffffff'
        intsixButton["bg"] = '#212121'
        intsixButton["activeforeground"] = '#ffffff'
        intsixButton["activebackground"] = '#212121'

        intoneButton["fg"] = '#ffffff'
        intoneButton["bg"] = '#212121'
        intoneButton["activeforeground"] = '#ffffff'
        intoneButton["activebackground"] = '#212121'

        inttwoButton["fg"] = '#ffffff'
        inttwoButton["bg"] = '#212121'
        inttwoButton["activeforeground"] = '#ffffff'
        inttwoButton["activebackground"] = '#212121'

        intthreeButton["fg"] = '#ffffff'
        intthreeButton["bg"] = '#212121'
        intthreeButton["activeforeground"] = '#ffffff'
        intthreeButton["activebackground"] = '#212121'

        intxButton["fg"] = '#ffffff'
        intxButton["bg"] = '#303030'
        intxButton["activeforeground"] = '#ffffff'
        intxButton["activebackground"] = '#303030'

        intzeroButton["fg"] = '#ffffff'
        intzeroButton["bg"] = '#212121'
        intzeroButton["activeforeground"] = '#ffffff'
        intzeroButton["activebackground"] = '#212121'

        intdecimalButton["fg"] = '#ffffff'
        intdecimalButton["bg"] = '#212121'
        intdecimalButton["activeforeground"] = '#ffffff'
        intdecimalButton["activebackground"] = '#212121'

        intplusButton["fg"] = '#ffffff'
        intplusButton["bg"] = '#212121'
        intplusButton["activeforeground"] = '#ffffff'
        intplusButton["activebackground"] = '#212121'

        intminusButton["fg"] = '#ffffff'
        intminusButton["bg"] = '#212121'
        intminusButton["activeforeground"] = '#ffffff'
        intminusButton["activebackground"] = '#212121'

        inttimesButton["fg"] = '#ffffff'
        inttimesButton["bg"] = '#212121'
        inttimesButton["activeforeground"] = '#ffffff'
        inttimesButton["activebackground"] = '#212121'

        intdivideButton["fg"] = '#ffffff'
        intdivideButton["bg"] = '#212121'
        intdivideButton["activeforeground"] = '#ffffff'
        intdivideButton["activebackground"] = '#212121'

        intdeleteButton["fg"] = '#ffffff'
        intdeleteButton["bg"] = '#402828'
        intdeleteButton["activeforeground"] = '#ffffff'
        intdeleteButton["activebackground"] = '#402828'

        intsinButton["fg"] = '#ffffff'
        intsinButton["bg"] = '#212121'
        intsinButton["activeforeground"] = '#ffffff'
        intsinButton["activebackground"] = '#212121'

        intcosButton["fg"] = '#ffffff'
        intcosButton["bg"] = '#212121'
        intcosButton["activeforeground"] = '#ffffff'
        intcosButton["activebackground"] = '#212121'

        inttanButton["fg"] = '#ffffff'
        inttanButton["bg"] = '#212121'
        inttanButton["activeforeground"] = '#ffffff'
        inttanButton["activebackground"] = '#212121'

        intasinButton["fg"] = '#ffffff'
        intasinButton["bg"] = '#212121'
        intasinButton["activeforeground"] = '#ffffff'
        intasinButton["activebackground"] = '#212121'

        intacosButton["fg"] = '#ffffff'
        intacosButton["bg"] = '#212121'
        intacosButton["activeforeground"] = '#ffffff'
        intacosButton["activebackground"] = '#212121'

        intatanButton["fg"] = '#ffffff'
        intatanButton["bg"] = '#212121'
        intatanButton["activeforeground"] = '#ffffff'
        intatanButton["activebackground"] = '#212121'

        intsinhButton["fg"] = '#ffffff'
        intsinhButton["bg"] = '#212121'
        intsinhButton["activeforeground"] = '#ffffff'
        intsinhButton["activebackground"] = '#212121'

        intcoshButton["fg"] = '#ffffff'
        intcoshButton["bg"] = '#212121'
        intcoshButton["activeforeground"] = '#ffffff'
        intcoshButton["activebackground"] = '#212121'

        inttanhButton["fg"] = '#ffffff'
        inttanhButton["bg"] = '#212121'
        inttanhButton["activeforeground"] = '#ffffff'
        inttanhButton["activebackground"] = '#212121'

        intasinhButton["fg"] = '#ffffff'
        intasinhButton["bg"] = '#212121'
        intasinhButton["activeforeground"] = '#ffffff'
        intasinhButton["activebackground"] = '#212121'

        intacoshButton["fg"] = '#ffffff'
        intacoshButton["bg"] = '#212121'
        intacoshButton["activeforeground"] = '#ffffff'
        intacoshButton["activebackground"] = '#212121'

        intatanhButton["fg"] = '#ffffff'
        intatanhButton["bg"] = '#212121'
        intatanhButton["activeforeground"] = '#ffffff'
        intatanhButton["activebackground"] = '#212121'

        diffpowerButton["fg"] = '#ffffff'
        diffpowerButton["bg"] = '#212121'
        diffpowerButton["activeforeground"] = '#ffffff'
        diffpowerButton["activebackground"] = '#212121'

        diffrootButton["fg"] = '#ffffff'
        diffrootButton["bg"] = '#212121'
        diffrootButton["activeforeground"] = '#ffffff'
        diffrootButton["activebackground"] = '#212121'

        diffmodulusButton["fg"] = '#ffffff'
        diffmodulusButton["bg"] = '#212121'
        diffmodulusButton["activeforeground"] = '#ffffff'
        diffmodulusButton["activebackground"] = '#212121'

        diffcommaButton["fg"] = '#ffffff'
        diffcommaButton["bg"] = '#212121'
        diffcommaButton["activeforeground"] = '#ffffff'
        diffcommaButton["activebackground"] = '#212121'

        diffleftbraceButton["fg"] = '#ffffff'
        diffleftbraceButton["bg"] = '#212121'
        diffleftbraceButton["activeforeground"] = '#ffffff'
        diffleftbraceButton["activebackground"] = '#212121'

        diffrightbraceButton["fg"] = '#ffffff'
        diffrightbraceButton["bg"] = '#212121'
        diffrightbraceButton["activeforeground"] = '#ffffff'
        diffrightbraceButton["activebackground"] = '#212121'

        diffeButton["fg"] = '#ffffff'
        diffeButton["bg"] = '#212121'
        diffeButton["activeforeground"] = '#ffffff'
        diffeButton["activebackground"] = '#212121'

        diffpiButton["fg"] = '#ffffff'
        diffpiButton["bg"] = '#212121'
        diffpiButton["activeforeground"] = '#ffffff'
        diffpiButton["activebackground"] = '#212121'

        diffnaturalButton["fg"] = '#ffffff'
        diffnaturalButton["bg"] = '#212121'
        diffnaturalButton["activeforeground"] = '#ffffff'
        diffnaturalButton["activebackground"] = '#212121'

        difflogButton["fg"] = '#ffffff'
        difflogButton["bg"] = '#212121'
        difflogButton["activeforeground"] = '#ffffff'
        difflogButton["activebackground"] = '#212121'

        diffsevenButton["fg"] = '#ffffff'
        diffsevenButton["bg"] = '#212121'
        diffsevenButton["activeforeground"] = '#ffffff'
        diffsevenButton["activebackground"] = '#212121'

        diffeightButton["fg"] = '#ffffff'
        diffeightButton["bg"] = '#212121'
        diffeightButton["activeforeground"] = '#ffffff'
        diffeightButton["activebackground"] = '#212121'

        diffnineButton["fg"] = '#ffffff'
        diffnineButton["bg"] = '#212121'
        diffnineButton["activeforeground"] = '#ffffff'
        diffnineButton["activebackground"] = '#212121'

        difffourButton["fg"] = '#ffffff'
        difffourButton["bg"] = '#212121'
        difffourButton["activeforeground"] = '#ffffff'
        difffourButton["activebackground"] = '#212121'

        difffiveButton["fg"] = '#ffffff'
        difffiveButton["bg"] = '#212121'
        difffiveButton["activeforeground"] = '#ffffff'
        difffiveButton["activebackground"] = '#212121'

        diffsixButton["fg"] = '#ffffff'
        diffsixButton["bg"] = '#212121'
        diffsixButton["activeforeground"] = '#ffffff'
        diffsixButton["activebackground"] = '#212121'

        diffoneButton["fg"] = '#ffffff'
        diffoneButton["bg"] = '#212121'
        diffoneButton["activeforeground"] = '#ffffff'
        diffoneButton["activebackground"] = '#212121'

        difftwoButton["fg"] = '#ffffff'
        difftwoButton["bg"] = '#212121'
        difftwoButton["activeforeground"] = '#ffffff'
        difftwoButton["activebackground"] = '#212121'

        diffthreeButton["fg"] = '#ffffff'
        diffthreeButton["bg"] = '#212121'
        diffthreeButton["activeforeground"] = '#ffffff'
        diffthreeButton["activebackground"] = '#212121'

        diffxButton["fg"] = '#ffffff'
        diffxButton["bg"] = '#303030'
        diffxButton["activeforeground"] = '#ffffff'
        diffxButton["activebackground"] = '#303030'

        diffzeroButton["fg"] = '#ffffff'
        diffzeroButton["bg"] = '#212121'
        diffzeroButton["activeforeground"] = '#ffffff'
        diffzeroButton["activebackground"] = '#212121'

        diffdecimalButton["fg"] = '#ffffff'
        diffdecimalButton["bg"] = '#212121'
        diffdecimalButton["activeforeground"] = '#ffffff'
        diffdecimalButton["activebackground"] = '#212121'

        diffplusButton["fg"] = '#ffffff'
        diffplusButton["bg"] = '#212121'
        diffplusButton["activeforeground"] = '#ffffff'
        diffplusButton["activebackground"] = '#212121'

        diffminusButton["fg"] = '#ffffff'
        diffminusButton["bg"] = '#212121'
        diffminusButton["activeforeground"] = '#ffffff'
        diffminusButton["activebackground"] = '#212121'

        difftimesButton["fg"] = '#ffffff'
        difftimesButton["bg"] = '#212121'
        difftimesButton["activeforeground"] = '#ffffff'
        difftimesButton["activebackground"] = '#212121'

        diffdivideButton["fg"] = '#ffffff'
        diffdivideButton["bg"] = '#212121'
        diffdivideButton["activeforeground"] = '#ffffff'
        diffdivideButton["activebackground"] = '#212121'

        diffdeleteButton["fg"] = '#ffffff'
        diffdeleteButton["bg"] = '#402828'
        diffdeleteButton["activeforeground"] = '#ffffff'
        diffdeleteButton["activebackground"] = '#402828'

        diffsinButton["fg"] = '#ffffff'
        diffsinButton["bg"] = '#212121'
        diffsinButton["activeforeground"] = '#ffffff'
        diffsinButton["activebackground"] = '#212121'

        diffcosButton["fg"] = '#ffffff'
        diffcosButton["bg"] = '#212121'
        diffcosButton["activeforeground"] = '#ffffff'
        diffcosButton["activebackground"] = '#212121'

        difftanButton["fg"] = '#ffffff'
        difftanButton["bg"] = '#212121'
        difftanButton["activeforeground"] = '#ffffff'
        difftanButton["activebackground"] = '#212121'

        diffasinButton["fg"] = '#ffffff'
        diffasinButton["bg"] = '#212121'
        diffasinButton["activeforeground"] = '#ffffff'
        diffasinButton["activebackground"] = '#212121'

        diffacosButton["fg"] = '#ffffff'
        diffacosButton["bg"] = '#212121'
        diffacosButton["activeforeground"] = '#ffffff'
        diffacosButton["activebackground"] = '#212121'

        diffatanButton["fg"] = '#ffffff'
        diffatanButton["bg"] = '#212121'
        diffatanButton["activeforeground"] = '#ffffff'
        diffatanButton["activebackground"] = '#212121'

        diffsinhButton["fg"] = '#ffffff'
        diffsinhButton["bg"] = '#212121'
        diffsinhButton["activeforeground"] = '#ffffff'
        diffsinhButton["activebackground"] = '#212121'

        diffcoshButton["fg"] = '#ffffff'
        diffcoshButton["bg"] = '#212121'
        diffcoshButton["activeforeground"] = '#ffffff'
        diffcoshButton["activebackground"] = '#212121'

        difftanhButton["fg"] = '#ffffff'
        difftanhButton["bg"] = '#212121'
        difftanhButton["activeforeground"] = '#ffffff'
        difftanhButton["activebackground"] = '#212121'

        diffasinhButton["fg"] = '#ffffff'
        diffasinhButton["bg"] = '#212121'
        diffasinhButton["activeforeground"] = '#ffffff'
        diffasinhButton["activebackground"] = '#212121'

        diffacoshButton["fg"] = '#ffffff'
        diffacoshButton["bg"] = '#212121'
        diffacoshButton["activeforeground"] = '#ffffff'
        diffacoshButton["activebackground"] = '#212121'

        diffatanhButton["fg"] = '#ffffff'
        diffatanhButton["bg"] = '#212121'
        diffatanhButton["activeforeground"] = '#ffffff'
        diffatanhButton["activebackground"] = '#212121'
        
        
    elif darkMode == True:
        darkMode = False
        
        equationsLabel["fg"] = '#000000'
        equationsLabel["bg"] = 'SystemButtonFace'
        graphFrame["bg"] = 'SystemButtonFace'
        root["bg"] = 'SystemButtonFace'
        
        backButton["fg"] = '#000000'
        backButton["bg"] = 'SystemButtonFace'
        backButton["activeforeground"] = '#000000'
        backButton["activebackground"] = 'SystemButtonFace'

        clearButton["fg"] = '#000000'
        clearButton["bg"] = '#fee0e0'
        clearButton["activeforeground"] = '#000000'
        clearButton["activebackground"] = '#fee0e0'

        yLabel1["fg"] = '#000000'
        yLabel1["bg"] = 'SystemButtonFace'
        yLabel2["fg"] = '#000000'
        yLabel2["bg"] = 'SystemButtonFace'
        yLabel3["fg"] = '#000000'
        yLabel3["bg"] = 'SystemButtonFace'
        yLabel4["fg"] = '#000000'
        yLabel4["bg"] = 'SystemButtonFace'
        yLabel5["fg"] = '#000000'
        yLabel5["bg"] = 'SystemButtonFace'
        yLabel6["fg"] = '#000000'
        yLabel6["bg"] = 'SystemButtonFace'
        yLabel7["fg"] = '#000000'
        yLabel7["bg"] = 'SystemButtonFace'
        yLabel8["fg"] = '#000000'
        yLabel8["bg"] = 'SystemButtonFace'
        yLabel9["fg"] = '#000000'
        yLabel9["bg"] = 'SystemButtonFace'
        yLabel10["fg"] = '#000000'
        yLabel10["bg"] = 'SystemButtonFace'
        yLabel11["fg"] = '#000000'
        yLabel11["bg"] = 'SystemButtonFace'
        yLabel12["fg"] = '#000000'
        yLabel12["bg"] = 'SystemButtonFace'
        yLabel13["fg"] = '#000000'
        yLabel13["bg"] = 'SystemButtonFace'
        yLabel14["fg"] = '#000000'
        yLabel14["bg"] = 'SystemButtonFace'
        yLabel15["fg"] = '#000000'
        yLabel15["bg"] = 'SystemButtonFace'
        yLabel16["fg"] = '#000000'
        yLabel16["bg"] = 'SystemButtonFace'
        yLabel17["fg"] = '#000000'
        yLabel17["bg"] = 'SystemButtonFace'
        yLabel18["fg"] = '#000000'
        yLabel18["bg"] = 'SystemButtonFace'
        yLabel19["fg"] = '#000000'
        yLabel19["bg"] = 'SystemButtonFace'
        yLabel20["fg"] = '#000000'
        yLabel20["bg"] = 'SystemButtonFace'

        expression1["fg"] = '#000000'
        expression1["insertbackground"] = '#000000'
        expression1["bg"] = '#ffffff'
        expression2["fg"] = '#000000'
        expression2["insertbackground"] = '#000000'
        expression2["bg"] = '#ffffff'
        expression3["fg"] = '#000000'
        expression3["insertbackground"] = '#000000'
        expression3["bg"] = '#ffffff'
        expression4["fg"] = '#000000'
        expression4["insertbackground"] = '#000000'
        expression4["bg"] = '#ffffff'
        expression5["fg"] = '#000000'
        expression5["insertbackground"] = '#000000'
        expression5["bg"] = '#ffffff'
        expression6["fg"] = '#000000'
        expression6["insertbackground"] = '#000000'
        expression6["bg"] = '#ffffff'
        expression7["fg"] = '#000000'
        expression7["insertbackground"] = '#000000'
        expression7["bg"] = '#ffffff'
        expression8["fg"] = '#000000'
        expression8["insertbackground"] = '#000000'
        expression8["bg"] = '#ffffff'
        expression9["fg"] = '#000000'
        expression9["insertbackground"] = '#000000'
        expression9["bg"] = '#ffffff'
        expression10["fg"] = '#000000'
        expression10["insertbackground"] = '#000000'
        expression10["bg"] = '#ffffff'
        expression11["fg"] = '#000000'
        expression11["insertbackground"] = '#000000'
        expression11["bg"] = '#ffffff'
        expression12["fg"] = '#000000'
        expression12["insertbackground"] = '#000000'
        expression12["bg"] = '#ffffff'
        expression13["fg"] = '#000000'
        expression13["insertbackground"] = '#000000'
        expression13["bg"] = '#ffffff'
        expression14["fg"] = '#000000'
        expression14["insertbackground"] = '#000000'
        expression14["bg"] = '#ffffff'
        expression15["fg"] = '#000000'
        expression15["insertbackground"] = '#000000'
        expression15["bg"] = '#ffffff'
        expression16["fg"] = '#000000'
        expression16["insertbackground"] = '#000000'
        expression16["bg"] = '#ffffff'
        expression17["fg"] = '#000000'
        expression17["insertbackground"] = '#000000'
        expression17["bg"] = '#ffffff'
        expression18["fg"] = '#000000'
        expression18["insertbackground"] = '#000000'
        expression18["bg"] = '#ffffff'
        expression19["fg"] = '#000000'
        expression19["insertbackground"] = '#000000'
        expression19["bg"] = '#ffffff'
        expression20["fg"] = '#000000'
        expression20["insertbackground"] = '#000000'
        expression20["bg"] = '#ffffff'

        colourButton1["bg"] = 'SystemButtonFace'
        colourButton1["activebackground"] = 'SystemButtonFace'
        colourButton2["bg"] = 'SystemButtonFace'
        colourButton2["activebackground"] = 'SystemButtonFace'
        colourButton3["bg"] = 'SystemButtonFace'
        colourButton3["activebackground"] = 'SystemButtonFace'
        colourButton4["bg"] = 'SystemButtonFace'
        colourButton4["activebackground"] = 'SystemButtonFace'
        colourButton5["bg"] = 'SystemButtonFace'
        colourButton5["activebackground"] = 'SystemButtonFace'
        colourButton6["bg"] = 'SystemButtonFace'
        colourButton6["activebackground"] = 'SystemButtonFace'
        colourButton7["bg"] = 'SystemButtonFace'
        colourButton7["activebackground"] = 'SystemButtonFace'
        colourButton8["bg"] = 'SystemButtonFace'
        colourButton8["activebackground"] = 'SystemButtonFace'
        colourButton9["bg"] = 'SystemButtonFace'
        colourButton9["activebackground"] = 'SystemButtonFace'
        colourButton10["bg"] = 'SystemButtonFace'
        colourButton10["activebackground"] = 'SystemButtonFace'
        colourButton11["bg"] = 'SystemButtonFace'
        colourButton11["activebackground"] = 'SystemButtonFace'
        colourButton12["bg"] = 'SystemButtonFace'
        colourButton12["activebackground"] = 'SystemButtonFace'
        colourButton13["bg"] = 'SystemButtonFace'
        colourButton13["activebackground"] = 'SystemButtonFace'
        colourButton14["bg"] = 'SystemButtonFace'
        colourButton14["activebackground"] = 'SystemButtonFace'
        colourButton15["bg"] = 'SystemButtonFace'
        colourButton15["activebackground"] = 'SystemButtonFace'
        colourButton16["bg"] = 'SystemButtonFace'
        colourButton16["activebackground"] = 'SystemButtonFace'
        colourButton17["bg"] = 'SystemButtonFace'
        colourButton17["activebackground"] = 'SystemButtonFace'
        colourButton18["bg"] = 'SystemButtonFace'
        colourButton18["activebackground"] = 'SystemButtonFace'
        colourButton19["bg"] = 'SystemButtonFace'
        colourButton19["activebackground"] = 'SystemButtonFace'
        colourButton20["bg"] = 'SystemButtonFace'
        colourButton20["activebackground"] = 'SystemButtonFace'

        expressionButton1["fg"] = '#000000'
        expressionButton1["bg"] = 'SystemButtonFace'
        expressionButton1["activeforeground"] = '#000000'
        expressionButton1["activebackground"] = 'SystemButtonFace'
        expressionButton2["fg"] = '#000000'
        expressionButton2["bg"] = 'SystemButtonFace'
        expressionButton2["activeforeground"] = '#000000'
        expressionButton2["activebackground"] = 'SystemButtonFace'
        expressionButton3["fg"] = '#000000'
        expressionButton3["bg"] = 'SystemButtonFace'
        expressionButton3["activeforeground"] = '#000000'
        expressionButton3["activebackground"] = 'SystemButtonFace'
        expressionButton4["fg"] = '#000000'
        expressionButton4["bg"] = 'SystemButtonFace'
        expressionButton4["activeforeground"] = '#000000'
        expressionButton4["activebackground"] = 'SystemButtonFace'
        expressionButton5["fg"] = '#000000'
        expressionButton5["bg"] = 'SystemButtonFace'
        expressionButton5["activeforeground"] = '#000000'
        expressionButton5["activebackground"] = 'SystemButtonFace'
        expressionButton6["fg"] = '#000000'
        expressionButton6["bg"] = 'SystemButtonFace'
        expressionButton6["activeforeground"] = '#000000'
        expressionButton6["activebackground"] = 'SystemButtonFace'
        expressionButton7["fg"] = '#000000'
        expressionButton7["bg"] = 'SystemButtonFace'
        expressionButton7["activeforeground"] = '#000000'
        expressionButton7["activebackground"] = 'SystemButtonFace'
        expressionButton8["fg"] = '#000000'
        expressionButton8["bg"] = 'SystemButtonFace'
        expressionButton8["activeforeground"] = '#000000'
        expressionButton8["activebackground"] = 'SystemButtonFace'
        expressionButton9["fg"] = '#000000'
        expressionButton9["bg"] = 'SystemButtonFace'
        expressionButton9["activeforeground"] = '#000000'
        expressionButton9["activebackground"] = 'SystemButtonFace'
        expressionButton10["fg"] = '#000000'
        expressionButton10["bg"] = 'SystemButtonFace'
        expressionButton10["activeforeground"] = '#000000'
        expressionButton10["activebackground"] = 'SystemButtonFace'
        expressionButton11["fg"] = '#000000'
        expressionButton11["bg"] = 'SystemButtonFace'
        expressionButton11["activeforeground"] = '#000000'
        expressionButton11["activebackground"] = 'SystemButtonFace'
        expressionButton12["fg"] = '#000000'
        expressionButton12["bg"] = 'SystemButtonFace'
        expressionButton12["activeforeground"] = '#000000'
        expressionButton12["activebackground"] = 'SystemButtonFace'
        expressionButton13["fg"] = '#000000'
        expressionButton13["bg"] = 'SystemButtonFace'
        expressionButton13["activeforeground"] = '#000000'
        expressionButton13["activebackground"] = 'SystemButtonFace'
        expressionButton14["fg"] = '#000000'
        expressionButton14["bg"] = 'SystemButtonFace'
        expressionButton14["activeforeground"] = '#000000'
        expressionButton14["activebackground"] = 'SystemButtonFace'
        expressionButton15["fg"] = '#000000'
        expressionButton15["bg"] = 'SystemButtonFace'
        expressionButton15["activeforeground"] = '#000000'
        expressionButton15["activebackground"] = 'SystemButtonFace'
        expressionButton16["fg"] = '#000000'
        expressionButton16["bg"] = 'SystemButtonFace'
        expressionButton16["activeforeground"] = '#000000'
        expressionButton16["activebackground"] = 'SystemButtonFace'
        expressionButton17["fg"] = '#000000'
        expressionButton17["bg"] = 'SystemButtonFace'
        expressionButton17["activeforeground"] = '#000000'
        expressionButton17["activebackground"] = 'SystemButtonFace'
        expressionButton18["fg"] = '#000000'
        expressionButton18["bg"] = 'SystemButtonFace'
        expressionButton18["activeforeground"] = '#000000'
        expressionButton18["activebackground"] = 'SystemButtonFace'
        expressionButton19["fg"] = '#000000'
        expressionButton19["bg"] = 'SystemButtonFace'
        expressionButton19["activeforeground"] = '#000000'
        expressionButton19["activebackground"] = 'SystemButtonFace'
        expressionButton20["fg"] = '#000000'
        expressionButton20["bg"] = 'SystemButtonFace'
        expressionButton20["activeforeground"] = '#000000'
        expressionButton20["activebackground"] = 'SystemButtonFace'

        powerButton["fg"] = '#000000'
        powerButton["bg"] = 'SystemButtonFace'
        powerButton["activeforeground"] = '#000000'
        powerButton["activebackground"] = 'SystemButtonFace'

        rootButton["fg"] = '#000000'
        rootButton["bg"] = 'SystemButtonFace'
        rootButton["activeforeground"] = '#000000'
        rootButton["activebackground"] = 'SystemButtonFace'

        modulusButton["fg"] = '#000000'
        modulusButton["bg"] = 'SystemButtonFace'
        modulusButton["activeforeground"] = '#000000'
        modulusButton["activebackground"] = 'SystemButtonFace'

        commaButton["fg"] = '#000000'
        commaButton["bg"] = 'SystemButtonFace'
        commaButton["activeforeground"] = '#000000'
        commaButton["activebackground"] = 'SystemButtonFace'

        leftbraceButton["fg"] = '#000000'
        leftbraceButton["bg"] = 'SystemButtonFace'
        leftbraceButton["activeforeground"] = '#000000'
        leftbraceButton["activebackground"] = 'SystemButtonFace'

        rightbraceButton["fg"] = '#000000'
        rightbraceButton["bg"] = 'SystemButtonFace'
        rightbraceButton["activeforeground"] = '#000000'
        rightbraceButton["activebackground"] = 'SystemButtonFace'

        eButton["fg"] = '#000000'
        eButton["bg"] = 'SystemButtonFace'
        eButton["activeforeground"] = '#000000'
        eButton["activebackground"] = 'SystemButtonFace'

        piButton["fg"] = '#000000'
        piButton["bg"] = 'SystemButtonFace'
        piButton["activeforeground"] = '#000000'
        piButton["activebackground"] = 'SystemButtonFace'

        naturalButton["fg"] = '#000000'
        naturalButton["bg"] = 'SystemButtonFace'
        naturalButton["activeforeground"] = '#000000'
        naturalButton["activebackground"] = 'SystemButtonFace'

        logButton["fg"] = '#000000'
        logButton["bg"] = 'SystemButtonFace'
        logButton["activeforeground"] = '#000000'
        logButton["activebackground"] = 'SystemButtonFace'

        sevenButton["fg"] = '#000000'
        sevenButton["bg"] = 'SystemButtonFace'
        sevenButton["activeforeground"] = '#000000'
        sevenButton["activebackground"] = 'SystemButtonFace'

        eightButton["fg"] = '#000000'
        eightButton["bg"] = 'SystemButtonFace'
        eightButton["activeforeground"] = '#000000'
        eightButton["activebackground"] = 'SystemButtonFace'

        nineButton["fg"] = '#000000'
        nineButton["bg"] = 'SystemButtonFace'
        nineButton["activeforeground"] = '#000000'
        nineButton["activebackground"] = 'SystemButtonFace'

        fourButton["fg"] = '#000000'
        fourButton["bg"] = 'SystemButtonFace'
        fourButton["activeforeground"] = '#000000'
        fourButton["activebackground"] = 'SystemButtonFace'

        fiveButton["fg"] = '#000000'
        fiveButton["bg"] = 'SystemButtonFace'
        fiveButton["activeforeground"] = '#000000'
        fiveButton["activebackground"] = 'SystemButtonFace'

        sixButton["fg"] = '#000000'
        sixButton["bg"] = 'SystemButtonFace'
        sixButton["activeforeground"] = '#000000'
        sixButton["activebackground"] = 'SystemButtonFace'

        oneButton["fg"] = '#000000'
        oneButton["bg"] = 'SystemButtonFace'
        oneButton["activeforeground"] = '#000000'
        oneButton["activebackground"] = 'SystemButtonFace'

        twoButton["fg"] = '#000000'
        twoButton["bg"] = 'SystemButtonFace'
        twoButton["activeforeground"] = '#000000'
        twoButton["activebackground"] = 'SystemButtonFace'

        threeButton["fg"] = '#000000'
        threeButton["bg"] = 'SystemButtonFace'
        threeButton["activeforeground"] = '#000000'
        threeButton["activebackground"] = 'SystemButtonFace'

        xButton["fg"] = '#000000'
        xButton["bg"] = '#dddddd'
        xButton["activeforeground"] = '#000000'
        xButton["activebackground"] = '#dddddd'

        zeroButton["fg"] = '#000000'
        zeroButton["bg"] = 'SystemButtonFace'
        zeroButton["activeforeground"] = '#000000'
        zeroButton["activebackground"] = 'SystemButtonFace'

        decimalButton["fg"] = '#000000'
        decimalButton["bg"] = 'SystemButtonFace'
        decimalButton["activeforeground"] = '#000000'
        decimalButton["activebackground"] = 'SystemButtonFace'

        plusButton["fg"] = '#000000'
        plusButton["bg"] = 'SystemButtonFace'
        plusButton["activeforeground"] = '#000000'
        plusButton["activebackground"] = 'SystemButtonFace'

        minusButton["fg"] = '#000000'
        minusButton["bg"] = 'SystemButtonFace'
        minusButton["activeforeground"] = '#000000'
        minusButton["activebackground"] = 'SystemButtonFace'

        timesButton["fg"] = '#000000'
        timesButton["bg"] = 'SystemButtonFace'
        timesButton["activeforeground"] = '#000000'
        timesButton["activebackground"] = 'SystemButtonFace'

        divideButton["fg"] = '#000000'
        divideButton["bg"] = 'SystemButtonFace'
        divideButton["activeforeground"] = '#000000'
        divideButton["activebackground"] = 'SystemButtonFace'

        deleteButton["fg"] = '#000000'
        deleteButton["bg"] = '#fee0e0'
        deleteButton["activeforeground"] = '#000000'
        deleteButton["activebackground"] = '#fee0e0'

        sinButton["fg"] = '#000000'
        sinButton["bg"] = 'SystemButtonFace'
        sinButton["activeforeground"] = '#000000'
        sinButton["activebackground"] = 'SystemButtonFace'

        cosButton["fg"] = '#000000'
        cosButton["bg"] = 'SystemButtonFace'
        cosButton["activeforeground"] = '#000000'
        cosButton["activebackground"] = 'SystemButtonFace'

        tanButton["fg"] = '#000000'
        tanButton["bg"] = 'SystemButtonFace'
        tanButton["activeforeground"] = '#000000'
        tanButton["activebackground"] = 'SystemButtonFace'

        asinButton["fg"] = '#000000'
        asinButton["bg"] = 'SystemButtonFace'
        asinButton["activeforeground"] = '#000000'
        asinButton["activebackground"] = 'SystemButtonFace'

        acosButton["fg"] = '#000000'
        acosButton["bg"] = 'SystemButtonFace'
        acosButton["activeforeground"] = '#000000'
        acosButton["activebackground"] = 'SystemButtonFace'

        atanButton["fg"] = '#000000'
        atanButton["bg"] = 'SystemButtonFace'
        atanButton["activeforeground"] = '#000000'
        atanButton["activebackground"] = 'SystemButtonFace'

        sinhButton["fg"] = '#000000'
        sinhButton["bg"] = 'SystemButtonFace'
        sinhButton["activeforeground"] = '#000000'
        sinhButton["activebackground"] = 'SystemButtonFace'

        coshButton["fg"] = '#000000'
        coshButton["bg"] = 'SystemButtonFace'
        coshButton["activeforeground"] = '#000000'
        coshButton["activebackground"] = 'SystemButtonFace'

        tanhButton["fg"] = '#000000'
        tanhButton["bg"] = 'SystemButtonFace'
        tanhButton["activeforeground"] = '#000000'
        tanhButton["activebackground"] = 'SystemButtonFace'

        asinhButton["fg"] = '#000000'
        asinhButton["bg"] = 'SystemButtonFace'
        asinhButton["activeforeground"] = '#000000'
        asinhButton["activebackground"] = 'SystemButtonFace'

        acoshButton["fg"] = '#000000'
        acoshButton["bg"] = 'SystemButtonFace'
        acoshButton["activeforeground"] = '#000000'
        acoshButton["activebackground"] = 'SystemButtonFace'

        atanhButton["fg"] = '#000000'
        atanhButton["bg"] = 'SystemButtonFace'
        atanhButton["activeforeground"] = '#000000'
        atanhButton["activebackground"] = 'SystemButtonFace'

        zoomInButton["fg"] = '#000000'
        zoomInButton["bg"] = 'SystemButtonFace'
        zoomInButton["activeforeground"] = '#000000'
        zoomInButton["activebackground"] = 'SystemButtonFace'

        zoomOutButton["fg"] = '#000000'
        zoomOutButton["bg"] = 'SystemButtonFace'
        zoomOutButton["activeforeground"] = '#000000'
        zoomOutButton["activebackground"] = 'SystemButtonFace'

        graph["bg"] = '#ffffff'

    redrawgraph()
        

def calcProbSolver():
    calcProbSolverMenu = Frame(root, width=screensize[0], height=screensize[1])

    Button7 = Button(calcProbSolverMenu, image=diffImage, width=300, height=320, command=lambda:[calcProbSolverMenu.place_forget(), differentiation()])
    Button7.place(relx=0.35, rely=0.5, anchor=CENTER)
    diffLabel = Label(calcProbSolverMenu, text="Differentiation")
    diffLabel.place(relx=0.35, rely=0.75, anchor=CENTER)
    diffLabel.config(font=boldFont)

    Button8 = Button(calcProbSolverMenu, image=intImage, width=300, height=320, command=lambda:[calcProbSolverMenu.place_forget(), integration()])
    Button8.place(relx=0.65, rely=0.5, anchor=CENTER)
    intLabel = Label(calcProbSolverMenu, text="Integration")
    intLabel.place(relx=0.65, rely=0.75, anchor=CENTER)
    intLabel.config(font=boldFont)

    backButton = Button(calcProbSolverMenu, text="Back", command=lambda:[calcProbSolverMenu.destroy(), mainMenu()])
    backButton.place(relx=0.005, rely=0.05, anchor=NW)
    backButton.config(font=buttonFont)

    if darkMode == True:
        Button7.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121', image=darkDiffImage)
        Button8.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121', image=darkIntImage)
        diffLabel.config(fg='#ffffff', bg='#212121')
        intLabel.config(fg='#ffffff', bg='#212121')
        backButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        calcProbSolverMenu.config(bg='#212121')
    
    calcProbSolverMenu.place(relx=0.5, rely=0.5, anchor=CENTER)

def differentiation():

    diffTitle = Label(diffMenu, text="Differentiation")
    diffTitle.place(relx=0.5, rely=0.15, anchor=CENTER)
    diffTitle.config(font=titleFont)
    
    backButton = Button(diffMenu, text="Back", command=lambda:[diffMenu.place_forget(), calcProbSolver()])
    backButton.place(relx=0.005, rely=0.05, anchor=NW)
    backButton.config(font=buttonFont)

    ddxlbl = Label(diffMenu, image=ddxImage)
    ddxlbl.place(relx=0.277, rely=0.45, anchor=CENTER)

    bracket1 = Label(diffMenu, text="(", font=("Times New Roman", 35))
    bracket1.place(relx=0.31, rely=0.446, anchor=CENTER)

    bracket2 = Label(diffMenu, text=")", font=("Times New Roman", 35))
    bracket2.place(relx=0.69, rely=0.446, anchor=CENTER)
    
    difflbl = Label(diffUnderFrame, font=("Cambria Math", 22, "italic"))
    difflbl.place(relx=0.5, rely=0.62, anchor=CENTER)

    doneDiffButton = Button(diffMenu, text="=", width=2, command=lambda:[getDiffExpression(), difflbl.config(text=deriv)])
    doneDiffButton.place(relx=0.72, rely=0.45, anchor=CENTER)
    doneDiffButton.config(font=buttonFont)

    if darkMode == True:
        backButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        diffTitle.config(fg='#ffffff', bg='#212121')
        diffUnderFrame.config(bg='#212121')
        ddxlbl.config(image=darkDdxImage, bg='#212121', highlightthickness=4, highlightbackground='#212121')
        bracket1.config(fg='#ffffff', bg='#212121')
        bracket2.config(fg='#ffffff', bg='#212121')
        difflbl.config(fg='#ffffff', bg='#212121')
        diffInput["fg"] = '#ffffff'
        diffInput["insertbackground"] = '#dfdfdf'
        diffInput["bg"] = '#303030'
        doneDiffButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        diffMenu.config(bg='#212121')
    elif darkMode == False:
        diffMenu.config(bg='SystemButtonFace')
        diffUnderFrame.config(bg='SystemButtonFace')
        ddxlbl.config(bg='SystemButtonFace', highlightthickness=0.01, highlightbackground='SystemButtonFace')

    if diffInput.get() != "":
        doneDiffButton.invoke()

    diffMenu.place(relx=0.5, rely=0.5, anchor=CENTER)

def getDiffExpression():
    global diffExpression
    global diffInput
    global deriv
    
    diffExpression = diffInput.get()
    deriv = smp.diff(diffExpression, ex)  
    
diffMenu = Frame(root, width=screensize[0], height=screensize[1])

ex=smp.symbols('x') 

diffInput = Entry(diffMenu, width=30, font=("Cambria", 20))
diffInput.place(relx=0.5, rely=0.45, anchor=CENTER)

def callback_diffInput_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = diffInput
    numberPressed = False
    closingBracketPressed = False

diffInput.bind("<FocusIn>", callback_diffInput_focus)

diffUnderFrame = Frame(diffMenu, width=screensize[0], height=(screensize[1]/10))
diffUnderFrame.place(relx=0.5, rely=0.55, anchor=CENTER)

diffsevenButton = Button(diffMenu, text="7", width=3, command=lambda:[insertsymbol("7"), pressnumber(1), pressclosingBracket(0)])
diffsevenButton.place(relx=0.475, rely=0.7, anchor=CENTER)

diffeightButton = Button(diffMenu, text="8", width=3, command=lambda:[insertsymbol("8"), pressnumber(1), pressclosingBracket(0)])
diffeightButton.place(relx=0.5, rely=0.7, anchor=CENTER)

diffnineButton = Button(diffMenu, text="9", width=3, command=lambda:[insertsymbol("9"), pressnumber(1), pressclosingBracket(0)])
diffnineButton.place(relx=0.525, rely=0.7, anchor=CENTER)

difffourButton = Button(diffMenu, text="4", width=3, command=lambda:[insertsymbol("4"), pressnumber(1), pressclosingBracket(0)])
difffourButton.place(relx=0.475, rely=0.74, anchor=CENTER)

difffiveButton = Button(diffMenu, text="5", width=3, command=lambda:[insertsymbol("5"), pressnumber(1), pressclosingBracket(0)])
difffiveButton.place(relx=0.5, rely=0.74, anchor=CENTER)

diffsixButton = Button(diffMenu, text="6", width=3, command=lambda:[insertsymbol("6"), pressnumber(1), pressclosingBracket(0)])
diffsixButton.place(relx=0.525, rely=0.74, anchor=CENTER)

diffoneButton = Button(diffMenu, text="1", width=3, command=lambda:[insertsymbol("1"), pressnumber(1), pressclosingBracket(0)])
diffoneButton.place(relx=0.475, rely=0.78, anchor=CENTER)

difftwoButton = Button(diffMenu, text="2", width=3, command=lambda:[insertsymbol("2"), pressnumber(1), pressclosingBracket(0)])
difftwoButton.place(relx=0.5, rely=0.78, anchor=CENTER)

diffthreeButton = Button(diffMenu, text="3", width=3, command=lambda:[insertsymbol("3"), pressnumber(1), pressclosingBracket(0)])
diffthreeButton.place(relx=0.525, rely=0.78, anchor=CENTER)

diffxButton = Button(diffMenu, text="𝑥", width=3, bg='#dddddd', activebackground='#dddddd', command=lambda:[insertsymbol("x"), inserttimes(), pressclosingBracket(0)])
diffxButton.place(relx=0.475, rely=0.82, anchor=CENTER)

diffzeroButton = Button(diffMenu, text="0", width=3, command=lambda:[insertsymbol("0"), pressnumber(1), pressclosingBracket(0)])
diffzeroButton.place(relx=0.5, rely=0.82, anchor=CENTER)

diffdecimalButton = Button(diffMenu, text=".", width=3, command=lambda:[insertsymbol("."), pressnumber(0), pressclosingBracket(0)])
diffdecimalButton.place(relx=0.525, rely=0.82, anchor=CENTER)

diffplusButton = Button(diffMenu, text="+", width=2, command=lambda:[insertsymbol("+"), pressnumber(0), pressclosingBracket(0)])
diffplusButton.place(relx=0.55, rely=0.7, anchor=CENTER)

diffminusButton = Button(diffMenu, text="–", width=2, command=lambda:[insertsymbol("-"), pressnumber(0), pressclosingBracket(0)])
diffminusButton.place(relx=0.55, rely=0.74, anchor=CENTER)

difftimesButton = Button(diffMenu, text="×", width=2, command=lambda:[insertsymbol("*"), pressnumber(0), pressclosingBracket(0)])
difftimesButton.place(relx=0.55, rely=0.78, anchor=CENTER)

diffdivideButton = Button(diffMenu, text="÷", width=2, command=lambda:[insertsymbol("/"), pressnumber(0), pressclosingBracket(0)])
diffdivideButton.place(relx=0.55, rely=0.82, anchor=CENTER)

diffpowerButton = Button(diffMenu, text="^", width=3, command=lambda:[insertsymbol("**"), pressnumber(0), pressclosingBracket(0)])
diffpowerButton.place(relx=0.345, rely=0.7, anchor=CENTER)

diffrootButton = Button(diffMenu, text="√", width=3, command=lambda:[insertsymbol("sqrt("), pressnumber(0), pressclosingBracket(0)])
diffrootButton.place(relx=0.37, rely=0.7, anchor=CENTER)

diffmodulusButton = Button(diffMenu, text="|  |", width=3, command=lambda:[insertsymbol("abs("), pressnumber(0), pressclosingBracket(0)])
diffmodulusButton.place(relx=0.395, rely=0.7, anchor=CENTER)

diffcommaButton = Button(diffMenu, text=",", width=3, command=lambda:[insertsymbol(","), pressnumber(0), pressclosingBracket(0)])
diffcommaButton.place(relx=0.42, rely=0.7, anchor=CENTER)

diffleftbraceButton = Button(diffMenu, text="(", width=3, command=lambda:[insertsymbol("("), pressnumber(0),insertBracketTimes(), pressclosingBracket(0)])
diffleftbraceButton.place(relx=0.345, rely=0.74, anchor=CENTER)

diffrightbraceButton = Button(diffMenu, text=")", width=3, command=lambda:[insertsymbol(")"), pressnumber(0), pressclosingBracket(1)])
diffrightbraceButton.place(relx=0.37, rely=0.74, anchor=CENTER)

diffeButton = Button(diffMenu, text="e", width=3, command=lambda:[insertsymbol("exp("), pressnumber(1), pressclosingBracket(0)])
diffeButton.place(relx=0.395, rely=0.74, anchor=CENTER)

diffpiButton = Button(diffMenu, text="π", width=3, command=lambda:[insertsymbol("pi"), pressnumber(1), pressclosingBracket(0)])
diffpiButton.place(relx=0.42, rely=0.74, anchor=CENTER)

diffnaturalButton = Button(diffMenu, text="ln", width=3, command=lambda:[insertsymbol("log("), pressnumber(0), pressclosingBracket(0)])
diffnaturalButton.place(relx=0.37, rely=0.78, anchor=CENTER)

difflogButton = Button(diffMenu, text="log", width=3, command=lambda:[insertsymbol("log(,"), pressnumber(0), pressclosingBracket(0)])
difflogButton.place(relx=0.395, rely=0.78, anchor=CENTER)

diffdeleteButton = Button(diffMenu, text="←", width=10, bg="#fee0e0", activebackground="#fee0e0", command=lambda:[deletesymbol(), pressnumber(0), pressclosingBracket(0)])
diffdeleteButton.place(relx=0.654, rely=0.66, anchor=CENTER)

diffsinButton = Button(diffMenu, text="sin", width=4, command=lambda:[insertsymbol("sin("), pressnumber(0), pressclosingBracket(0)])
diffsinButton.place(relx=0.61, rely=0.7, anchor=CENTER)

diffcosButton = Button(diffMenu, text="cos", width=4, command=lambda:[insertsymbol("cos("), pressnumber(0), pressclosingBracket(0)])
diffcosButton.place(relx=0.64, rely=0.7, anchor=CENTER)

difftanButton = Button(diffMenu, text="tan", width=4, command=lambda:[insertsymbol("tan("), pressnumber(0), pressclosingBracket(0)])
difftanButton.place(relx=0.67, rely=0.7, anchor=CENTER)

diffasinButton = Button(diffMenu, text="arcsin", width=4, command=lambda:[insertsymbol("asin("), pressnumber(0), pressclosingBracket(0)])
diffasinButton.place(relx=0.61, rely=0.74, anchor=CENTER)

diffacosButton = Button(diffMenu, text="arccos", width=4, command=lambda:[insertsymbol("acos("), pressnumber(0), pressclosingBracket(0)])
diffacosButton.place(relx=0.64, rely=0.74, anchor=CENTER)

diffatanButton = Button(diffMenu, text="arctan", width=4, command=lambda:[insertsymbol("atan("), pressnumber(0), pressclosingBracket(0)])
diffatanButton.place(relx=0.67, rely=0.74, anchor=CENTER)

diffsinhButton = Button(diffMenu, text="sinh", width=4, command=lambda:[insertsymbol("sinh("), pressnumber(0), pressclosingBracket(0)])
diffsinhButton.place(relx=0.61, rely=0.78, anchor=CENTER)

diffcoshButton = Button(diffMenu, text="cosh", width=4, command=lambda:[insertsymbol("cosh("), pressnumber(0), pressclosingBracket(0)])
diffcoshButton.place(relx=0.64, rely=0.78, anchor=CENTER)

difftanhButton = Button(diffMenu, text="tanh", width=4, command=lambda:[insertsymbol("tanh("), pressnumber(0), pressclosingBracket(0)])
difftanhButton.place(relx=0.67, rely=0.78, anchor=CENTER)

diffasinhButton = Button(diffMenu, text="arsinh", width=4, command=lambda:[insertsymbol("asinh("), pressnumber(0), pressclosingBracket(0)])
diffasinhButton.place(relx=0.61, rely=0.82, anchor=CENTER)

diffacoshButton = Button(diffMenu, text="arcosh", width=4, command=lambda:[insertsymbol("acosh("), pressnumber(0), pressclosingBracket(0)])
diffacoshButton.place(relx=0.64, rely=0.82, anchor=CENTER)

diffatanhButton = Button(diffMenu, text="artanh", width=4, command=lambda:[insertsymbol("atanh("), pressnumber(0), pressclosingBracket(0)])
diffatanhButton.place(relx=0.67, rely=0.82, anchor=CENTER)

def integration():

    intTitle = Label(intMenu, text="Integration")
    intTitle.place(relx=0.5, rely=0.15, anchor=CENTER)
    intTitle.config(font=titleFont)
    
    backButton = Button(intMenu, text="Back", command=lambda:[intMenu.place_forget(), calcProbSolver()])
    backButton.place(relx=0.005, rely=0.05, anchor=NW)
    backButton.config(font=buttonFont)

    intgrllbl = Label(intMenu, image=intgrlImage)
    intgrllbl.place(relx=0.29, rely=0.45, anchor=CENTER)

    bracket1 = Label(intMenu, text="(", font=("Times New Roman", 35))
    bracket1.place(relx=0.31, rely=0.446, anchor=CENTER)

    bracket2 = Label(intMenu, text=")", font=("Times New Roman", 35))
    bracket2.place(relx=0.69, rely=0.446, anchor=CENTER)

    dxlbl = Label(intMenu, image=dxImage)
    dxlbl.place(relx=0.713, rely=0.45, anchor=CENTER)
    
    intlbl = Label(intUnderFrame, font=("Cambria Math", 22, "italic"))
    intlbl.place(relx=0.5, rely=0.5, anchor=CENTER)

    doneIntButton = Button(intMenu, text="=", width=2, command=lambda:[getIntExpression(), intlbl.config(text=integral)])
    doneIntButton.place(relx=0.75, rely=0.45, anchor=CENTER)
    doneIntButton.config(font=buttonFont)

    if darkMode == True:
        backButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        intTitle.config(fg='#ffffff', bg='#212121')
        intUnderFrame.config(bg='#212121')
        intgrllbl.config(image=darkIntgrlImage, bg='#212121', highlightthickness=4, highlightbackground='#212121')
        bracket1.config(fg='#ffffff', bg='#212121')
        bracket2.config(fg='#ffffff', bg='#212121')
        dxlbl.config(image=darkDxImage, bg='#212121')
        intlbl.config(fg='#ffffff', bg='#212121')
        intInput["fg"] = '#ffffff'
        intInput["insertbackground"] = '#dfdfdf'
        intInput["bg"] = '#303030'
        doneIntButton.config(fg='#ffffff', bg='#212121', activeforeground='#ffffff', activebackground='#212121')
        intMenu.config(bg='#212121')
    elif darkMode == False:
        intMenu.config(bg='SystemButtonFace')
        intUnderFrame.config(bg='SystemButtonFace')
        intgrllbl.config(bg='SystemButtonFace', highlightthickness=0.01, highlightbackground='SystemButtonFace')


    if intInput.get() != "":
        doneIntButton.invoke()

    intMenu.place(relx=0.5, rely=0.5, anchor=CENTER)

def getIntExpression():
    global intExpression
    global intInput
    global integral
    
    intExpression = intInput.get()
    integral = smp.integrate(intExpression, ex)
    integral = str(integral) + " + c"
    
intMenu = Frame(root, width=screensize[0], height=screensize[1])
    
intInput = Entry(intMenu, width=30, font=("Cambria", 20))
intInput.place(relx=0.5, rely=0.45, anchor=CENTER)

def callback_intInput_focus(event):
    global currentEntry
    global numberPressed
    global closingBracketPressed
    currentEntry = intInput
    numberPressed = False
    closingBracketPressed = False

intInput.bind("<FocusIn>", callback_intInput_focus)

intUnderFrame = Frame(intMenu, width=screensize[0], height=(screensize[1]/10))
intUnderFrame.place(relx=0.5, rely=0.55, anchor=CENTER)

intsevenButton = Button(intMenu, text="7", width=3, command=lambda:[insertsymbol("7"), pressnumber(1), pressclosingBracket(0)])
intsevenButton.place(relx=0.475, rely=0.7, anchor=CENTER)

inteightButton = Button(intMenu, text="8", width=3, command=lambda:[insertsymbol("8"), pressnumber(1), pressclosingBracket(0)])
inteightButton.place(relx=0.5, rely=0.7, anchor=CENTER)

intnineButton = Button(intMenu, text="9", width=3, command=lambda:[insertsymbol("9"), pressnumber(1), pressclosingBracket(0)])
intnineButton.place(relx=0.525, rely=0.7, anchor=CENTER)

intfourButton = Button(intMenu, text="4", width=3, command=lambda:[insertsymbol("4"), pressnumber(1), pressclosingBracket(0)])
intfourButton.place(relx=0.475, rely=0.74, anchor=CENTER)

intfiveButton = Button(intMenu, text="5", width=3, command=lambda:[insertsymbol("5"), pressnumber(1), pressclosingBracket(0)])
intfiveButton.place(relx=0.5, rely=0.74, anchor=CENTER)

intsixButton = Button(intMenu, text="6", width=3, command=lambda:[insertsymbol("6"), pressnumber(1), pressclosingBracket(0)])
intsixButton.place(relx=0.525, rely=0.74, anchor=CENTER)

intoneButton = Button(intMenu, text="1", width=3, command=lambda:[insertsymbol("1"), pressnumber(1), pressclosingBracket(0)])
intoneButton.place(relx=0.475, rely=0.78, anchor=CENTER)

inttwoButton = Button(intMenu, text="2", width=3, command=lambda:[insertsymbol("2"), pressnumber(1), pressclosingBracket(0)])
inttwoButton.place(relx=0.5, rely=0.78, anchor=CENTER)

intthreeButton = Button(intMenu, text="3", width=3, command=lambda:[insertsymbol("3"), pressnumber(1), pressclosingBracket(0)])
intthreeButton.place(relx=0.525, rely=0.78, anchor=CENTER)

intxButton = Button(intMenu, text="𝑥", width=3, bg='#dddddd', activebackground='#dddddd', command=lambda:[insertsymbol("x"), inserttimes(), pressclosingBracket(0)])
intxButton.place(relx=0.475, rely=0.82, anchor=CENTER)

intzeroButton = Button(intMenu, text="0", width=3, command=lambda:[insertsymbol("0"), pressnumber(1), pressclosingBracket(0)])
intzeroButton.place(relx=0.5, rely=0.82, anchor=CENTER)

intdecimalButton = Button(intMenu, text=".", width=3, command=lambda:[insertsymbol("."), pressnumber(0), pressclosingBracket(0)])
intdecimalButton.place(relx=0.525, rely=0.82, anchor=CENTER)

intplusButton = Button(intMenu, text="+", width=2, command=lambda:[insertsymbol("+"), pressnumber(0), pressclosingBracket(0)])
intplusButton.place(relx=0.55, rely=0.7, anchor=CENTER)

intminusButton = Button(intMenu, text="–", width=2, command=lambda:[insertsymbol("-"), pressnumber(0), pressclosingBracket(0)])
intminusButton.place(relx=0.55, rely=0.74, anchor=CENTER)

inttimesButton = Button(intMenu, text="×", width=2, command=lambda:[insertsymbol("*"), pressnumber(0), pressclosingBracket(0)])
inttimesButton.place(relx=0.55, rely=0.78, anchor=CENTER)

intdivideButton = Button(intMenu, text="÷", width=2, command=lambda:[insertsymbol("/"), pressnumber(0), pressclosingBracket(0)])
intdivideButton.place(relx=0.55, rely=0.82, anchor=CENTER)

intpowerButton = Button(intMenu, text="^", width=3, command=lambda:[insertsymbol("**"), pressnumber(0), pressclosingBracket(0)])
intpowerButton.place(relx=0.345, rely=0.7, anchor=CENTER)

introotButton = Button(intMenu, text="√", width=3, command=lambda:[insertsymbol("sqrt("), pressnumber(0), pressclosingBracket(0)])
introotButton.place(relx=0.37, rely=0.7, anchor=CENTER)

intmodulusButton = Button(intMenu, text="|  |", width=3, command=lambda:[insertsymbol("abs("), pressnumber(0), pressclosingBracket(0)])
intmodulusButton.place(relx=0.395, rely=0.7, anchor=CENTER)

intcommaButton = Button(intMenu, text=",", width=3, command=lambda:[insertsymbol(","), pressnumber(0), pressclosingBracket(0)])
intcommaButton.place(relx=0.42, rely=0.7, anchor=CENTER)

intleftbraceButton = Button(intMenu, text="(", width=3, command=lambda:[insertsymbol("("), pressnumber(0),insertBracketTimes(), pressclosingBracket(0)])
intleftbraceButton.place(relx=0.345, rely=0.74, anchor=CENTER)

intrightbraceButton = Button(intMenu, text=")", width=3, command=lambda:[insertsymbol(")"), pressnumber(0), pressclosingBracket(1)])
intrightbraceButton.place(relx=0.37, rely=0.74, anchor=CENTER)

inteButton = Button(intMenu, text="e", width=3, command=lambda:[insertsymbol("exp("), pressnumber(1), pressclosingBracket(0)])
inteButton.place(relx=0.395, rely=0.74, anchor=CENTER)

intpiButton = Button(intMenu, text="π", width=3, command=lambda:[insertsymbol("pi"), pressnumber(1), pressclosingBracket(0)])
intpiButton.place(relx=0.42, rely=0.74, anchor=CENTER)

intnaturalButton = Button(intMenu, text="ln", width=3, command=lambda:[insertsymbol("log("), pressnumber(0), pressclosingBracket(0)])
intnaturalButton.place(relx=0.37, rely=0.78, anchor=CENTER)

intlogButton = Button(intMenu, text="log", width=3, command=lambda:[insertsymbol("log(,"), pressnumber(0), pressclosingBracket(0)])
intlogButton.place(relx=0.395, rely=0.78, anchor=CENTER)

intdeleteButton = Button(intMenu, text="←", width=10, bg="#fee0e0", activebackground="#fee0e0", command=lambda:[deletesymbol(), pressnumber(0), pressclosingBracket(0)])
intdeleteButton.place(relx=0.654, rely=0.66, anchor=CENTER)

intsinButton = Button(intMenu, text="sin", width=4, command=lambda:[insertsymbol("sin("), pressnumber(0), pressclosingBracket(0)])
intsinButton.place(relx=0.61, rely=0.7, anchor=CENTER)

intcosButton = Button(intMenu, text="cos", width=4, command=lambda:[insertsymbol("cos("), pressnumber(0), pressclosingBracket(0)])
intcosButton.place(relx=0.64, rely=0.7, anchor=CENTER)

inttanButton = Button(intMenu, text="tan", width=4, command=lambda:[insertsymbol("tan("), pressnumber(0), pressclosingBracket(0)])
inttanButton.place(relx=0.67, rely=0.7, anchor=CENTER)

intasinButton = Button(intMenu, text="arcsin", width=4, command=lambda:[insertsymbol("asin("), pressnumber(0), pressclosingBracket(0)])
intasinButton.place(relx=0.61, rely=0.74, anchor=CENTER)

intacosButton = Button(intMenu, text="arccos", width=4, command=lambda:[insertsymbol("acos("), pressnumber(0), pressclosingBracket(0)])
intacosButton.place(relx=0.64, rely=0.74, anchor=CENTER)

intatanButton = Button(intMenu, text="arctan", width=4, command=lambda:[insertsymbol("atan("), pressnumber(0), pressclosingBracket(0)])
intatanButton.place(relx=0.67, rely=0.74, anchor=CENTER)

intsinhButton = Button(intMenu, text="sinh", width=4, command=lambda:[insertsymbol("sinh("), pressnumber(0), pressclosingBracket(0)])
intsinhButton.place(relx=0.61, rely=0.78, anchor=CENTER)

intcoshButton = Button(intMenu, text="cosh", width=4, command=lambda:[insertsymbol("cosh("), pressnumber(0), pressclosingBracket(0)])
intcoshButton.place(relx=0.64, rely=0.78, anchor=CENTER)

inttanhButton = Button(intMenu, text="tanh", width=4, command=lambda:[insertsymbol("tanh("), pressnumber(0), pressclosingBracket(0)])
inttanhButton.place(relx=0.67, rely=0.78, anchor=CENTER)

intasinhButton = Button(intMenu, text="arsinh", width=4, command=lambda:[insertsymbol("asinh("), pressnumber(0), pressclosingBracket(0)])
intasinhButton.place(relx=0.61, rely=0.82, anchor=CENTER)

intacoshButton = Button(intMenu, text="arcosh", width=4, command=lambda:[insertsymbol("acosh("), pressnumber(0), pressclosingBracket(0)])
intacoshButton.place(relx=0.64, rely=0.82, anchor=CENTER)

intatanhButton = Button(intMenu, text="artanh", width=4, command=lambda:[insertsymbol("atanh("), pressnumber(0), pressclosingBracket(0)])
intatanhButton.place(relx=0.67, rely=0.82, anchor=CENTER)

mainMenu()
root.mainloop()
