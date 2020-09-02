#!/usr/bin/env python3
from tkinter import *
import shelve, os, Ali_mod_v3, sys, time

#####выбор языка###################################
def langChoose(langlist):
    ch_lang = Tk()
    ch_lang.title(mes[0])
    ch_lang.geometry('+450+250')
    chf1 = Frame(ch_lang, bd=2)
    chf1.pack()
    Label(chf1, text=mes[1]).pack()
    chf2 = Frame(ch_lang, bd=2)
    chf2.pack()
    if langlist[0] == 'rus':
        imagelist = ['ru.gif', 'gb.gif']
    else:
        imagelist = ['gb.gif', 'ru.gif']
    lang = StringVar()
    i = 0
    savephotos = []
    for image in imagelist:
        img = PhotoImage(file=image)
        Radiobutton(chf2, image=img, variable=lang, value=langlist[i]).pack(side=LEFT)
        i += 1
        savephotos.append(img)
    lang.set(langlist[0])
    Button(ch_lang, text='OK', bd=2, command=ch_lang.destroy).pack()
    ch_lang.focus_set()
    ch_lang.grab_set()
    ch_lang.wait_window()
    lg = lang.get()
    ch_lang.mainloop()
    return lg

def chooseMessage(lang):
    if lang == 'rus':
        mes = Ali_mod_v3.mes_r
    else:
        mes = Ali_mod_v3.mes_e
    return mes
######################################################
    
def _quit():
    """
    выход, с предварительной перезаписью ДБ,
    с учетом удаленных позиций
    """
    #print('Exit:',db_dict)
    db = shelve.open(dbname)
    if len(delname) != 0:
        for key in delname:
            db.pop(key)
    db['language'] = langlist
    for key in db_dict:
        db[key] = db_dict[key]
    db.close()
    sys.exit()


        
def updateDB():
    """
    обновление ДБ, с удалением позиций,
    отмеченных как полученные
    """
    for key in db_dict:
        basket = db_dict[key]
        j = 0
        for i in basket:
            #print(i, i[2])
            if i[2] != None:
                if month != int(i[2]):
                    basket.pop(j)
            j += 1
            
#####создание строки меню#####################################
def makemenu(win):
    top = Menu(win)
    win.config(menu=top)
    hl = Menu(top, tearoff=False)
    hl.add_command(label = mes[34], command=lambda:hl_show(mes))
    top.add_cascade(label=mes[34], menu=hl)
    about = Menu(top, tearoff=False)
    about.add_command(label=mes[35], command=lambda:about_me(mes))
    top.add_cascade(label=mes[35], menu=about)
    
######создание или открытие БД###################################
db_dict = {}
pl = sys.platform
dbname = 'AliDB'
if pl[:3] == 'win':
    checkname = dbname + '.dat'
else:
    checkname = dbname
    
if not os.path.exists(checkname):
    db = shelve.open(dbname)
    language = ['rus', 'eng']
    db['language'] = language
    db_dict['language'] = language
else:
    db = shelve.open(dbname)
    for key in db:
        db_dict[key] = db[key]
db.close()

# список удаленных корзин
delname = []

#получение текущей даты (месяца)
date = time.gmtime()
month = date.tm_mon

#выбор языка сеанса
langlist = db_dict['language']
lang = langlist[0]
db_dict.pop('language')
mes = chooseMessage(lang)
l_time = langChoose(langlist)
if l_time != lang:
    langlist[0], langlist[1] = langlist[1], langlist[0]
    lang = langlist[0]
    mes = chooseMessage(lang)

#обновление БД
updateDB()

######
LbInsert = Ali_mod_v3.LbInsert
onCreate = Ali_mod_v3.onCreate
onView = Ali_mod_v3.onView
onEdit = Ali_mod_v3.onEdit
onDelete = Ali_mod_v3.onDelete
hl_show = Ali_mod_v3.hl_show
about_me = Ali_mod_v3.about_me
######

root = Tk()
root.title(mes[3])
root.geometry('+150+150')
makemenu(root)
Label(root, text=mes[2]).pack()
fr1 = Frame(root)
fr1.pack(side=TOP, expand=YES, fill=BOTH)
lb = Listbox(fr1, selectmode=SINGLE, height=4, bd=2, cursor='hand2')
sb = Scrollbar(fr1)
sb.config(command=lb.yview)
lb.config(yscrollcommand=sb.set)
sb.pack(side=RIGHT, fill=Y)
lb.pack(side=LEFT, expand=YES, fill=BOTH)
LbInsert(db_dict, mes, lb)
fr2 = Frame(root)
fr2.pack(side=TOP, fill=X)
Button(fr2, text=mes[5], bd=2, command=lambda: onCreate(mes, db_dict, lb)).pack(side=LEFT, fill=X)
Button(fr2, text=mes[6], bd=2, command=lambda: onView(mes, db_dict, lb)).pack(side=LEFT, fill=X)
Button(fr2, text=mes[7], bd=2, command=lambda: onEdit(mes, db_dict, lb, month)).pack(side=LEFT, fill=X)
Button(fr2, text=mes[8], bd=2, command=lambda: onDelete(mes, db_dict, lb, delname)).pack(side=LEFT, fill=X)
Button(root, text=mes[9], bd=2, command=_quit).pack()
root.mainloop()


    
    
