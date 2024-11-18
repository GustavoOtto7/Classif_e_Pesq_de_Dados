class Nodo:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dire = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        def _inserir(nodo, chave):
            if not nodo:
                return Nodo(chave)
            if chave < nodo.chave:
                nodo.esq = _inserir(nodo.esq, chave)
            else:
                nodo.dire = _inserir(nodo.dire, chave)
            return nodo

        self.raiz = _inserir(self.raiz, chave)

    def buscar(self, chave):
        def _buscar(nodo, chave):
            if not nodo or nodo.chave == chave:
                return nodo
            if chave < nodo.chave:
                return _buscar(nodo.esq, chave)
            return _buscar(nodo.dire, chave)

        return _buscar(self.raiz, chave)

    def deletar(self, chave):
        def _deletar(nodo, chave):
            if not nodo:
                return None
            if chave < nodo.chave:
                nodo.esq = _deletar(nodo.esq, chave)
            elif chave > nodo.chave:
                nodo.dire = _deletar(nodo.dire, chave)
            else:
                if not nodo.esq and not nodo.dire:
                    return None
                if not nodo.esq:
                    return nodo.dire
                if not nodo.dire:
                    return nodo.esq
                temp = self._menor_valor_nodo(nodo.dire)
                nodo.chave = temp.chave
                nodo.dire = _deletar(nodo.dire, temp.chave)
            return nodo
        self.raiz = _deletar(self.raiz, chave)

    def _menor_valor_nodo(self, nodo):
        atual = nodo
        while atual.esq:
            atual = atual.esq
        return atual

    def pre_ordem(self, nodo=None):
        if nodo is None:
            if self.raiz is None:  
                return
            nodo = self.raiz
        print(nodo.chave, end=" ")
        if nodo.esq:
            self.pre_ordem(nodo.esq)
        if nodo.dire:
            self.pre_ordem(nodo.dire)

    def em_ordem(self, nodo=None):
        if nodo is None:
            if self.raiz is None:  
                return
            nodo = self.raiz
        if nodo.esq:
            self.em_ordem(nodo.esq)
        print(nodo.chave, end=" ")
        if nodo.dire:
            self.em_ordem(nodo.dire)

    def pos_ordem(self, nodo=None):
        if nodo is None:
            if self.raiz is None: 
                return
            nodo = self.raiz
        if nodo.esq:
            self.pos_ordem(nodo.esq)
        if nodo.dire:
            self.pos_ordem(nodo.dire)
        print(nodo.chave, end=" ")

if __name__ == "__main__":
    abb = ArvoreBinariaBusca()
    abb.inserir(50)
    abb.inserir(30)
    abb.inserir(70)
    abb.inserir(20)
    abb.inserir(40)
    abb.inserir(60)
    abb.inserir(80)

    print("Pré-ordem:")
    abb.pre_ordem()
    print("\nEm ordem:")
    abb.em_ordem()
    print("\nPós-ordem:")
    abb.pos_ordem()

    print("\n\nBuscar por 40:")
    print(abb.buscar(40).chave if abb.buscar(40) else "Não encontrado")

    abb.deletar(20)
    print("\nApós deletar 20 (em ordem):")
    abb.em_ordem()
