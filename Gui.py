import tkinter as tk                # python 3
from tkinter import font as tkfont # python 3
from tkinter import ttk
from tkinter import messagebox as mBox
import ToolTip as tt


class TopScreen(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.background_color = '#7E97FA'
        self.text_color = '#222c54'
        self.button_color = '#acbaf2'

        self.title_font = tkfont.Font(family='Tahoma', size=10, weight="bold", slant="italic")
        self.title("AutoChar")
        self.configure(background=self.background_color)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, NewCharSystemPage, NewCharSpecPage, NewCharAbilityPage, CharSheetPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def load_char(self):
        mBox.showinfo("Todo Message Info Box", "This will load old character\nsheet")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        brand = ttk.Label(self, text="WiseGuy Productions", font=controller.title_font, justify="center")
        brand.grid(column=0, row=0, columnspan=2)

        controller.minsize(width=250, height=60)
        self.new_character = ttk.Button(self, text="New Character", command=lambda: controller.show_frame("NewCharSystemPage"))
        self.new_character.grid(column=0, row=1)
        self.old_character = ttk.Button(self, text="Load Character", command=lambda: controller.load_char())
        self.old_character.grid(column=1, row=1)

        tt.createToolTip(self.old_character, 'Need to write the code for this, probably Pickle')
        tt.createToolTip(self.new_character, 'Should go to next window to create a new character')


class NewCharSystemPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="NewCharSystemPage", font=controller.title_font)
        label.grid(column=0, row=0, columnspan=2)

        system = tk.StringVar()
        adjective = tk.StringVar()
        noun = tk.StringVar()
        verb = tk.StringVar()
        # description = tk.StringVar() #will use this for description text

        self.description_label = ttk.Label(self, borderwidth=5, relief="groove", padding=10, width=48, wraplength=320, justify='left', textvariable=system)#TODO
        self.description_label.grid(column=1, row=1, rowspan=7)

        system_label = ttk.Label(self,width=12, text="System")
        system_label.grid(column=0, row=1)

        self.system_chosen = ttk.Combobox(self, width=12, textvariable=system)
        self.system_chosen['values'] = ("Numenera", "Predation", "The Strange", "Gods of the Fall")
        self.system_chosen.grid(column=0, row=2)
        self.system_chosen.current(0)

        adjective_label = ttk.Label(self, width=12, text="A(n) ...")
        adjective_label.grid(column=0, row=3)

        self.adjective_chosen = ttk.Combobox(self, width=12, textvariable=adjective)
        self.adjective_chosen['values'] = ["list", "of", "Adjectives"]
        self.adjective_chosen.grid(column=0, row=4)
        self.adjective_chosen.current(0)

        self.noun_chosen = ttk.Combobox(self, width=12, textvariable=noun)
        self.noun_chosen['values'] = ('List', "of", "Noun")
        self.noun_chosen.grid(column=0, row=5)
        self.noun_chosen.current(0)

        verb_label = ttk.Label(self, width=12, text="Who...")
        verb_label.grid(column=0, row=6)

        self.verb_chosen = ttk.Combobox(self, width=12, textvariable=verb)
        self.verb_chosen['values'] = ("List", "of", "Verbs")
        self.verb_chosen.grid(column=0, row=7)
        self.verb_chosen.current(0)

        tt.createToolTip(self.system_chosen, 'Choose a System')
        tt.createToolTip(self.adjective_chosen, "Choose your Descriptor")
        tt.createToolTip(self.noun_chosen, "Choose your Noun")
        tt.createToolTip(self.verb_chosen, "Choose your Focus")


class NewCharSpecPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="NewCharSpecPage", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("NewCharAbilityPage"))
        button.pack()


class NewCharAbilityPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="NewCharAbilityPage", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class CharSheetPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="CharSheetPage", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = TopScreen()
    app.mainloop()