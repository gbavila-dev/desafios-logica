# ==================================================
# REVISÃO DE PYTHON
# ==================================================

# ==================================================
# QUESTÃO 26 — TUPLAS
# ==================================================

# filmes = ("Harry Potter e o Cálice de Fogo", "O Exorcista", "Obsessão", "O Iluminado", "Matrix")

# def menu():
#     print("1 - Mostrar filmes")
#     print("2 - Primeiro filme")
#     print("3 - Último filme")
#     print("4 - Quantidade de filmes")
#     print("0 - Sair")

# def mostrar_filmes(filmes):
#     for i in range (len(filmes)):
#         print(f"{i+1} - Filme: {filmes[i]}")

# def primeiro_filme(filmes):
#     print(f"Primeiro filme: {filmes[0]}")

# def ultimo_filme(filmes):
#     print(f"Último filme: {filmes[-1]}")

# def quantidade_filmes(filmes):
#     print(f"Quantidade: {len(filmes)}")
        

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("Selecione uma opção: "))
#             print()
#         except ValueError:
#             print("Insira um valor válido!")
#             continue 

#         match opcao:
#             case 1:
#                 mostrar_filmes(filmes)
#             case 2:
#                 primeiro_filme(filmes)
#             case 3:
#                 ultimo_filme(filmes)
#             case 4:
#                 quantidade_filmes(filmes)
#             case 0:
#                 print("Saindo do sistema...")
#                 break
# main()

# ==================================================
# QUESTÃO 27 — SETS
# ==================================================

# filmes = {"Harry Potter e a Pedra Filosofal", "A Múmia"}

# def menu():
#     print("1 - Adicionar filme")
#     print("2 - Remover filme")
#     print("3 - Mostrar filme")
#     print("4 - Verificar filme")
#     print("5 - Quantidade filmes")
#     print("0 - Sair")

# def add_filme(filmes):
#     f = str(input("Insira o nome do filme: "))
#     filmes.add(f)

#     print(f"{f} adicionado com sucesso!")
#     print()

# def remover_filme(filmes):
#     f = str(input("Insira o nome do filme: "))
#     if f in filmes:
#         filmes.remove(f)
#     else:
#         print("Este filme não existe!")

#     print(f"{f} removido com sucesso!")
#     print()

# def mostrar_filmes(filmes):
#     contador = 0
#     for filme in filmes:
#         contador += 1
#         print(f"{contador} - Filme: {filme}")
#     print()

# def verificar_filme(filmes):
#     f = str(input("Insira o nome do filme: "))
#     if f in filmes:
#         print("Este filme existe!")
#     else:
#         print("Este filme não existe!")
#     print()

# def quantidade_filmes(filmes):
#     print(f"Quantidade: {len(filmes)}")
#     print()

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("Insira a opção:"))
#             print()
#         except ValueError:
#             print("Insira um valor válido!")
#             continue    

#         match opcao:
#             case 1:
#                 add_filme(filmes)
#             case 2:
#                 remover_filme(filmes)
#             case 3:
#                 mostrar_filmes(filmes)
#             case 4:
#                 verificar_filme(filmes)
#             case 5:
#                 quantidade_filmes(filmes)
#             case 0: 
#                 print("Saindo do sistema...")
#                 break
# main()

# ==================================================
# QUESTÃO 28 — Dicionários
# ==================================================


# filme = {}

# def menu():
#     print("1 - Cadastrar filme")
#     print("2 - Mostrar informações")
#     print("3 - Alterar informações")
#     print("4 - Remover informações")
#     print("5 - Verificar informações")
#     print("0 - Sair")

# def cadastrar_filme(filme):
#     n = input("Digite o nome do filme: ")
#     a = input("Digite o ano de lançamento: ")
#     g = input("Digite o genero do filme: ")

#     filme['Nome'] = n
#     filme['Ano'] = a
#     filme['Gênero'] = g

# def mostrar_info(filme):
#     for chave, valor in filme.items():
#         print(f"- {chave}: {valor}")

# def alterar_info(filme):
#     while True:
#         novo_n = input("Deseja alterar o nome do filme? (S/N): ").upper()
#         if novo_n == "S":
#             novo_n = input("Digite o nome do filme: ")
#             filme['Nome'] = novo_n

