class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo    
        self.esq = None     
        self.dire = None    

class ArvoreJogos:
    def __init__(self):
        self.raiz = None    

    def inserir(self, jogo):
        novo_no = NoJogo(jogo)  
        if self.raiz is None:   
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, nodo_atual, novo_no):
        if novo_no.jogo.preco < nodo_atual.jogo.preco:
            if nodo_atual.esq is None:
                nodo_atual.esq = novo_no
            else:
                self._inserir_recursivo(nodo_atual.esq, novo_no)
        else:
            if nodo_atual.dire is None:
                nodo_atual.dire = novo_no
            else:
                self._inserir_recursivo(nodo_atual.dire, novo_no)

    def buscar_por_preco(self, preco):
        resultados = [] 
        self._buscar_recursivo(self.raiz, preco, resultados)
        if not resultados:
            print(f"Nenhum jogo encontrado com o preço: R$ {preco}")
        return resultados

    def _buscar_recursivo(self, nodo_atual, preco, resultados):
        if nodo_atual is None:
            return
        if preco == nodo_atual.jogo.preco:
            resultados.append(nodo_atual.jogo)
        self._buscar_recursivo(nodo_atual.esq, preco, resultados)
        self._buscar_recursivo(nodo_atual.dire, preco, resultados)  

    def buscar_por_faixa_preco(self, preco_min, preco_max):
        resultados = []
        self._buscar_faixa_recursivo(self.raiz, preco_min, preco_max, resultados)
        return resultados

    def _buscar_faixa_recursivo(self, nodo_atual, preco_min, preco_max, resultados):
        if nodo_atual is None:
            return
        if preco_min <= nodo_atual.jogo.preco <= preco_max:
            resultados.append(nodo_atual.jogo)
        if preco_min < nodo_atual.jogo.preco:
            self._buscar_faixa_recursivo(nodo_atual.esq, preco_min, preco_max, resultados)
        if preco_max >= nodo_atual.jogo.preco:
            self._buscar_faixa_recursivo(nodo_atual.dire, preco_min, preco_max, resultados)

    def buscar_por_id(self, jogo_id):
        return self._buscar_id_recursivo(self.raiz, jogo_id)

    def _buscar_id_recursivo(self, nodo_atual, jogo_id):
        if nodo_atual is None:
            return None
        if nodo_atual.jogo.jogo_id == jogo_id:
            return nodo_atual.jogo
        esquerdo = self._buscar_id_recursivo(nodo_atual.esq, jogo_id)
        if esquerdo:
            return esquerdo
        return self._buscar_id_recursivo(nodo_atual.dire, jogo_id)

    def em_ordem(self):
        resultados = []
        self._em_ordem_recursivo(self.raiz, resultados)
        return resultados

    def _em_ordem_recursivo(self, nodo_atual, resultados):
        if nodo_atual is not None:
            self._em_ordem_recursivo(nodo_atual.esq, resultados)  
            resultados.append(nodo_atual.jogo)                    
            self._em_ordem_recursivo(nodo_atual.dire, resultados) 