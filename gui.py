from tkinter import *
from tkinter import messagebox
import functions


class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("Kalkulator Nutrisi")
        self.switch(Menu)
        self.geometry('350x350')
        self.config(bg = "Black")

    def switch(self, frame_class):
        """Berpindah Ke Halaman Main Menu"""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Menu(Frame):
    """Main menu"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        """Frame widgets"""
        label = Label(self, text = "Kalkulator Nutrisi!\n Silahkan memilih opsi dibawah."\
                      , bg = "black", fg = "white")
        label.pack()
        button = Button(self, text = "Kalkulator", width = 20, command = lambda: master.switch(Calculator))
        button.pack(padx = 10, pady = 10)
        button2 = Button(self, text = "Input data makanan", width = 20, command = lambda: master.switch(File_Write))
        button2.pack()
        button3 = Button(self, text = "Exit", width = 20, command = self.close)
        button3.pack(padx = 10, pady = 10)

    def close(self):
        """Keluar"""
        self.destroy()
        exit()


class Calculator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        def on_click():
            product = entryProduct.get()
            gram = entryGram.get()
            output.delete(0.0, END)

            Error = False
            try:
                gram = int(entryGram.get())
            except:
                Error = True
            try:
                x = int(product)
                Error = True
            except:
                pass
            if Error == True:
                messagebox.showerror("Error", "Masukkan Data Yang Sesuai!")
            else:
                functions.file_open()
                output.insert(END, functions.result(product, gram))

        """Frame"""
        label = Label(self, text ="Masukkan makanan yang anda makan.", bg = "black", fg = "white")
        label.pack()
        # user input, product
        label2 = Label(self, text = "Nama: ", bg = "black", fg = "white")
        label2.pack()
        entryProduct = Entry(self, width = 20, bg = "white")
        entryProduct.pack()
        # user input, amount
        label3 = Label(self, text = "Jumlah/Gram: ", bg = "black", fg = "white")
        label3.pack()
        entryGram = Entry(self, width = 20, bg = "white")
        entryGram.pack()
        # submit
        submit = Button(self, text = "Submit", width = 8, command = on_click)
        submit.pack(padx = 10, pady = 10)
        # output
        label4 = Label(self, text = "Hasil perhitungan nutrisi:", bg = "black", fg = "white")
        label4.pack()
        output = Text(self, width = 20, height = 6, wrap = WORD, bg = "white")
        output.pack()
        #going back to menu
        self.button = Button(self, text = "Back", width = 8, command = lambda: master.switch(Menu))
        self.button.pack(padx = 10, pady = 10)


class File_Write(Frame):
    """Menambahkan makanan"""
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg = "black")

        def validate():
            """cek apakah user sudah memasukkan data dengan benar"""
            def write(name, kcal, protein, karbohidrat, lemak):
                """Writes to file"""
                file = open("Products.txt", "a")
                productValue = "%s,%s:%s:%s:%s" % (name, kcal, protein, karbohidrat, lemak)
                file.write("\n" + productValue)
                file.close()
                nameEntry.delete(0, END)
                kcalEntry.delete(0, END)
                proteinEntry.delete(0, END)
                karbohidratEntry.delete(0, END)
                lemakEntry.delete(0, END)

            error = False  
            try:
                name = int(nameEntry.get())
                error = True
            except:
                 name = nameEntry.get()
            try:
                kcal = int(kcalEntry.get())
                protein = int(proteinEntry.get())
                karbohidrat = int(karbohidratEntry.get())
                lemak = int(lemakEntry.get())
            except:
                error = True
            if error == True:
                messagebox.showerror("Error", "Masukkan Data Yang Sesuai!")
            else:
                #writing to a file
                write(name, kcal, protein, karbohidrat, lemak)

        """Frame"""
        label = Label(self, text ="Masukkan jenis makanan berdasarkan nutrisi "\
                " per 100 gram", bg = "black", fg = "white")
        label.pack()
        label1 = Label(self, text = "Nama:", bg = "black", fg = "white")
        label1.pack()
        nameEntry = Entry(self, width = 20, bg = "white")
        nameEntry.pack()

        label2 = Label(self, text = "Kalori:", bg = "black", fg = "white")
        label2.pack()
        kcalEntry = Entry(self, width = 20, bg = "white")
        kcalEntry.pack()

        label3 = Label(self, text = "Protein:", bg = "black", fg = "white")
        label3.pack()
        proteinEntry = Entry(self, width = 20, bg = "white")
        proteinEntry.pack()

        label4 = Label(self, text = "Karbohidrat:", bg = "black", fg = "white")
        label4.pack()
        karbohidratEntry = Entry(self, width = 20, bg = "white")
        karbohidratEntry.pack()

        label5 = Label(self, text = "Lemak:", bg = "black", fg = "white")
        label5.pack()
        lemakEntry = Entry(self, width = 20, bg = "white")
        lemakEntry.pack()

        submit = Button(self, text = "Submit", width = 8, command = validate)
        submit.pack(padx = 10, pady = 10)

        button3 = Button(self, text = "Back", width = 20, command = lambda: master.switch(Menu))
        button3.pack(padx = 10, pady = 10)


if __name__ == "__main__":
    app = App()
    app.mainloop()

