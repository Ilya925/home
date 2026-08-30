from tkinter import Canvas, Frame, Menu, Label, Button
from tkinter import Entry, Tk, BOTH, X, BOTTOM, LEFT, ROUND, TOP

TOOLBAR_BG = '#f0f0f0'


class DrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Рисование')
        self.root.geometry('550x500')
        self.root.resizable(False, False)

        # Стартовые настройки
        self.color = 'red'
        self.line_width = 10
        self.last_x, self.last_y = None, None

        # Меню
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Очистить', accelerator='Ctrl+D', command=self.clear_canvas)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Выход', accelerator='Ctrl+Q', command=self.root.quit)
        self.menu_bar.add_cascade(label='Файл', menu=self.file_menu)
        self.root.config(menu=self.menu_bar)
        self.root.bind('<Control-Key-q>', lambda e: self.root.quit())
        self.root.bind('<Control-Key-d>', lambda e: self.clear_canvas())
        # Холст
        self.canvas = Canvas(self.root, bg='white')
        self.canvas.pack(fill=BOTH, expand=True)

        # Панель инструментов отдельным фреймом
        self.toolbar = Frame(self.root, bg=TOOLBAR_BG, height=40)
        self.toolbar.pack(fill=X, side=TOP)

        # Палитра цветов
        self.colors = ['red', 'green', 'blue', 'black']
        for color in self.colors:
            btn = Frame(self.toolbar, bg=color, width=40, height=30, cursor='hand2')
            btn.pack(side=LEFT, padx=2, pady=5)
            btn.bind('<Button-1>', lambda event, c=color: self.set_color(c))

        # Поле ввода толщины и кнопка для подтверждения
        self.label_width = Label(self.toolbar, text='Укажите толщину: ', font=('Arial', 12))
        self.label_width.pack(side=LEFT, padx=(20, 5))

        self.width_entry = Entry(self.toolbar, width=5)
        self.width_entry.insert(0, str(self.line_width))
        self.width_entry.pack(side=LEFT, padx=5)

        self.btn_set_width = Button(self.toolbar,
                                    text='Установить толщину',
                                    command=self.update_width)
        self.btn_set_width.pack(side=LEFT, padx=5)

        # Привязка событий к кнопкам мыши (к холсту)
        self.canvas.bind('<Button-1>', self.start_draw)
        self.canvas.bind('<B1-Motion>', self.draw)

    def clear_canvas(self):
        self.canvas.delete('all')

    def set_color(self, new_color):
        self.color = new_color

    def update_width(self):
        try:
            temp = int(self.width_entry.get())
            if 0 < temp < 25:
                self.line_width = temp
            else:
                self.line_width = 10
        except ValueError:
            pass

    def start_draw(self, event):
        # Фиксация координат клика мыши при начале рисования
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        # Линия от точки к точке при движении мыши
        if self.last_x and self.last_y:
            self.canvas.create_line(
                self.last_x, self.last_y,
                event.x, event.y,
                fill=self.color, width=self.line_width,
                capstyle=ROUND, smooth=True
            )
        self.last_x, self.last_y = event.x, event.y


if __name__ == '__main__':
    root = Tk()
    app = DrawApp(root)
    root.mainloop()
