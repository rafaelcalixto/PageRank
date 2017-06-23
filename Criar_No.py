import bs4 #Beautifulsoup

class Criar_No:
    def criar(dados_html, url_no):
        no = {}
        no['titulo'] = None
        no['url'] = url_no
        no['links'] = []
        no['ranking'] = 0
        
        tags_html = bs4.BeautifulSoup(dados_html, 'lxml')
        #### lxml é uma dependência

        titulo = tags_html.find('title')
        subtitle = tags_html.find('h3')
        
        if titulo is not None:
            no['titulo'] = titulo.text
        else:
            no['titulo'] = 'Unknow'
        if subtitle is not None:
            for h3 in subtitle:
                if isinstance(h3, str) and len(h3) < 40:
                    no['titulo'] += '-' + h3
                    print(no['titulo'])

        lista_links = tags_html.find_all('a', href = True)

        for cada_link in list(set(lista_links)):
            if 'http' in cada_link['href']:
                no['links'].append(cada_link['href'])

        return no