#             print("Nome alterado com sucesso!")
#             print()

#         novo_a = input("Deseja alterar o ano do filme? (S/N): ").upper()
#         if novo_a == "S":
#             novo_a = input("Digite o ano de lançamento: ")
#             filme['Ano'] = novo_a

#             print("Ano de lançamento alterado com sucesso!")
#             print()

#         novo_g = input("Deseja alterar o gênero do filme? (S/N): ").upper()
#         if novo_g == "S":
#             novo_g = input("Digite o gênero do filme: ")
#             filme['Gênero'] = novo_g

#             print("Gênero alterado com sucesso!")
#             print()

#         continuar = input("Deseja continuar alterando? (S/N)").upper()
#         if continuar == "S":
#             continue
#         else:
#             break

# def remover_info(filme):
#     while True:
#             r_n = input("Deseja remover o nome do filme? (S/N): ").upper()
#             if r_n == "S":
#                 if 'Nome' in filme:
#                     del filme['Nome']
    
#                 print("Nome removido com sucesso!")
#                 print()
    
#             r_a = input("Deseja remover o ano do filme? (S/N): ").upper()
#             if r_a == "S":
#                 if 'Ano' in filme:
#                     del filme['Ano']
    
#                 print("Ano de lançamento removido com sucesso!")
#                 print()
    
#             r_g = input("Deseja remover o gênero do filme? (S/N): ").upper()
#             if r_g == "S":
#                 if 'Gênero' in filme:
#                     del filme['Gênero']
    
#                 print("Gênero removido com sucesso!")
#                 print()
    
#             continuar = input("Deseja remover algo a mais? (S/N)").upper()
#             if continuar == "S":
#                 continue
#             else:
#                 break

# def verificar_info(filme):
#     verificar = input("Digite a informação que deseja verificar:")
#     if verificar in filme:
#         print("Esta informação existe!")
#     else:
#         print("Esta informação não existe!")

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("Insira a opção: "))
#             print()
#         except ValueError:
#             print("Insira um valor válido!")
#             continue

#         match opcao:
#             case 1:
#                 cadastrar_filme(filme)
#             case 2:
#                 mostrar_info(filme)
#             case 3:
#                 alterar_info(filme)
#             case 4:
#                 remover_info(filme)
#             case 5:
#                 verificar_info(filme)
#             case 0:
#                 print("Encerrando o sistema...")
#                 break
# main()

# ==================================================
# QUESTÃO 29 — LISTA + DICIONARIOS
# ==================================================

# alunos = []

# def menu():
#     print("====================")
#     print("1 - Cadastrar aluno")
#     print("2 - Mostrar alunos")
#     print("3 - Calcular média (Notas)")
#     print("4 - Mostrar maior nota")
#     print("5 - Verificar aluno")
#     print("0 - Sair")
#     print("====================")


# def cadastrar_alunos(alunos):
#     aluno = {}

#     aluno["Nome"] = input("Nome: ")
#     aluno["Idade"] = int(input("Idade: "))
#     aluno["Nota"] = int(input("Nota: "))

#     alunos.append(aluno)

# def mostrar_alunos(alunos):
#     i = 0

#     for aluno in alunos:
#         i += 1
#         print(f"Aluno {i}: ")
#         for chave, valor in aluno.items():
#             print(f" - {chave}: {valor}")
#         print()

# def calcular_media(alunos):
#     soma = 0
#     quantidade = 0

#     for aluno in alunos:
#         soma += aluno["Nota"]
#         quantidade += 1

#     media = soma / quantidade

#     print(f"Média de notas: {media}")

# def maior_nota(alunos):
#     maior = 0

#     for aluno in alunos:
#         if aluno["Nota"] > maior:
#             maior = aluno["Nota"]

#     print(f"Maior nota: {maior}")

# def verificar_aluno(alunos):
#     nome = input("Digite o nome do aluno: ")

#     encontrado = False

#     for aluno in alunos:
#         if nome == aluno["Nome"]:
#             encontrado = True

