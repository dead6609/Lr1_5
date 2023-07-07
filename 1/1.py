
from tkinter import LEFT, RIGHT, ttk
from PIL import Image, ImageFilter , ImageTk
import sys
import tkinter as tk
from tkinter.ttk import Frame, Label
import tkinter.filedialog as fd



class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()


    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=3)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.btn_open_quest_1 = tk.Button(toolbar, text="LR1.5 Задание 1", command=self.open_dialog_lr15_z1, bd=2, compound=tk.TOP)

        self.btn_open_quest_1.pack(side=tk.LEFT)


    def open_dialog_lr15_z1(self):
        pre_lr15_z1()

class pre_lr15_z1(tk.Toplevel):
    def __init__(self):
        super().__init__()
        btn_file = tk.Button(self, text="Выбрать файл",
                             command=self.choose_file)
        btn_file.pack(padx=60, pady=10)
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def choose_file(self):
        filetypes = (("Изображение", "*.jpg *.gif *.png"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            lr15_z1(filename)

class lr15_z1(tk.Toplevel):
    def __init__(self,filename):
        super().__init__(root)
        self.fn = filename
        self.init_child()



    def r_chanel(self):
        im = self.img_norm.convert('RGB')

        # Split into 3 channels
        r, g, b = im.split()

        # Increase Reds
        r = r.point(lambda i: i * 1)

        # Decrease Greens
        g = g.point(lambda i: i * 0)

        b = b.point(lambda i: i * 0)

        # Recombine back to RGB image
        self.img = Image.merge('RGB', (r, g, b))
        self.img.thumbnail([300,300], Image.NEAREST)

        self.tatras = ImageTk.PhotoImage(self.img)
        self.label = Label(self, image=self.tatras)
        self.label.image = self.tatras
            
        self.label.place(x=260,y=30)


    def b_chanel(self):
        im = self.img_norm.convert('RGB')

        # Split into 3 channels
        r, g, b = im.split()

        # Increase Reds
        r = r.point(lambda i: i * 0)

        # Decrease Greens
        g = g.point(lambda i: i * 0)

        b = b.point(lambda i: i * 1)

        # Recombine back to RGB image
        self.img = Image.merge('RGB', (r, g, b))
        self.img.thumbnail([300,300], Image.NEAREST)

        self.tatras = ImageTk.PhotoImage(self.img)
        self.label = Label(self, image=self.tatras)
        self.label.image = self.tatras
            
        self.label.place(x=260,y=30)

    def g_chanel(self):
        im = self.img_norm.convert('RGB')

        # Split into 3 channels
        r, g, b = im.split()

        # Increase Reds
        r = r.point(lambda i: i * 0)

        # Decrease Greens
        g = g.point(lambda i: i * 1)

        b = b.point(lambda i: i * 0)

        # Recombine back to RGB image
        self.img = Image.merge('RGB', (r, g, b))
        self.img.thumbnail([300,300], Image.NEAREST)

        self.tatras = ImageTk.PhotoImage(self.img)
        self.label = Label(self, image=self.tatras)
        self.label.image = self.tatras
            
        self.label.place(x=260,y=30)


    def all_chanel(self):
        self.img = self.img_norm
        self.img.thumbnail([300,300], Image.NEAREST)

        self.tatras = ImageTk.PhotoImage(self.img)
        self.label = Label(self, image=self.tatras)
        self.label.image = self.tatras
            
        self.label.place(x=260,y=30)

    def rot_90(self):
            self.label.pack_forget()
            self.label = None

            self.img=self.img.rotate(90)
            self.img_norm = self.img_norm.rotate(90)

            self.tatras = ImageTk.PhotoImage(self.img)
            self.label = Label(self, image=self.tatras)
            self.label.image = self.tatras
            
            self.label.place(x=260,y=30)

    def rev_rot_90(self):
            self.label.pack_forget()
            self.label = None

            self.img=self.img.rotate(-90)
            self.img_norm = self.img_norm.rotate(-90)

            self.tatras = ImageTk.PhotoImage(self.img)
            self.label = Label(self, image=self.tatras)
            self.label.image = self.tatras
            
            self.label.place(x=260,y=30)

    def init_child(self):
        self.title("Quest №1")
        self.geometry("600x450+400+400")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        self.btn_red = tk.Button(self,text="R", bd=2, width=20, height=1, command=self.r_chanel)
        self.btn_green = tk.Button(self,text="G", bd=2,  width=20, height=1, command=self.g_chanel)
        self.btn_blue = tk.Button(self,text="B", bd=2, width=20, height=1, command=self.b_chanel)
        self.btn_all = tk.Button(self,text="ALL", bd=2, width=20, height=1, command=self.all_chanel)

        self.btn_right_rotate = tk.Button(self,text="Повернуть по часовой", bd=2, width=25, height=2, command=self.rev_rot_90)
        self.btn_left_rotate = tk.Button(self,text="Повернуть против по часовой", bd=2, width=25, height=2, command=self.rot_90)

        self.btn_red.place(x=25, y=50)
        #self.btn_red.pack()
        self.btn_green.place(x=25, y=125)
        #self.btn_green.pack()
        self.btn_blue.place(x=25, y=200)
        #self.btn_blue.pack()
        self.btn_all.place(x=25, y=275)

        self.btn_right_rotate.place(x=380, y=350)
        self.btn_left_rotate.place(x=25, y=350)


        self.img = Image.open(self.fn)
        self.img_norm = Image.open(self.fn)
        self.img.thumbnail([300,300], Image.NEAREST)
        self.tatras = ImageTk.PhotoImage(self.img)
        self.label = Label(self, image=self.tatras)
        self.label.image = self.tatras
        
        self.label.place(x=260,y=30)

        




if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Lr1.5-Lr1.7")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
