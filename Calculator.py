from tkinter import *

root_var = Tk()
root_var.title("Calculator")

e = Entry(root_var, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

f_num = opr = None

def button_click(number=None):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current+str(number))

def button_opr(op):
    global f_num, opr
    
    try:
        f_num = int(e.get())
        opr = op
        
        e.delete(0, END)
    except Exception as ex:
        print(ex)

def button_clear():
    global f_num, opr
    e.delete(0, END)
    
    f_num = opr = None

def button_equal():
    global f_num, opr
    if f_num and opr:
        try:
            current = int(e.get())
            e.delete(0, END)
            if opr == "+":
                e.insert(0, f_num+current)
            elif opr == "-":
                e.insert(0, f_num-current)
            elif opr == "*":
                e.insert(0, f_num*current)
            elif opr == "/":
                e.insert(0, f_num/current)
            elif opr == "^":
                e.insert(0, f_num**current)
        except Exception as ex:
            print(ex)
    # reset first number and operator
    f_num = opr = None

button_1 = Button(root_var, text="1", padx=50, pady=10, command=lambda: button_click(1))
button_2 = Button(root_var, text="2", padx=50, pady=10, command=lambda: button_click(2))
button_3 = Button(root_var, text="3", padx=50, pady=10, command=lambda: button_click(3))
button_4 = Button(root_var, text="4", padx=50, pady=10, command=lambda: button_click(4))
button_5 = Button(root_var, text="5", padx=50, pady=10, command=lambda: button_click(5))
button_6 = Button(root_var, text="6", padx=50, pady=10, command=lambda: button_click(6))
button_7 = Button(root_var, text="7", padx=50, pady=10, command=lambda: button_click(7))
button_8 = Button(root_var, text="8", padx=50, pady=10, command=lambda: button_click(8))
button_9 = Button(root_var, text="9", padx=50, pady=10, command=lambda: button_click(9))
button_0 = Button(root_var, text="0", padx=50, pady=10, command=lambda: button_click(0))

button_addition = Button(root_var, text="+", padx=50, pady=10, command=lambda: button_opr("+"))
button_subtraction = Button(root_var, text="-", padx=50, pady=10, command=lambda: button_opr("-"))
button_multiplication = Button(root_var, text="*", padx=50, pady=10, command=lambda: button_opr("*"))
button_division = Button(root_var, text="/", padx=50, pady=10, command=lambda: button_opr("/"))
button_exponents = Button(root_var, text="^", padx=50, pady=10, command=lambda: button_opr("^"))
button_equals = Button(root_var, text="=", padx=50, pady=10, command=button_equal)
button_clear = Button(root_var, text="C", padx=50, pady=10, command=button_clear)

button_1.grid(row=3, column=2, sticky="ew")
button_2.grid(row=3, column=1, sticky="ew")
button_3.grid(row=3, column=0, sticky="ew")
button_4.grid(row=2, column=2, sticky="ew")
button_5.grid(row=2, column=1, sticky="ew")
button_6.grid(row=2, column=0, sticky="ew")
button_7.grid(row=1, column=2, sticky="ew")
button_8.grid(row=1, column=1, sticky="ew")
button_9.grid(row=1, column=0, sticky="ew")
button_0.grid(row=4, column=0, sticky="ew")

button_addition.grid(row=4, column=1, sticky="ew")
button_subtraction.grid(row=4, column=2, sticky="ew")
button_multiplication.grid(row=5, column=0, sticky="ew")
button_division.grid(row=5, column=1, sticky="ew")
button_exponents.grid(row=5, column=2, sticky="ew")
button_equals.grid(row=6, column=0, sticky="ew")
button_clear.grid(row=6, column=1, sticky="ew")

root_var.mainloop()