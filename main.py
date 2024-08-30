from tkinter import *
from tkinter import ttk

color1 = '#1c1c1c'
color2 = '#ffffff'
color3 = '#ad788f'
color4 = '#ffb0d2'
color5 = '#ad788f'

#window

window = Tk()
window.title('Calculator ♡')
window.geometry('235x310')
window.config(bg=color1)

frame_tela = Frame(window, width=235, height=50, bg=color3)
frame_tela.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=310)
frame_body.grid(row=1, column=0)

#var all_valores

all_valores = ''

#label

valor_text = StringVar()

#function

def input_valores(event):
    global all_valores
    all_valores = all_valores + str(event)
    valor_text.set(all_valores) 
    
#math

def calcular():
    global all_valores 
    result = eval(all_valores)
    
    valor_text.set(str(result))
 
#clear window

def clear(): 
    global all_valores
    all_valores = ''
    valor_text.set('')

app_label = Label(frame_tela, textvariable=valor_text, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg= color3, fg=color2)
app_label.place(x=0, y=0)

#buttons

b_1 = Button(frame_body, command = clear, text='Clear', width=11, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #column 1
b_1.place(x=0, y=0)
b_2 = Button(frame_body, command = lambda: input_valores('%'), text='%', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_body, command = lambda: input_valores('/'), text='/', width=5, height=2, bg= color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_3.place(x=177, y=0)

b_4 = Button(frame_body, command = lambda: input_valores('7'), text='7', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #column 2
b_4.place(x=0, y=52)
b_5 = Button(frame_body, command = lambda: input_valores('8'), text='8', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_body, command = lambda: input_valores('9'), text='9', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_body, command = lambda: input_valores('*'), text='*', width=5, height=2, bg= color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_7.place(x=177, y=52)

b_8 = Button(frame_body, command = lambda: input_valores('4'), text='4', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #column 3
b_8.place(x=0, y=104)
b_9 = Button(frame_body, command = lambda: input_valores('5'), text='5', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_body, command = lambda: input_valores('6'), text='6', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_body, command = lambda: input_valores('-'), text='-', width=5, height=2, bg= color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_11.place(x=177, y=104)


b_12 = Button(frame_body, command = lambda: input_valores('1'), text='1', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #column 4
b_12.place(x=0, y=156)
b_13 = Button(frame_body, command = lambda: input_valores('2'), text='2', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_body, command = lambda: input_valores('3'), text='3', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_body, command = lambda: input_valores('+'), text='+', width=5, height=2, bg= color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_15.place(x=177, y=156)


b_16 = Button(frame_body, command = lambda: input_valores('0'), text='0', width=11, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #column 5
b_16.place(x=0, y=208)
b_17 = Button(frame_body, command = lambda: input_valores('.'), text='.', width=5, height=2, bg= color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_body, command = calcular, text='=', width=5, height=2, bg= color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_18.place(x=177, y=208)

window.mainloop()