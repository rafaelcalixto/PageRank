class Ranking:
    def criar(catalogo):
        d = 0.8 # Amortecimento
        
        #### primeira fase: contagem de links
        for pos_no in range(0, len(catalogo)):
            no = catalogo[pos_no]
            for link in catalogo:
                for cada_link in link['links']:
                    if no['url'] in cada_link:
                        no['ranking'] = no['ranking'] + 1

        #### segunda fase: aplicação do cálculo
        for pos_no in range(0, len(catalogo)):
            no = catalogo[pos_no]
            for link in catalogo:
                for cada_link in link['links']:
                    if no['url'] in cada_link:
                        no['ranking'] = ((1 - d) + d * (link['ranking'] / no['ranking']))

        #### terceira fase: bubble sort para ordenação
        contador = 1
        while contador < len(catalogo):
            atual = catalogo[contador - 1]['ranking']
            proximo = catalogo[contador]['ranking']
            if atual < proximo:
                catalogo.insert(contador - 1, catalogo.pop(contador))
                contador = 1
            else:
                contador += 1
