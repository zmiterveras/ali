 #!/usr/bin/env python3
#Ali_mod_v3.py
from tkinter import *
from tkinter.messagebox import showwarning, showinfo
import os, sys

#4,11,16,21,27,30,32,35,37,40
mes_r = ['Выбор языка', 'Выберите язык приложения', 'Имя корзины', 'Нет таможне', 'Пусто',
         'Создать','Просмотр', 'Редактировать', 'Удалить', 'Выход', 'Введите имя корзины:','OK',
         'Отмена', 'Предупреждение', 'Не введено имя', 'Информация', 'Создана корзина:',
         'Корзина пуста', 'Покупка', 'Цена','Сумма:', 'Выбранная корзина не существует',
         'Закрыть', 'Получено', 'Добавить', 'Изменить', 'Удалить', 'Не введено имя покупки',
         'Отметить', 'Не введена стоимость покупки','Стоимось покупки должна быть числом: "2 или 2.3"',
         'Превышена сумма таможенного лимита', 'Не выбрана покупка',
         'Невозможно одновременное изменение нескольких покупок', 'Помощь', 'О программе',
         'Если вы не используете LibereOffice, откройте файл Manual.doc сами;)', ': ',
         '"Нет таможне" ver.3 - создана чтобы помочь избежать таможенных платежей\n\n', 'Автор', 'zmv\n\n',
         'Обратная связь', 'zmiter_v@tut.by\n\n', 'Донаты', 'WebMoney(WMZ) Z087613107605']
mes_e = ['Choice of language', 'Choose application language', 'Name of Basket','No customs',
         'Empty', 'Create','View', 'Edit', 'Delete', 'Quit', 'Enter Name of Basket:', 'OK',
         'Cancel', 'Warning',"The Name isn't entered", 'Info', 'Create the Basket:',
         'Basket is empty','Purchase','Price', 'Sum:', "Choosed basket don't exist", 'Close',
         'Recieved', 'Add', 'Change', 'Delete', "Don't entred name of purchase", 'Mark',
         "Don't entred price of purchase",'Price of purchase must be figure: "2 or 2.3"',
         'The sum of a customs limit is exceeded', "Purchase isn't chosen",
         'Simultaneous change of several purchases is impossible', 'Help', 'About',
         "If you don't use LibereOffice, open file Manual.doc yourself;)", ': ',
         '"No customs" ver.3 is created to help to avoid customs payments\n\n', 'Creator', 'zmv\n\n',
         'Link', 'zmiter_v@tut.by\n\n', 'Donate', 'WebMoney(WMZ) Z087613107605']

#################################################################################
def LbInsert(db, mes, lb):
    lb.delete(0, END)
    if len(db) == 0:
        for i in range(4):
            lb.insert(i, mes[4])
    else:
        k = 0
        for (i, name) in enumerate(list(db.keys())):
            lb.insert(i, name)
            k += 1
        while k <= 3:
            lb.insert(k, mes[4])
            k += 1
################################################################################

def onCreate(mes, db_dict, lb):
    def getName():
        value = ent.get()
        if value == '':
            showwarning(mes[13], mes[14])
        else:
            showinfo(mes[15], mes[16] + value)
            db_dict[value] = []
            LbInsert(db_dict, mes, lb)
            cr_win.destroy()
            
            
    cr_win = Tk()
    cr_win.title(mes[5])
    cr_win.geometry('+250+250')
    Label(cr_win, text=mes[10]).pack()
    Frame(cr_win, height=5).pack()
    ent = Entry(cr_win, width=10, bd=2)
    ent.pack()
    Frame(cr_win, height=5).pack()
    Button(cr_win, text=mes[11], bd=2, command=getName).pack(side=LEFT)
    Button(cr_win, text=mes[12], bd=2, command=cr_win.destroy).pack(side=RIGHT)
    #cr_win.focus_set()
    #cr_win.grab_set()
    #cr_win.wait_window()
################################################################################
  
