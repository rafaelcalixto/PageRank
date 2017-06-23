from urllib import request, parse

class Crawler():
    def __init__(self):
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux 1686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
        self.tipo_encode = 'utf-8'
        self.historico_url = []

    def get_it(self, site_buscado):
        dados_parseados = None

        if site_buscado not in self.historico_url:
            try:
                print(site_buscado)
                rec_busca = request.Request(site_buscado, headers = self.headers)
                dados_brutos = request.urlopen(rec_busca)
                dados_parseados = dados_brutos.read()
            except Exception as e:
                print('Não foi possível acessar a URL:'
                      , site_buscado
                      , '\n'
                      , e)
                
        self.historico_url.append(site_buscado)

        return dados_parseados
