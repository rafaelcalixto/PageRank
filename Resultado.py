import tkinter
from tkinter import ttk

class Resultado():
    def __init__(self):
        self.tela = tkinter.Tk()
        self.fonte = ('Ariel Black', 12)
        self.texto = 'Googlis!'
        self.pos_x = 20
        self.pos_y = 80

        ###########  BARRA DE ROLAGEM  #############
        self.subTela = tkinter.Canvas(self.tela, width = 600, height = 1100)
        self.canvas = tkinter.Canvas(self.subTela, width = 600, height = 1100)
        self.frameTela = tkinter.Frame(self.canvas, width = 600, height = 1100)
        ###########  BARRA DE ROLAGEM  #############

    def exibir(self, lista_resultado):
        self.tela.wm_title('Googlis!')
        self.tela.wm_minsize(width = 600, height = 250)

        ###########  BARRA DE ROLAGEM  #############
        roll = ttk.Scrollbar(self.subTela, orient = 'vertical', command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = roll.set)
        roll.pack(side = 'right', fill = 'y')
        self.canvas.pack(side = 'left', fill = 'both', expand = True)
        self.canvas.create_window((4,4), window = self.frameTela, anchor = 'nw', tags = 'frameTela')
        self.frameTela.bind('<Configure>', self.canvas.configure(scrollregion = self.canvas.bbox('all')))
        self.subTela.pack(side='left', fill = 'y')
        ###########  BARRA DE ROLAGEM  #############
        
        tkinter.Label(self.frameTela
                      , text = self.texto
                      , font = self.fonte).place(x = 270, y = 20)

        for cada_resultado in lista_resultado:
            resultado_exibido = cada_resultado['titulo'] + '\n' + cada_resultado['url'] + '\nRanking: ' + str(cada_resultado['ranking'])

            tkinter.Label(self.frameTela,
                         text = resultado_exibido,
                         bg = '#99cccc',
                         bd = 2,
                         relief = 'solid',
                         font = self.fonte,
                         width = 30,
                         height = 2).place(x = self.pos_x, y = self.pos_y, width = 560, height = 90)

            self.pos_y += 100