def onView(mes, db_dict, lb):
    def fullbasket():
        k = len(bas)
        y = 45
        Ym = 40 + (k*25)
        canv = Canvas(frm, width=330, bg='lightblue')
        canv.pack(expand=YES, fill=BOTH, side=LEFT)
        sb = Scrollbar(frm)
        sb.pack(side=RIGHT, fill=Y)
        sb.config(command=canv.yview)
        canv.config(yscrollcommand=sb.set)
        canv.config(scrollregion=(0,0,330,Ym))
        lab1 = Label(canv, text=mes[18], bg='lightblue')
        lab1.pack()
        canv.create_window(20, 20, anchor=W, window=lab1)
        lab2 = Label(canv, text=mes[19], bg='lightblue')
        lab2.pack()
        canv.create_window(275,20, anchor=W, window=lab2)
        summ = 0
        for i in range(k):
            ent1 = Entry(canv,width=30, relief=RIDGE, bg='white')
            ent1.pack()
            ent1.insert(0, bas[i][0])
            canv.create_window(20, y,anchor=W, window=ent1)
            ent2 = Entry(canv, width=5, relief=RIDGE, bg='white')
            ent2.pack()
            ent2.insert(0, bas[i][1])
            canv.create_window(275, y, anchor=W, window=ent2)
            if bas[i][2] != None:
                ent1.config(foreground='green')
                ent2.config(foreground='green')
            summ += float(bas[i][1])
            y += 25
        lab3 = Label(canv, text=mes[20],bg='lightblue')
        lab3.pack()
        canv.create_window(20,y, anchor=W, window=lab3)
        ent3 = Entry(canv, width=5, relief=RIDGE, bg='white')
        ent3.pack()
        ent3.insert(0, summ)
        canv.create_window(275, y, anchor=W, window=ent3)
        y += 25
        if summ > 22.0:
            ent3.config(foreground='red')
            lab3.config(foreground='red')
            lab4 = Label(canv, text=mes[31],bg='lightblue', fg='red')
            lab4.pack()
            canv.create_window(50,y, anchor=W, window=lab4)
            
    b_name = lb.get(ACTIVE)
    #print(b_name)
    if b_name not in db_dict:
        showwarning(mes[13], mes[21])
    else:
        bas = db_dict[b_name]
        if len(bas) == 0:
            showinfo(mes[15], mes[17])
        else:
            v_win = Toplevel()
            v_win.title(mes[6] +': ' + b_name)
            v_win.geometry('+250+250')
            frm = Frame(v_win)
            frm.pack(expand=YES, fill=BOTH)
            fullbasket()
            Button(v_win, text=mes[22], bd=2, command=v_win.destroy).pack()
################################################################################
   
