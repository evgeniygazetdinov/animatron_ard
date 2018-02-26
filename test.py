import tkinter
from tkinter import ttk


def _Btn(param):
    print(param)


def main():
    hWin = tkinter.Tk()
    hWin.title(u'Моя программа')
    hWin.geometry('300x100+300+200')  # ширина=500, высота=400, x=300, y=200
    frameBtn = ttk.Frame(hWin)
    frameBtn.grid()
    frame = ttk.Frame(hWin)
    frame.grid()
    list1 = [u"Один", u"Два", u"Три"]
    # ссылка на описание параметров: https://docs.python.org/2/library/ttk.html#combobox
    combobox = ttk.Combobox(frame, values=list1, height=3, style='Kim.TButton', foreground='#FF0000', state='readonly')
    # combobox = Combobox(frame,values = list1,height=3)
    # frame - задает родительский виджет, на его территории будет располагаться Combobox
    # values - задает набор значений, которые будут содержаться в Combobox изначально
    # height - задает высоту выпадающего списка. Если число элементов списка меньше 11, то можно не задавать.
    # Если не задано при колличестве элементов больше 10, то с правой стороны появится полоса прокрутки.
    # Если в нашем примере задать значение height меньше трех, то с правой стороны появится полоса прокрутки,
    # но она будет недоступна, а все элементы будут отображаться одновременно.
    combobox.set(u"Один")  # Пункт по умолчанию
    combobox.grid(column=0, row=0)  # Позиционируем Combobox на форме (,sticky='s' здесь n, e, s, и/или w)

    # ~ combobox["<<ComboboxSelected>>"] = lambda: _Btn(combobox.get())

    # Привязка события при выборе
    def Get_Selected(param):
        print
        combobox.get()

    combobox.bind('<<ComboboxSelected>>', Get_Selected)
    button = tkinter.Button(frameBtn, text=u"-- Моя кнопка --")  # создаём кнопку
    button["command"] = lambda: _Btn(combobox.current())
    button.pack()
    hWin.mainloop()


if __name__ == '__main__':
    main()