#     if encontrado:
#         print("Este aluno está cadastrado!")
#     else:
#         print("Este aluno não está cadastrado!")

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("Insira a opção: "))
#             print()
#         except ValueError:
#             print("Insira um valor válido!")
#             continue

#         match opcao:
#             case 1:
#                 cadastrar_alunos(alunos)
#             case 2:
#                 mostrar_alunos(alunos)
#             case 3: 
#                 calcular_media(alunos)
#             case 4:
#                 maior_nota(alunos)
#             case 5:
#                 verificar_aluno(alunos)
#             case 0:
#                 print("Encerrando o sistema...")
#                 break
# main()

# ==================================================
# QUESTÃO 30 — Sistema de Produtos
# ==================================================

# produtos = []

# def menu():
#     print("==================")
#     print("1 - Cadastrar Produto")
#     print("2 - Mostrar Produto")
#     print("3 - Calcular valor total do estoque")
#     print("4 - Mostrar produto mais caro")
#     print("5 - Buscar produto")
#     print("6 - Remover Produto")
#     print("0 - Sair")
#     print("==================")

# def cadastrar_produto(produtos):
#     produto = {}

#     produto["Nome"] = input("Nome do produto: ")
#     produto["Preço"] = float(input("Preço do produto: R$"))
#     produto["Quantidade"] = int(input("Quantidade no estoque: "))

#     print("- Produto cadastrado com sucesso!")

#     produtos.append(produto)

# def mostrar_produto(produtos):
#     i = 0
#     for produto in produtos:
#         i += 1
#         print(f"Produto {i}:")
#         for chave, valor in produto.items():
#             print(f"- {chave}: {valor}")
#         print()

# def calcular_estoque(produtos):
#     total_produto = 0
#     valor_estoque = 0

#     for produto in produtos:
#         total_produto = produto["Preço"] * produto["Quantidade"]
#         valor_estoque += total_produto

#         print(f"- {produto['Nome']}: R${total_produto}")
#     print()

#     print(f"- Valor total do estoque: R${valor_estoque}")

# def mostrar_caro(produtos):
#     if len(produtos) > 0:
#         maior_valor = produtos[0]["Preço"]
#         produto_c = produtos[0]["Nome"]


#         for produto in produtos:
#             if produto["Preço"] > maior_valor:
#                  maior_valor = produto["Preço"]
#                  produto_c = produto["Nome"]

#         print(f"Produto mais caro: {produto_c} - {maior_valor}")
#     else:
#         print("Cadastre um produto primeiro!")


# def buscar_produto(produtos):
#     busca = input("Nome do produto que deseja buscar: ")
#     encontrado = False

#     for produto in produtos:
#         if busca == produto["Nome"]:
#             encontrado = True

#     if encontrado == True:
#         print("Produto encontrado com sucesso!")
#     else:
#         print("Produto não existente!")

# def remover_produto(produtos):
#     remover = input("Nome do produto que deseja remover: ")
#     encontrado = False

#     for produto in produtos:
#         if remover == produto["Nome"]:
#             encontrado = True

#             produtos.remove(produto)
#             print("Produto removido com sucesso!")

#     if encontrado == False:
#         print("Produto não existe ou ja fora deletado!")

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("- Insira a opção: "))
#             print()
#         except ValueError:
#             print("- Insira um valor válido!")
#             continue

#         match opcao:
#             case 1:
#                 cadastrar_produto(produtos)
#             case 2:
#                 mostrar_produto(produtos)
#             case 3:
#                 calcular_estoque(produtos)
#             case 4:
#                 mostrar_caro(produtos)
#             case 5:
#                 buscar_produto(produtos)
#             case 6:
#                 remover_produto(produtos)
#             case 0:
#                 print("Saindo do sistema...")
#                 break
# main()

# ==================================================
# QUESTÃO 31 — Sistema de Alunos
# ==================================================

# alunos = []

# def menu():
#     print()
#     print("====================")
#     print("1 - Cadastrar aluno")
#     print("2 - Mostrar alunos")
#     print("3 - Calcular média da turma")
#     print("4 - Mostrar maior nota")
#     print("5 - Mostrar menor nota")                
#     print("6 - Mostrar alunos aprovados")
#     print("7 - Buscar aluno")
#     print("8 - Remover aluno")
#     print("0 - Sair")
#     print("====================")
#     print()

