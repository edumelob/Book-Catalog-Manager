from collections import namedtuple
import os

# Criamos o namedtuple que representará um livro
Book = namedtuple('Book', ['titulo', 'autor', 'ano', 'genero'])

class CatalogManager:
    def __init__(self, data_file='data/books.txt'):
        self.data_file = data_file
        self.books = []
        self._load_books()

    def _load_books(self):
        """Carrega os livros do arquivo, se existir."""
        if not os.path.exists(self.data_file):
            return
        with open(self.data_file, 'r', encoding='utf-8') as f:
            for line in f:
                titulo, autor, ano, genero = line.strip().split(';')
                self.books.append(Book(titulo, autor, int(ano), genero))

    def _save_books(self):
        """Salva os livros no arquivo."""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            for b in self.books:
                f.write(f"{b.titulo};{b.autor};{b.ano};{b.genero}\n")

    def adicionar_livro(self, titulo, autor, ano, genero):
        """Adiciona um novo livro ao catálogo."""
        novo_livro = Book(titulo, autor, ano, genero)
        self.books.append(novo_livro)
        self._save_books()
        print(f"✅ Livro '{titulo}' adicionado com sucesso!")

    def listar_livros(self):
        """Lista todos os livros do catálogo."""
        if not self.books:
            print("Nenhum livro cadastrado ainda.")
            return
        for i, b in enumerate(self.books, start=1):
            print(f"{i}. {b.titulo} ({b.ano}) - {b.autor} [{b.genero}]")

    def buscar_livro(self, termo):
        """Busca livros pelo título."""
        resultados = [b for b in self.books if termo.lower() in b.titulo.lower()]
        if resultados:
            print(f"🔍 Livros encontrados com '{termo}':")
            for b in resultados:
                print(f" - {b.titulo} ({b.ano}) - {b.autor}")
        else:
            print(f"Nenhum livro encontrado com o termo '{termo}'.")
