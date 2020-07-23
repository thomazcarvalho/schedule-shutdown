import tkinter as tk
from tkinter import ttk


class Aplication:

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.canvas = tk.Canvas()

        self.container1 = ttk.Frame(
            self.master,
            borderwidth=10,
            heigh=5,
            padding=3,
            relief='groove'
        )
        self.container1.grid(row=0)

        self.title = ttk.Label(
            self.container1,
            font=('Arial', 10, 'bold'),
            text='Windows'
        )
        self.title.pack(side='top')
        self.title = ttk.Label(
            self.container1,
            font=('Arial', 10, 'bold'),
            text='Agendar Desligamento do Sistema'
        )
        self.title.pack(side='bottom')

        self.container_extra = ttk.Frame(
            self.master,
            padding=13
        )
        self.container_extra.grid(row=1)

        self.ask = ttk.Label(
            self.container_extra,
            font=('Arial', 10),
            text='Você deseja: '
        )
        self.var = tk.IntVar()
        self.ask.pack(side='left')
        self.ask_entry1 = ttk.Radiobutton(
            self.container_extra,
            text='Agendar desligamento',
            variable=self.var,
            value=0,
            command=self.hide_show_entry
        )
        self.ask_entry1.pack(side='left')
        self.ask_entry2 = ttk.Radiobutton(
            self.container_extra,
            text='Abortar agendamento',
            variable=self.var,
            value=1,
            command=self.hide_show_entry
        )
        self.ask_entry2.pack(side='left')

        self.container2 = ttk.Frame(
            self.master,
            padding=5
        )
        self.container2.grid(row=2)

        self.txt1 = ttk.Label(
            self.container2,
            font=('Arial', 10),
            text='Digite o tempo em minutos: '
        )
        self.txt1.pack(side='left')
        self.txt1_entry = ttk.Entry(
            self.container2,
            width=10
        )
        self.txt1_entry.pack(side='left')

        self.container3 = ttk.Frame(
            self.master,
            padding=15
        )
        self.container3.grid(row=3)

        self.exit_button = ttk.Button(
            self.container3,
            width=10,
            text='Sair',
            command=self.master.destroy
        )
        self.exit_button.pack(side='left')
        self.confirm_button = ttk.Button(
            self.container3,
            width=10,
            text='Confirmar',
            command=self.confirm
        )
        self.confirm_button.pack(side='left')

        self.container4 = ttk.Frame(
            self.master,
            padding=10
        )
        self.container4.grid(row=4)

        self.status = ttk.Label(
            self.container4,
            font=('Arial', 10)
        )

    def confirm(self):
        from os import system
        if self.var.get() == 0:
            try:
                time_in_secs = int(self.txt1_entry.get()) * 60
                system(f'shutdown -s -t {time_in_secs}')
            except Exception:
                self.status['text'] = (
                    'Ocorreu um erro. Contatar desenvolvedor.'
                )
                self.status.pack()
            else:
                self.status['text'] = 'Agendamento realizado com sucesso.'
                self.status.pack()
        else:
            try:
                system('shutdown -a')
            except Exception:
                self.status['text'] = (
                    'Ocorreu um erro. Contatar desenvolvedor.'
                )
                self.status.pack()
            else:
                self.status['text'] = 'Desagendamento realizado com sucesso.'
                self.status.pack()

    def hide_show_entry(self):
        if self.var.get() == 1:
            self.txt1.pack_forget()
            self.txt1_entry.pack_forget()
            self.container2.grid_forget()
        elif self.var.get() == 0:
            self.container2.grid(row=2)
            self.txt1.pack(side='left')
            self.txt1_entry.pack(side='left')


root = tk.Tk()
root.title('Agendar Desligamento')
Aplication(root)
root.mainloop()
