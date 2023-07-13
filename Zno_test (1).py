from asyncio import open_connection
import math
from tkinter import *
from random import *
from tkinter import messagebox as mbox
from turtle import title

from setuptools import Command


class ZNO(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.master.title("ZNO test")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()
        lb = Label(self, text='Welcome to ZNO test')
        lb.place(x=20, y=30)
        btt = Button(self, text='Chose subject', command=self.selct)
        btt.place(x=20, y=50)


    def selct(self):
        self.test = Toplevel()
        self.test.title('chose your subject')
        btm = Button(self.test, text='math', command=self.mathe)
        btm.place(x=20, y=30)
        btu = Button(self.test, text='ukrainian', command=self.ukrainian)
        btu.place(x=20, y=60)
        btp = Button(self.test, text='physick', command=self.phusick)
        btp.place(x=20, y=90)
        btg = Button(self.test, text='geographe', command=self.geography)
        btg.place(x=20, y=120)
        btcl = Button(self.test, text='close', command=self.test.destroy)
        btcl.place(x=20, y=150)

    def mathe(self):
        self.mathe = Toplevel()
        self.mathe.title('math')
        frm_form = Frame(self.mathe, relief=SUNKEN, borderwidth=3)
        frm_form.pack()
        labels = [
            "Имя:",
            "Фамилия:",
            "Адрес 1:",
            "Адрес 2:",
            "Город:",
            "Регион:",
            "Почтовый индекс:",
            "Страна:",
        ]
        
      
        frm_form = Frame(self.mathe, relief=SUNKEN, borderwidth=3)

        frm_form.pack()

        lbl_first_name = Label(frm_form, text="f(x)=12+x^2 y`=")
        ent1 = Entry(frm_form, width=50)

        lbl_first_name.grid(row=0, column=0, sticky="e")
        ent1.grid(row=0, column=1)

        lbl_last_name = Label(frm_form, text='У коли было два яблока одно он дал другу.\nСколько у коли яблок')
        ent2 = Entry(frm_form, width=50)

        lbl_last_name.grid(row=1, column=0, sticky="e")
        ent2.grid(row=1, column=1)
 

        lbl_address1 = Label(frm_form, text='Два трактора пахали поле у\nБогданаю За сколько они вспахают квадратное поле размером 100км^2 \nесли одну часть поля плуги шириной 2 м за 0.5 часа?')
        ent3 = Entry(frm_form, width=50)

        lbl_address1.grid(row=2, column=0, sticky="e")
        ent3.grid(row=2, column=1)
 

        lbl_address2 = Label(frm_form, text='решить уровнение (x^2+3x-10)/(x+5)=0')
        ent4 = Entry(frm_form, width=50)

        lbl_address2.grid(row=3, column=0, sticky=E)
        ent4.grid(row=3, column=1)
 

        lbl_city = Label(frm_form, text='У куб, ребро якого 6 см,\nвписано кулю. Обчисліть поверхню кулі. число пи не учитывать')
        ent5 = Entry(frm_form, width=50)

        lbl_city.grid(row=4, column=0, sticky=E)
        ent5.grid(row=4, column=1)
 

        lbl_state = Label(frm_form, text='Знайти длину меньшего катета если гипотенуза=5,\nа угол против меньшего катета равен 35 градусам')
        ent6 = Entry(frm_form, width=50)

        lbl_state.grid(row=5, column=0, sticky=E)
        ent6.grid(row=5, column=1)
 

        lbl_postal_code = Label(frm_form, text='(x+2)(x+4)(x+6)(x+8)=0 \n найти их сумму')
        ent7 = Entry(frm_form, width=50)

        lbl_postal_code.grid(row=6, column=0, sticky=E)
        ent7.grid(row=6, column=1)

        lbl_country = Label(frm_form, text='x+y=12\nx-3y=4 \n найти их сумму')
        ent8 = Entry(frm_form, width=50)

        lbl_country.grid(row=7, column=0, sticky=E)
        ent8.grid(row=7, column=1)
        
        frm_buttons = Frame(self.mathe)
        frm_buttons.pack(fill=X, ipadx=5, ipady=5)


        def gedree():
            a = str(ent1.get())
            b = int(ent2.get())
            c = int(ent3.get())
            d = int(ent4.get())
            e = int(ent5.get())
            f = int(ent6.get())
            g = int(ent7.get())
            h = int(ent8.get())

            l = [a, b, c, d, e, f, g, h]
            ans =['2x', 1, 10, 2, 36, 3, -20, 12]


            res = [x for x in l if x not in l or x not in ans]

            print(res, len(res))
            mark = 200 - (25 * len(res))


            if not res and mark == 200:
                mbox.showinfo('Mark', 'Your pass. Your mark: 200')
            elif 100 < mark < 200:
                mbox.showinfo('Mark', f'Your pass. Your mark: {mark}')
            else:
                mbox.showinfo('Mark', f'Your don`t pass. Your marl:{mark}')
            
                

        btn_submit = Button(frm_buttons, text="Submit", command=gedree)
        btn_submit.grid()
        btn_submit.pack(side=RIGHT, padx=10, ipadx=10)
    
        btn_clear = Button(frm_buttons, text="Clear")
        btn_clear.pack(side=RIGHT, ipadx=10)


    def ukrainian(self):
        self.ukrainian = Toplevel()
        self.ukrainian.title('ukrainian')
        frm_form = Frame(self.ukrainian, relief=SUNKEN, borderwidth=3)
        frm_form.pack()
        labels = [
            "Имя:",
            "Фамилия:",
            "Адрес 1:",
            "Адрес 2:",
            "Город:",
            "Регион:",
            "Почтовый индекс:",
            "Страна:",
        ]
        
      
        frm_form = Frame(self.ukrainian, relief=SUNKEN, borderwidth=3)

        frm_form.pack()

        lbl_first_name = Label(frm_form, text="f(x)=12+x^2 y`=")
        ent1 = Entry(frm_form, width=50)

        lbl_first_name.grid(row=0, column=0, sticky="e")
        ent1.grid(row=0, column=1)

        lbl_last_name = Label(frm_form, text='У коли было два яблока одно он дал другу.\nСколько у коли яблок')
        ent2 = Entry(frm_form, width=50)

        lbl_last_name.grid(row=1, column=0, sticky="e")
        ent2.grid(row=1, column=1)
 

        lbl_address1 = Label(frm_form, text='Два трактора пахали поле у\nБогданаю За сколько они вспахают квадратное поле размером 100км^2 \nесли одну часть поля плуги шириной 2 м за 0.5 часа?')
        ent3 = Entry(frm_form, width=50)

        lbl_address1.grid(row=2, column=0, sticky="e")
        ent3.grid(row=2, column=1)
 

        lbl_address2 = Label(frm_form, text='решить уровнение (x^2+3x-10)/(x+5)=0')
        ent4 = Entry(frm_form, width=50)

        lbl_address2.grid(row=3, column=0, sticky=E)
        ent4.grid(row=3, column=1)
 

        lbl_city = Label(frm_form, text='У куб, ребро якого 6 см,\nвписано кулю. Обчисліть поверхню кулі. число пи не учитывать')
        ent5 = Entry(frm_form, width=50)

        lbl_city.grid(row=4, column=0, sticky=E)
        ent5.grid(row=4, column=1)
 

        lbl_state = Label(frm_form, text='Знайти длину меньшего катета если гипотенуза=5,\nа угол против меньшего катета равен 35 градусам')
        ent6 = Entry(frm_form, width=50)

        lbl_state.grid(row=5, column=0, sticky=E)
        ent6.grid(row=5, column=1)
 

        lbl_postal_code = Label(frm_form, text='(x+2)(x+4)(x+6)(x+8)=0 \n найти их сумму')
        ent7 = Entry(frm_form, width=50)

        lbl_postal_code.grid(row=6, column=0, sticky=E)
        ent7.grid(row=6, column=1)

        lbl_country = Label(frm_form, text='x+y=12\nx-3y=4 \n найти их сумму')
        ent8 = Entry(frm_form, width=50)

        lbl_country.grid(row=7, column=0, sticky=E)
        ent8.grid(row=7, column=1)
        
        frm_buttons = Frame(self.mathe)
        frm_buttons.pack(fill=X, ipadx=5, ipady=5)


        def gedree():
            a = str(ent1.get())
            b = int(ent2.get())
            c = int(ent3.get())
            d = int(ent4.get())
            e = int(ent5.get())
            f = int(ent6.get())
            g = int(ent7.get())
            h = int(ent8.get())

            l = [a, b, c, d, e, f, g, h]
            ans =['2x', 1, 10, 2, 36, 3, -20, 12]


            res = [x for x in l if x not in l or x not in ans]

            print(res, len(res))
            mark = 200 - (25 * len(res))


            if not res and mark == 200:
                mbox.showinfo('Mark', 'Your pass. Your mark: 200')
            elif 100 < mark < 200:
                mbox.showinfo('Mark', f'Your pass. Your mark: {mark}')
            else:
                mbox.showinfo('Mark', f'Your don`t pass. Your marl:{mark}')
            
                

        btn_submit = Button(frm_buttons, text="Submit", command=gedree)
        btn_submit.grid()
        btn_submit.pack(side=RIGHT, padx=10, ipadx=10)
    
        btn_clear = Button(frm_buttons, text="Clear")
        btn_clear.pack(side=RIGHT, ipadx=10)
   
    def phusick(self):
        self.phusick = Toplevel()
        self.phusick.title('phusick')
        frm_form = Frame(self.phusick, relief=SUNKEN, borderwidth=3)
        frm_form.pack()
        labels = [
            "Имя:",
            "Фамилия:",
            "Адрес 1:",
            "Адрес 2:",
            "Город:",
            "Регион:",
            "Почтовый индекс:",
            "Страна:",
        ]
        
      
        frm_form = Frame(self.phusick, relief=SUNKEN, borderwidth=3)

        frm_form.pack()

        lbl_first_name = Label(frm_form, text="f(x)=12+x^2 y`=")
        ent1 = Entry(frm_form, width=50)

        lbl_first_name.grid(row=0, column=0, sticky="e")
        ent1.grid(row=0, column=1)

        lbl_last_name = Label(frm_form, text='У коли было два яблока одно он дал другу.\nСколько у коли яблок')
        ent2 = Entry(frm_form, width=50)

        lbl_last_name.grid(row=1, column=0, sticky="e")
        ent2.grid(row=1, column=1)
 

        lbl_address1 = Label(frm_form, text='Два трактора пахали поле у\nБогданаю За сколько они вспахают квадратное поле размером 100км^2 \nесли одну часть поля плуги шириной 2 м за 0.5 часа?')
        ent3 = Entry(frm_form, width=50)

        lbl_address1.grid(row=2, column=0, sticky="e")
        ent3.grid(row=2, column=1)
 

        lbl_address2 = Label(frm_form, text='решить уровнение (x^2+3x-10)/(x+5)=0')
        ent4 = Entry(frm_form, width=50)

        lbl_address2.grid(row=3, column=0, sticky=E)
        ent4.grid(row=3, column=1)
 

        lbl_city = Label(frm_form, text='У куб, ребро якого 6 см,\nвписано кулю. Обчисліть поверхню кулі. число пи не учитывать')
        ent5 = Entry(frm_form, width=50)

        lbl_city.grid(row=4, column=0, sticky=E)
        ent5.grid(row=4, column=1)
 

        lbl_state = Label(frm_form, text='Знайти длину меньшего катета если гипотенуза=5,\nа угол против меньшего катета равен 35 градусам')
        ent6 = Entry(frm_form, width=50)

        lbl_state.grid(row=5, column=0, sticky=E)
        ent6.grid(row=5, column=1)
 

        lbl_postal_code = Label(frm_form, text='(x+2)(x+4)(x+6)(x+8)=0 \n найти их сумму')
        ent7 = Entry(frm_form, width=50)

        lbl_postal_code.grid(row=6, column=0, sticky=E)
        ent7.grid(row=6, column=1)

        lbl_country = Label(frm_form, text='x+y=12\nx-3y=4 \n найти их сумму')
        ent8 = Entry(frm_form, width=50)

        lbl_country.grid(row=7, column=0, sticky=E)
        ent8.grid(row=7, column=1)
        
        frm_buttons = Frame(self.mathe)
        frm_buttons.pack(fill=X, ipadx=5, ipady=5)


        def gedree():
            a = str(ent1.get())
            b = int(ent2.get())
            c = int(ent3.get())
            d = int(ent4.get())
            e = int(ent5.get())
            f = int(ent6.get())
            g = int(ent7.get())
            h = int(ent8.get())

            l = [a, b, c, d, e, f, g, h]
            ans =['2x', 1, 10, 2, 36, 3, -20, 12]


            res = [x for x in l if x not in l or x not in ans]

            print(res, len(res))
            mark = 200 - (25 * len(res))


            if not res and mark == 200:
                mbox.showinfo('Mark', 'Your pass. Your mark: 200')
            elif 100 < mark < 200:
                mbox.showinfo('Mark', f'Your pass. Your mark: {mark}')
            else:
                mbox.showinfo('Mark', f'Your don`t pass. Your marl:{mark}')
            
                

        btn_submit = Button(frm_buttons, text="Submit", command=gedree)
        btn_submit.grid()
        btn_submit.pack(side=RIGHT, padx=10, ipadx=10)
    
        btn_clear = Button(frm_buttons, text="Clear")
        btn_clear.pack(side=RIGHT, ipadx=10)

    def geography(self):
        self.geography = Toplevel()
        self.geography.title('geography')
        frm_form = Frame(self.geography, relief=SUNKEN, borderwidth=3)
        frm_form.pack()
        labels = [
            "Имя:",
            "Фамилия:",
            "Адрес 1:",
            "Адрес 2:",
            "Город:",
            "Регион:",
            "Почтовый индекс:",
            "Страна:",
        ]
        
      
        frm_form = Frame(self.geography, relief=SUNKEN, borderwidth=3)

        frm_form.pack()

        lbl_first_name = Label(frm_form, text="f(x)=12+x^2 y`=")
        ent1 = Entry(frm_form, width=50)

        lbl_first_name.grid(row=0, column=0, sticky="e")
        ent1.grid(row=0, column=1)

        lbl_last_name = Label(frm_form, text='У коли было два яблока одно он дал другу.\nСколько у коли яблок')
        ent2 = Entry(frm_form, width=50)

        lbl_last_name.grid(row=1, column=0, sticky="e")
        ent2.grid(row=1, column=1)
 

        lbl_address1 = Label(frm_form, text='Два трактора пахали поле у\nБогданаю За сколько они вспахают квадратное поле размером 100км^2 \nесли одну часть поля плуги шириной 2 м за 0.5 часа?')
        ent3 = Entry(frm_form, width=50)

        lbl_address1.grid(row=2, column=0, sticky="e")
        ent3.grid(row=2, column=1)
 

        lbl_address2 = Label(frm_form, text='решить уровнение (x^2+3x-10)/(x+5)=0')
        ent4 = Entry(frm_form, width=50)

        lbl_address2.grid(row=3, column=0, sticky=E)
        ent4.grid(row=3, column=1)
 

        lbl_city = Label(frm_form, text='У куб, ребро якого 6 см,\nвписано кулю. Обчисліть поверхню кулі. число пи не учитывать')
        ent5 = Entry(frm_form, width=50)

        lbl_city.grid(row=4, column=0, sticky=E)
        ent5.grid(row=4, column=1)
 

        lbl_state = Label(frm_form, text='Знайти длину меньшего катета если гипотенуза=5,\nа угол против меньшего катета равен 35 градусам')
        ent6 = Entry(frm_form, width=50)

        lbl_state.grid(row=5, column=0, sticky=E)
        ent6.grid(row=5, column=1)
 

        lbl_postal_code = Label(frm_form, text='(x+2)(x+4)(x+6)(x+8)=0 \n найти их сумму')
        ent7 = Entry(frm_form, width=50)

        lbl_postal_code.grid(row=6, column=0, sticky=E)
        ent7.grid(row=6, column=1)

        lbl_country = Label(frm_form, text='x+y=12\nx-3y=4 \n найти их сумму')
        ent8 = Entry(frm_form, width=50)

        lbl_country.grid(row=7, column=0, sticky=E)
        ent8.grid(row=7, column=1)
        
        frm_buttons = Frame(self.mathe)
        frm_buttons.pack(fill=X, ipadx=5, ipady=5)


        def gedree():
            a = str(ent1.get())
            b = int(ent2.get())
            c = int(ent3.get())
            d = int(ent4.get())
            e = int(ent5.get())
            f = int(ent6.get())
            g = int(ent7.get())
            h = int(ent8.get())

            l = [a, b, c, d, e, f, g, h]
            ans =['2x', 1, 10, 2, 36, 3, -20, 12]


            res = [x for x in l if x not in l or x not in ans]

            print(res, len(res))
            mark = 200 - (25 * len(res))


            if not res and mark == 200:
                mbox.showinfo('Mark', 'Your pass. Your mark: 200')
            elif 100 < mark < 200:
                mbox.showinfo('Mark', f'Your pass. Your mark: {mark}')
            else:
                mbox.showinfo('Mark', f'Your don`t pass. Your marl:{mark}')
            
                

        btn_submit = Button(frm_buttons, text="Submit", command=gedree)
        btn_submit.grid()
        btn_submit.pack(side=RIGHT, padx=10, ipadx=10)
    
        btn_clear = Button(frm_buttons, text="Clear")
        btn_clear.pack(side=RIGHT, ipadx=10)



def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = ZNO()
    root.mainloop()
 
 
if __name__ == '__main__':
    main()