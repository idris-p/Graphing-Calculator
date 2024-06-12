from tkinter import *
from sympy import *
from sympy.abc import x,y


root = Tk()
root.title("Calculus")
root.state('zoomed')

init_printing()
x=symbols('x') 

diffInput = Entry(root, width=30, font=('20'))
diffInput.place(relx=0.5, rely=0.5, anchor=CENTER)

expression = ""

def getDiffExpression():
    global expression
    expression = diffInput.get()
    deriv = diff(expression, x)

    lbl = Label(root, text=deriv)
    lbl.place(relx=0.5, rely=0.7, anchor=CENTER)
    

#img_lbl = Label(root)
#img_lbl.place(relx=0.5, rely=0.7, anchor=CENTER)

doneButton = Button(root, text="✓", command=lambda:[getDiffExpression()])
doneButton.place(relx=0.7, rely=0.5, anchor=CENTER)



root.mainloop()