def onEdit(mes, db_dict, lb, month):
    
    def fullbasket():
        nonlocal var_s
        k = len(bas)
        if k == 0:
            #showinfo(mes[15],mes[17])
            l_e = Label(frm, text = mes[17])
            l_e.pack()
        else:
            y = 45
            Ym = 40 + (k*25)
            canv = Canvas(frm, width=380, bg='lightblue')
            canv.pack(expand=YES, fill=BOTH, side=LEFT)
            sb = Scrollbar(frm)
            sb.pack(side=RIGHT, fill=Y)
            sb.config(command=canv.yview)
            canv.config(yscrollcommand=sb.set)
            canv.config(scrollregion=(0,0,380,Ym))
            var_s = []
            lab1 = Label(canv, text=mes[18], bg='lightblue')
            lab1.pack()
            canv.create_window(20, 20, anchor=W, window=lab1)
            lab2 = Label(canv, text=mes[19], bg='lightblue')
            lab2.pack()
            canv.create_window(275,20, anchor=W, window=lab2)
            summ = 0
            for i in range(k):
                var = IntVar()
                ent1 = Entry(canv,width=30, relief=RIDGE, bg='white')
                ent1.pack()
                ent1.insert(0, bas[i][0])
                canv.create_window(20, y,anchor=W, window=ent1)
                ent2 = Entry(canv, width=5, relief=RIDGE, bg='white')
                ent2.pack()
                ent2.insert(0, bas[i][1])
                canv.create_window(275, y, anchor=W, window=ent2)
                chb = Checkbutton(canv, variable=var, onvalue=1, offvalue=0,
                                  command=onClick)
                chb.pack()
                canv.create_window(330, y, anchor=W, window=chb)
                if bas[i][2] != None:
                    ent1.config(foreground='green')
                    ent2.config(foreground='green')
                summ += float(bas[i][1])
                y += 25
                var_s.append(var)
            lab3 = Label(canv, text=mes[20],bg='lightblue')
            lab3.pack()
            canv.create_window(20,y, anchor=W, window=lab3)
            ent3 = Entry(canv, width=5, relief=RIDGE, bg='white')
            ent3.pack()
            ent3.insert(0, summ)
            canv.create_window(275, y, anchor=W, window=ent3)
            y += 25
            if summ > 22.0:
                ent3.config(foreground='red')
                lab3.config(foreground='red')
                lab4 = Label(canv, text=mes[31],bg='lightblue', fg='red')
                lab4.pack()
                canv.create_window(50,y, anchor=W, window=lab4)
                                     
                
                
    def onClick():
        l=[]
        for i in var_s:
            k = i.get()
            l.append(k)
        #print(l)
        return l

    
    
    def onAdd(new=('',''), mes_add=mes[24]):
        def onFetch():
            Pur = ent1.get()
            Pr = ent2.get()
            if Pur == '':
                showwarning(mes[13], mes[27])
            elif Pr == '':
                showwarning(mes[13], mes[29])
            else:
                try:
                    float(Pr)
                except ValueError:
                    showwarning(mes[13], mes[30])
                else:
                    new = (Pur, float(Pr), None)
                    bas.append(new)
                    clear()
                    fullbasket()
                    add_win.destroy()
                    
        def add_win_close():
            if new != ('',''):
                bas.append(new)
                clear()
                fullbasket()
            add_win.destroy()
                

        add_win = Toplevel(ed_win)
        add_win.title(mes_add)
        add_win.geometry('+300+300')
        Label(add_win, text=mes[18]).grid(row=0, column=0)
        Label(add_win, text=mes[19]).grid(row=0, column=1)
        ent1 = Entry(add_win, bd=2, width=20)
        ent1.grid(row=1, column=0)
        ent1.insert(0, new[0])
        ent2 = Entry(add_win, bd=2, width=5)
        ent2.grid(row=1, column=1)
        ent2.insert(0, new[1])
        Button(add_win, text=mes[11], bd=2, command=lambda: onFetch()).grid(row=2, column=0)
        Button(add_win, text=mes[12], bd=2, command=lambda:add_win_close()).grid(row=2,  column=1)
        #add_win.focus_set()
        #add_win.grab_set()
        #add_win.wait_window()
                
    def onClose():
        db_dict[b_name] = bas
        ed_win.destroy()
        
    def onChange():
        st = onClick()
        fig = st.count(1)
        if fig == 0:
            showwarning(mes[13], mes[32])
        elif fig > 1:
            showwarning(mes[13], mes[33])
        else:
            index = st.index(1)
            new = bas.pop(index)
            onAdd(new, mes[25])   
            
        
    def onDelete():
        st = onClick()
        fig = st.count(1)
        if fig == 0:
            showwarning(mes[13], mes[32])
        elif fig > 1:
            showwarning(mes[13], mes[33])
        else:
            index = st.index(1)
            bas.pop(index)
            clear()
            fullbasket()
    
    def onRecieve():
        st = onClick()
        fig = st.count(1)
        if fig == 0:
            showwarning(mes[13], mes[32])
        elif fig > 1:
            showwarning(mes[13], mes[33])
        else:
            index = st.index(1)
            new = bas.pop(index)
            new = (new[0],) + (new[1],) + (str(month),)
            bas.append(new)
            clear()
            fullbasket()

    
    def clear():
        lis_del = frm.pack_slaves()
        for l in lis_del:
            l.destroy()
    
    b_name = lb.get(ACTIVE)
    var_s = []
    if b_name not in db_dict:
        showwarning(mes[13], mes[21])
    else:
        bas = db_dict[b_name]
        ed_win = Toplevel()
        ed_win.title(mes[7] +': ' + b_name)
        ed_win.geometry('+250+250')
        frm = Frame(ed_win)
        frm.pack(expand=YES, fill=BOTH)
        fullbasket()
        frb = Frame(ed_win)
        frb.pack(expand=YES, fill=X)
        btns = [(mes[24], onAdd), (mes[25], onChange), (mes[26], onDelete), (mes[23], onRecieve)]
        for i,j in btns:
            Button(frb, text=i, bd=2, command=j).pack(side=LEFT, expand=YES, fill=X)
        Button(ed_win, text=mes[22], bd=2, command=onClose).pack()
        
def onDelete(mes, db_dict, lb, delname):
    b_name = lb.get(ACTIVE)
    if b_name not in db_dict:
        showwarning(mes[13], mes[21])
    else:
        delname.append(b_name)
        db_dict.pop(b_name)
        LbInsert(db_dict, mes, lb)
        
def hl_show(mes):
    if sys.platform[:3] == 'win':
        os.startfile('Manual.doc')
    else:
        try:
            os.system('libreoffice --writer Manual.doc')
        except:
            showwarrning(mes[13], mes[36])
        

def about_me(mes):
    mess = mes[35] + mes[37] + mes[38] + mes[39] + mes[37] + mes[40] + mes [41] + mes[37] + mes[42] + mes[43] + mes [37] + mes[44]
    showinfo(mes[35], mess)
        
    
    
        
    
    
    
        
    
        
    
        



