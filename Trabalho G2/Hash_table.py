class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = {}  

    def adicionar_jogo(self, jogo):
        for genero in jogo.generos:  
            if genero not in self.genero_para_jogos:
                self.genero_para_jogos[genero] = []  
            if jogo.jogo_id not in self.genero_para_jogos[genero]: 
                self.genero_para_jogos[genero].append(jogo.jogo_id)  

    def obter_jogos(self, genero, arvore_jogos):
        ids = self.genero_para_jogos.get(genero, [])
        resultados = []
        for jogo_id in ids:
            jogo = arvore_jogos.buscar_por_id(jogo_id)  
            if jogo:
                resultados.append(jogo)
        return resultados