# def cadastrar_aluno(alunos):
#     aluno = {}

#     aluno["Nome"] = input("Nome do aluno: ")
#     aluno["Idade"] = int(input("Idade do aluno: "))
#     aluno["Nota"] = float(input("Nota do aluno: "))

#     print("Aluno cadastrado com sucesso!")

#     alunos.append(aluno)

# def mostrar_aluno(alunos):
#     i = 0
#     for aluno in alunos:
#         i += 1
#         print(f"Aluno {i}:")
#         for chave, valor in aluno.items():
#             print(f"- {chave}: {valor}")
#         print()

# def calcular_media(alunos):

#     if len(alunos) > 0:
#         soma = 0
#         quantidade = 0

#         for aluno in alunos:
#             soma += aluno["Nota"]
#             quantidade += 1

#         media = soma / quantidade

#         print(f"A média das notas existentes é: {media}")
#     else:
#         print("Nenhum aluno cadastrado!")
#     print()

# def mostrar_maior(alunos):
#     if len(alunos) > 0:
#         maior_nota = alunos[0]["Nota"]
#         aluno_maior = alunos[0]["Nome"]

#         for aluno in alunos:
#             if aluno["Nota"] > maior_nota:
#                 maior_nota = aluno["Nota"]
#                 aluno_maior = aluno["Nome"]

#         print(f"O aluno {aluno_maior} possui a maior nota: {maior_nota}")
#         print()

# def mostrar_menor(alunos):
#     if len(alunos) > 0:
#         menor_nota = alunos[0]["Nota"]
#         aluno_menor = alunos[0]["Nome"]

#         for aluno in alunos:
#             if aluno["Nota"] < menor_nota:
#                 menor_nota = aluno["Nota"]
#                 aluno_menor = aluno["Nome"]

#         print(f"O aluno {aluno_menor} possui a menor nota: {menor_nota}")
#         print()

# def mostrar_aprovados(alunos):
#     reprovado = True

#     for aluno in alunos:
#         if aluno["Nota"] >= 6:
#             print(f"{aluno['Nome']}: APROVADO ({aluno['Nota']})")
#             reprovado = False

#     if reprovado:
#         print("Nenhum aluno aprovado!")
#     print()

# def buscar_alunos(alunos):
#     nome = input("Digite o nome do aluno que queira buscar: ")
#     encontrado = False

#     for aluno in alunos:
#         if nome == aluno["Nome"]:
#             encontrado = True
#             aluno_encontrado = aluno["Nome"]

#     if encontrado:
#         print(f"O aluno {aluno_encontrado} está cadastrado!")
#     else:
#         print("Nenhum aluno com este nome foi encontrado!")
#     print()

# def remover_aluno(alunos):
#     nome = input("Digite o nome do aluno que queira remover: ")
#     encontrado = False

#     for aluno in alunos:
#         if nome == aluno["Nome"]:
#             encontrado = True

#             alunos.remove(aluno)
#             print(f"O aluno foi removido com sucesso!")

#     if encontrado == False:
#         print("Nenhum aluno com este nome foi encontrado!")
#     print()

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("Insira uma opção: "))
#             print()
#         except ValueError:
#             print("Insira um valor válido!")
#             continue

#         match opcao:
#             case 1:
#                 cadastrar_aluno(alunos)
#             case 2:
#                 mostrar_aluno(alunos)
#             case 3:
#                 calcular_media(alunos)
#             case 4:
#                 mostrar_maior(alunos)
#             case 5:
#                 mostrar_menor(alunos)
#             case 6:
#                 mostrar_aprovados(alunos)
#             case 7:
#                 buscar_alunos(alunos)
#             case 8:
#                 remover_aluno(alunos)
#             case 0: 
#                 print("Encerrando o sistema...")
#                 break
# main()

# ==================================================
# QUESTÃO 32 — Sistema de Produtos
# ==================================================

# produtos = []

