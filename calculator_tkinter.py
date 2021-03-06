import tkinter

window = tkinter.Tk()

window.title("Calculator Ku")
window.geometry('400x300')

masukin = tkinter.Entry(window, width=60, borderwidth=5)
masukin.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def myClick(number):
    current = masukin.get()
    masukin.delete(0, tkinter.END)
    masukin.insert(0, str(current) + str(number))
    
    def button_clear():
    masukin.delete(0, tkinter.END)

def button_add():
    first_number = masukin.get()
    global f_num2
    global kali
    kali = "add"
    f_num2 = int(first_number)
    masukin.delete(0, tkinter.END)
    
    
def button_sum():
    jumlah = masukin.get()
    masukin.delete(0, tkinter.END)
    
    if kali == "add" :
        masukin.insert(0, int(f_num2) + int(jumlah))
    if kali == "mult" :
        masukin.insert(0, int(f_num2) * int(jumlah))
    if kali == "div" :
        masukin.insert(0, int(f_num2) / int(jumlah))
    if kali == "subs" :
        masukin.insert(0, int(f_num2) - int(jumlah))
        
    
    

def button_multiply():
    first_number2 = masukin.get()
    global f_num2
    global kali
    kali = "mult"
    f_num2 = int(first_number2)
    masukin.delete(0, tkinter.END)

def button_divide():
    first_number2 = masukin.get()
    global f_num2
    global kali
    kali = "div"
    f_num2 = int(first_number2)
    masukin.delete(0, tkinter.END)

def button_substract():
    first_number2 = masukin.get()
    global f_num2
    global kali
    kali = "subs"
    f_num2 = int(first_number2)
    masukin.delete(0, tkinter.END)

mybutton1 = tkinter.Button(window, text = "1"
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10, command= lambda: myClick(1))
mybutton1.grid(row=1, column=0)
mybutton2 = tkinter.Button(window, text = "2", command= lambda: myClick(2)
                          , fg="Blue", bg="Yellow", padx=37, pady=10)
mybutton2.grid(row=1, column=1)
mybutton3 = tkinter.Button(window, text = "3", command=lambda: myClick(3)
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybutton3.grid(row=1, column=2)
mybutton4 = tkinter.Button(window, text = "4", command=lambda: myClick(4)
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybutton4.grid(row=2, column=0)
mybutton5 = tkinter.Button(window, text = "5", command=lambda: myClick(5)
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybutton5.grid(row=2, column=1)
mybutton6 = tkinter.Button(window, text = "6", command=lambda: myClick(6)
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybutton6.grid(row=2, column=2)
mybutton7 = tkinter.Button(window, text = "7", command=lambda: myClick(7)
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybutton7.grid(row=3, column=0)
mybutton8 = tkinter.Button(window, text = "8", command=lambda: myClick(8)
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybutton8.grid(row=3, column=1)
mybutton9 = tkinter.Button(window, text = "9", command=lambda: myClick(9)
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybutton9.grid(row=3, column=2)
mybutton0 = tkinter.Button(window, text = "0", command=lambda: myClick(0)
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybutton0.grid(row=3, column=3)

mybuttonAdd = tkinter.Button(window, text = "+", command=lambda: myClick(1)
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybuttonAdd.grid(row=2, column=3)

mybuttonSum = tkinter.Button(window, text = "=", command=lambda: myClick(1)
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybuttonSum.grid(row=1, column=3)
mybuttonClear = tkinter.Button(window, text = "Clear", command=lambda: myClick(1)
                          , fg="Blue", bg="Yellow", padx= 173, pady= 10)
mybuttonClear.grid(row=4, column=0, columnspan=4)
mybuttonMultiply = tkinter.Button(window, text = "x", command=lambda: button_multiply()
                          , fg="Blue", bg="Yellow", padx= 36, pady= 10)
mybuttonMultiply.grid(row=4, column=0)

mybuttonDivide = tkinter.Button(window, text = "/", command=lambda: button_divide()
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybuttonDivide.grid(row=4, column=1)

mybuttonSubstract = tkinter.Button(window, text = "-", command=lambda: button_substract()
                          , fg="Blue", bg="Yellow", padx= 37, pady= 10)
mybuttonSubstract.grid(row=1, column=3)

window.mainloop()
