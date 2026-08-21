from tkinter import *

root = Tk()
root.title('что-то')
root.geometry('700x500')
hallo = Label(text='Выбери кнопку', fg='red', font=('arial', 22))
hallo.pack()

photo = PhotoImage(file='D:\\Фото\\Китай\\IMG_20250425_161401.jpg')
btn = Button(root, image=photo)

btn.pack()

root.mainloop()
