
caminho_biblia = '/Bible-CLI/biblia.txt'

with open(caminho_biblia, 'r', encoding='utf-8') as arquivo_biblia:
    biblia = arquivo_biblia.readlines()

titulo = ''.join(biblia[:3]).strip()

antigo_testamento = biblia[6:24116]
novo_testamento = biblia[24118:]
nomes_livros = []
linhas_livros = []

def imprimir(texto):
    for linha in texto:
        print(linha.strip())

linhas_livro = []
for indice, linha in enumerate(antigo_testamento):
    if linha[0].isalpha() and linha[0] != ' ':
        if linhas_livro is not None:
            linhas_livros.append(linhas_livro)
        nomes_livros.append(linha.strip())
        linhas_livro = []
        continue
    linhas_livro.append(linha.strip())

for indice, linha in enumerate(novo_testamento):
    if linha[0].isalpha() and linha[0] != ' ':
        if linhas_livro is not None:
            linhas_livros.append(linhas_livro)
        nomes_livros.append(linha.strip())
        linhas_livro = []
        continue
    linhas_livro.append(linha.strip())
    
livros = dict(zip(nomes_livros, linhas_livros))

# for chave, valor in livros.items():
    # print(chave)
