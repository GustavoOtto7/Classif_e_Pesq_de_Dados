import Bst
import Hash_table
from Jogo import Jogo

def main():
    arvore_jogos = Bst.ArvoreJogos() 
    hash_generos = Hash_table.HashGeneros()
    while True:
        menu = """
        --- MENU ---
        Escolha uma opção:
        1. Adicionar jogo
        2. Buscar jogo por preço
        3. Buscar jogo por faixa de preço
        4. Buscar jogo por gênero
        5. Listar todos os jogos em ordem de preço
        6. Sair
        """
        print(menu)
        opc = int(input("Digite a opção desejada: "))
        if opc == 1:
            print("Adicionar jogo: ")
            jogo_id = input("Digite o ID: ")
            titulo = input("Digite o título: ")
            desenvolvedor = input("Digite o desenvolvedor: ")
            preco = int(input("Digite o preço: "))
            generos = input("Digite os gêneros separados por vírgula: ").split(",")
            jogo = Jogo(jogo_id, titulo, desenvolvedor, preco, [g.strip() for g in generos])
            arvore_jogos.inserir(jogo)  
            hash_generos.adicionar_jogo(jogo)
            print("Jogo adicionado com sucesso!\n")

        elif opc == 2:
            preco = int(input("Digite o valor desejado: "))
            resultado = arvore_jogos.buscar_por_preco(preco)
            print(f"Jogo encontrado: {resultado}\n" if resultado else "Nenhum jogo encontrado.\n")
        
        elif opc == 3:
            preco_min = int(input("Digite o valor mínimo desejado: "))
            preco_max = int(input("Digite o valor máximo desejado: "))
            resultados = arvore_jogos.buscar_por_faixa_preco(preco_min, preco_max)
            if resultados:
                print("Jogos encontrados na faixa de preço:")
                for jogo in resultados:
                    print(jogo)
            else:
                print("Nenhum jogo encontrado nesta faixa de preço.\n")

        elif opc == 4:
            genero = input("Digite o gênero desejado: ")
            resultados = hash_generos.obter_jogos(genero, arvore_jogos)
            if resultados:
                print(f"Jogos encontrados no gênero '{genero}':")
                for jogo in resultados:
                    print(jogo)
            else:
                print("Nenhum jogo encontrado neste gênero.\n")

        elif opc == 5:
            jogos_ordenados = arvore_jogos.em_ordem()
            print("Jogos em ordem crescente de preço:")
            for jogo in jogos_ordenados:
                print(jogo)

        elif opc == 6:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
main()