# def menu():
#     print()
#     print("===========================")
#     print("1 - Cadastrar produto")
#     print("2 - Mostrar produtos")
#     print("3 - Buscar por categoria")
#     print("4 - Calcular valor total do estoque")
#     print("5 - Mostrar produto mais caro")
#     print("6 - Mostrar produtos com estoque mais baixo")
#     print("7 - Remover produto")
#     print("0 - Sair")
#     print("===========================")
#     print()

# def cadastrar_produtos(produtos):
#     produto = {}

#     produto["Nome"] = input("Nome do produto: ")
#     produto["Preço"] = float(input("Preço do produto: "))
#     produto["Categoria"] = input("Categoria do produto: ")
#     produto["Quantidade"] = int(input("Quantidade do produto:"))

#     print("Produto cadastrado com sucesso!")

#     produtos.append(produto)

# def mostrar_produtos(produtos):
#     if len(produtos) > 0:
#         i = 0

#         for produto in produtos:
#             i += 1
#             print(f"Produto {i}:")
#             for chave, valor in produto.items():
#                 print(f"- {chave}: {valor}")
#     else:
#         print("Nenhum produto cadastrado!")

# def buscar_categoria(produtos):
#     if len(produtos) > 0:
#         busca = input("Digite a categoria do produto: ")
#         encontrado = False

#         for produto in produtos:
#             if busca == produto["Categoria"]:
#                 encontrado = True
#                 print(f"{busca}: ")
#                 for chave, valor in produto.items():
#                     print(f"- {chave}: {valor}")
        
#         if encontrado == False:
#             print("Categoria não encontrada!")
#     else:
#         print("Nenhum produto cadastrado!")

# def calcular_estoque(produtos):
#     if len(produtos) > 0:
#         valor_estoque = 0
#         valor_total = 0

#         for produto in produtos:
#             valor_estoque = produto["Preço"] * produto["Quantidade"]
#             valor_total += valor_estoque

#         print(f"Valor total do estoque: {valor_total}")
#     else:
#         print("Nenhum produto cadastrado!")

# def mostrar_caro(produtos):
#     if len(produtos) > 0:
#         maior = produtos[0]["Preço"]
#         produto_c = produtos[0]["Nome"]

#         for produto in produtos:
#             if produto["Preço"] > maior:
#                 maior = produto["Preço"]
#                 produto_c = produto["Nome"]

#         print(f"Produto mais caro: {produto_c} (R${maior}")
#     else:
#         print("Nenhum produto cadastrado!")

# def estoque_baixo(produtos):
#     if len(produtos) > 0:
#         encontrado = False

#         for produto in produtos:
#             if produto["Quantidade"] <= 5:
#                 encontrado = True
#                 print("Baixo estoque:")
#                 print(f"- {produto["Nome"]}: {produto['Quantidade']}")

#         if encontrado == False:
#             print("Nenhum produto possui estoque baixo!")
#     else:
#         print("Nenhum produto cadastrado!")

# def remover_produto(produtos):
#     if len(produtos) > 0:
#         b = input("Nome do produto: ")
#         encontrado = False

#         for produto in produtos:
#             if b == produto["Nome"]:
#                 encontrado = True

#                 produtos.remove(produto)
#                 print("Produto removido com sucesso!")

#                 break

#         if encontrado == False:
#             print("Nenhum produto com esse nome foi encontrado!")
#     else:
#         print("Nenhum produto cadastrado!")

# def main():
#     while True:
#         menu()
#         try:
#             opcao = int(input("Insira uma opção: "))
#         except ValueError:
#             print("Insira um valor válido!")
#             continue

#         match opcao:
#             case 1:
#                 cadastrar_produtos(produtos)
#             case 2:
#                 mostrar_produtos(produtos)
#             case 3:
#                 buscar_categoria(produtos)
#             case 4:
#                 calcular_estoque(produtos)
#             case 5:
#                 mostrar_caro(produtos)
#             case 6:
#                 estoque_baixo(produtos)
#             case 7:
#                 remover_produto(produtos)
#             case 0:
#                 print("Encerrando sistema...")
#                 break
# main()

 # ==================================================
# QUESTÃO 33 — Sistema de Vendas
# ==================================================

vendas = []

