from tkinter import *
from learn_language import *
from languages import *





class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def get_word(self,language):
        l=Learning()
        return l.get_random_word(language)


    def create_widgets(self):

        self.v = IntVar()
        self.label=Label(root,
              text="""Valitse kieli:""",
              justify=LEFT,
              padx=20).pack()

        self.finnish=Radiobutton(root,
                    text="Suomi -> Ruotsi",
                    padx=20,
                    variable=self.v,
                    value=Languages.FINNISH,
                    command=self.sel).pack(anchor=W)
        self.swedish=Radiobutton(root,
                    text="Ruotsi -> Suomi",
                    padx=20,
                    variable=self.v,
                    value=Languages.SWEDISH,
                    command=self.sel).pack(anchor=W)

        self.quit = Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")



        self.label_verb=Label(root)
        self.label_verb.pack()

        self.label_selection = Label(root)
        self.label_selection.pack()

        self.textinput = Text(root, height=1)
        self.textinput.pack()


    def say_hi(self):
        print("hi there, everyone!")
    def sel(self):
        selection = "Kirjoita alla olevaan kenttään: "

        if self.v.get()==Languages.FINNISH:
            self.label_verb.config(text=self.get_word(Languages.FINNISH))
            selection+="verbin ruotsinkielinen käännös aikamuotoineen"

        else:
            self.label_verb.config(text=self.get_word(Languages.SWEDISH))
            selection += "verbin suomenkielinen käännös."

        self.label_selection.config(text=selection)

root = Tk()

app = Application(master=root)
app.master.minsize(400,400)
app.mainloop()