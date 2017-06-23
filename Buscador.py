import bs4 #Beautifulsoup

class Buscador:
    def google_it(dados_html, pesquisa):
        encontrado = False

        if dados_html is not None:
            tags_html = bs4.BeautifulSoup(dados_html, 'lxml')
            #### lxml é uma dependência
            
            body_tag = tags_html.find('body')

            if body_tag is not None:
                texto = body_tag.text

                if pesquisa in texto.lower():
                    encontrado = True

        return encontrado
