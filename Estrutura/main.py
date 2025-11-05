from catalog_manager import CatalogManager

def menu():
    print("\n📚 GERENCIADOR DE CATÁLOGO DE LIVROS 📚")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Sair")

def main():
    catalog = CatalogManager()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            genero = input("Gênero: ")
            catalog.adicionar_livro(titulo, autor, ano, genero)

        elif opcao == '2':
            catalog.listar_livros()

        elif opcao == '3':
            termo = input("Digite o termo de busca: ")
            catalog.buscar_livro(termo)

        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
