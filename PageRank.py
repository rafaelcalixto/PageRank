import Crawler
import Criar_No
import Ranking
import Buscador
import Resultado
import Grafo

class PageRank():
    def __init__(self, busca, distancia = 5):
        self.ponto_inicial = 'http://www.rugbyfluminense.com.br/'
        self.distancia = 2
        self.crawler = Crawler.Crawler()
        self.criar_no = Criar_No.Criar_No
        self.catalogo = []
        self.busca = busca #### termo buscado
        self.grafo = Grafo.Grafo()

    def rank_it(self):
        no_atual = 0
        
        dados_html = self.crawler.get_it(self.ponto_inicial)
        no_inicial = self.criar_no.criar(dados_html, self.ponto_inicial)

        self.catalogo.append(no_inicial)

        while no_atual < self.distancia:
            for cada_no in self.catalogo.copy():
                for cada_link in cada_no['links'].copy():
                    dados_html = self.crawler.get_it(cada_link)
                    relacionado = Buscador.Buscador.google_it(dados_html, self.busca)
                    if relacionado:
                        novo_no = self.criar_no.criar(dados_html, cada_link)
                        self.catalogo.append(novo_no)
                
            no_atual += 1

        Ranking.Ranking.criar(self.catalogo)

        Resultado.Resultado().exibir(self.catalogo[:10])

        self.grafo.criar_grafo(self.catalogo[:10])
