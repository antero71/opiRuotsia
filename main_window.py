from tkinter import *
from learn_language import *
from languages import *




class Application(Frame):

    def __init__(self, master=None,file_name="sanasto.txt"):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.learn=Learning(file_name)
        self.points=0
        self.word=""

    def get_word(self,language):
        return self.learn.get_random_word(language)

    def check_answer(self, event):
        answer_string = self.textinput.get("1.0", END)
        verb=self.word[1]
        index=self.word[0]
        points=self.points
        ret=self.learn.check_answer(self.v.get(), None, answer_string, points, index)
        if len(ret)>0:
            self.points=ret[0]

        if len(ret)==3:
            self.label_check_answer.config(text="Sinulla on pisteitä "+str(ret[0])+"\n"+ret[1]+"\n"+ret[2])
        elif len(ret)==2:
            self.label_check_answer.config(text="Sinulla on pisteitä "+str(ret[0])+"\n"+ret[1])


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
                    command=self.select_language).pack(anchor=W)
        self.swedish=Radiobutton(root,
                    text="Ruotsi -> Suomi",
                    padx=20,
                    variable=self.v,
                    value=Languages.SWEDISH,
                    command=self.select_language).pack(anchor=W)

        self.quit = Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")



        self.label_verb=Label(root)
        self.label_verb.pack()

        self.label_selection = Label(root)
        self.label_selection.pack()

        self.textinput = Text(root, height=1,width=50)
        self.textinput.bind("<KeyPress-Return>",self.check_answer)
        self.textinput.focus_set()
        self.textinput.pack()

        self.label_check_answer=Label(root)
        self.label_check_answer.pack()

        self.play_again_button=Button(root,text="Uusi sana",command=self.select_language)
        self.play_again_button.pack()



    def select_language(self):
        selection = "Kirjoita alla olevaan kenttään "

        if self.v.get()==Languages.FINNISH:
            self.word=self.get_word(Languages.FINNISH)
            self.label_verb.config(text=self.word[1])
            selection+="verbin ruotsinkielinen käännös aikamuotoineen"

        else:
            self.word=self.get_word(Languages.SWEDISH)
            self.label_verb.config(text=self.word[1])
            selection += "verbin suomenkielinen käännös."

        self.label_selection.config(text=selection)

root = Tk()

app = Application(master=root)
app.master.minsize(400,400)
app.mainloop()