import tkinter
import PageRank

class Google():
    def __init__(self):
        self.tela = tkinter.Tk()
        self.fonte = ('Ariel Black', 12)
        self.texto = 'Googlis!'

    def pesquisar(self):
        self.tela.wm_title('Googlis!')
        self.tela.wm_minsize(width = 500, height = 250)
        tkinter.Label(self.tela
                      , text = self.texto
                      , font = self.fonte).pack(side = 'top')
        
        #####  IMAGEM
        img = tkinter.PhotoImage(file = 'googlis.png')
        logo = tkinter.Button(self.tela, image = img)
        logo.image = img
        logo.place(x = 190, y = 30)
        
        #####  BOTÕES
        busca = tkinter.Entry(self.tela)
        busca.place(x = 150, y = 150, width = 200)

        botao_1 = tkinter.Button(self.tela
                                 , text = 'Pesquisa Googlis!'
                                 , command = lambda: PageRank.PageRank(busca.get()).rank_it())
                                 
        botao_2 = tkinter.Button(self.tela
                                 , text = 'Estou com sorte!')

        botao_1.place(x = 130, y = 200)
        botao_2.place(x = 270, y = 200)

Google().pesquisar()
