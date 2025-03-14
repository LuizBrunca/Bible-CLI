
caminho_biblia = '/Biblia-CLI/biblia.txt'

with open(caminho_biblia, 'r', encoding='utf-8') as arquivo_biblia:
    biblia = arquivo_biblia.readlines()

titulo = ''.join(biblia[:3]).strip()
print(titulo)