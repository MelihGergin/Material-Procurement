import tkinter as m

def material1():
    a1 = float(20.70)
    num1 = int(s1.get())
    result['text'] = str(num1)
    price['text'] = float(a1*num1)

def material2():
    a2 = float(33.52)
    num1 = int(s1.get())
    result['text'] = str(num1)
    price['text'] = float(a2*num1)

def material3():
    a3 = float(150.25)
    num1 = int(s1.get())
    result['text'] = str(num1)
    price['text'] = float(a3*num1)

window = m.Tk()
window.title("Material Purchasing Application")
window.geometry("400x450+800+200")
window.configure(bg="gray")

head = m.Label(text="MATERIALS AND PRICES\n"
                      "1- M24X50 Hexagon Head Bolt 20.70 TL\n"
                      "2- M18X170 Hexagon Head Bolt 33.52 TL\n"
                      "3- 1000x2000 0.5mm 304 Steel Plate 150.25 TL", bg="yellow", font="arial 13 bold")
head.pack(side="top")

s1 = m.Entry(width=10)
s1.place(x=30, y=150)

result = m.Label(text="Amount:")
result.place(x=180, y=120)
result = m.Label(text="...")
result.place(x=245, y=120)

price = m.Label(text="Total price: ")
price.place(x=180, y=150)
price = m.Label(text="... ")
price.place(x=260, y=150)

button1 = m.Button(text="1", command=material1)
button1.place(x=100, y=120)
button2 = m.Button(text="2", command=material2)
button2.place(x=100, y=150)
button3 = m.Button(text="3", command=material3)
button3.place(x=100, y=180)

window.mainloop()