def menu():
    print()
    print("======================")
    print("1 - Registrar venda")
    print("2 - Mostrar vendas")
    print("3 - Calcular faturamento")
    print("4 - Mostrar produto mais vendido")
    print("5 - Mostrar categoria com maior faturamento")
    print("6 - Buscar vendas por produto")
    print("7 - Cancelar venda")
    print("0 - Sair")
    print("======================")
    print()

def registrar_venda(vendas):
    venda = {}

    venda["Produto"] = input("Nome do produto: ")
    venda["Categoria"] = input("Categoria do produto: ")
    venda["Preço"] = float(input("Valor do produto:"))
    venda["Quantidade"] = int(input("Quantidade vendida: ")) 

    vendas.append(venda)

def mostrar_vendas(vendas):
    if len(vendas) > 0:
        i = 0
        for venda in vendas:
            i += 1
            print(f"Venda {i}: ")
            for chave, valor in venda.items():
                print(f"- {chave}: {valor}")
    else:
        print("Nenhuma venda registrada!")

def calcular_faturamento(vendas):
    if len(vendas) > 0:
        faturamento_venda = 0
        valor_total = 0

        for venda in vendas:
            faturamento_venda = venda["Preço"] * venda["Quantidade"]
            valor_total += faturamento_venda

            print(f"{venda['Produto']} = R${venda['Preço']} x {venda['Quantidade']} = {faturamento_venda}")
        print(f"- Faturamento total: {valor_total}")
    else:
        print("Nenhuma venda registrada!")    

def mais_vendido(vendas):
    if len(vendas) > 0:
        mais_v = vendas[0]["Quantidade"]
        produto_mais_v = vendas[0]["Produto"]

        for venda in vendas:
            if venda["Quantidade"] > mais_v:
                mais_v = venda["Quantidade"]
                produto_mais_v = venda["Produto"]
        print(f"O produto {produto_mais_v} foi o mais vendido, com {mais_v} vendas!")
    else:
        print("Nenhuma venda registrada!") 

def categoria_faturamento(vendas):
    if len(vendas) > 0:
        faturamento_categorias = {}
        valor_venda = 0
        
        for venda in vendas:
            categoria = venda["Categoria"]
            valor_venda = venda["Preço"] * venda["Quantidade"]
            if categoria not in faturamento_categorias:
                faturamento_categorias[categoria] = valor_venda
            else:
                faturamento_categorias[categoria] += valor_venda

        chave, valor = list(faturamento_categorias.items())[0]

        maior = valor
        nome_categoria = chave

        for chave, valor in faturamento_categorias.items():
            if valor > maior:
                maior = valor
                nome_categoria = chave

        print(f"Categoria com maior faturamento: {nome_categoria} que faturou R${maior}")

    else:
        print("Nenhuma venda registrada!") 

def buscar_vendas(vendas):
    if len(vendas) > 0:
        busca = input("Nome do produto: ")
        encontrado = False

        for venda in vendas:
            if busca == venda["Produto"]:
                encontrado = True
                print(venda)

        if not encontrado:
            print("Produto não encontrado!")
    else:
        print("Nenhuma venda registrada!")          

def cancelar_venda(vendas):
    if len(vendas) > 0:
        busca = input("Nome do produto: ")
        encontrado = False

        for venda in vendas:
            if busca == venda["Produto"]:
                encontrado = True

                vendas.remove(venda)
                print("Venda cancelada com sucesso!")

                break

        if not encontrado:
            print("Produto não encontrado!")
    else:
        print("Nenhuma venda registrada!")

def main():
    while True:
        menu()
        try:
            opcao = int(input("Insira uma opção: "))
        except ValueError:
            print("Insira um valor válido!")
            continue

        match opcao:
            case 1:
                registrar_venda(vendas)
            case 2:
                mostrar_vendas(vendas)
            case 3:
                calcular_faturamento(vendas)
            case 4:
                mais_vendido(vendas)
            case 5:
                categoria_faturamento(vendas)
            case 6:
                buscar_vendas(vendas)
            case 7:
                cancelar_venda(vendas)
            case 0:
                print("Encerrando sistema...")
                break
main()
