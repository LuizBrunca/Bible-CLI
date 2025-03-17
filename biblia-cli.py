import os
from unicodedata import normalize, category

caminho_biblia = '/Bible-CLI/biblia.txt'

with open(caminho_biblia, 'r', encoding='utf-8') as arquivo_biblia:
    biblia_txt = arquivo_biblia.readlines()

biblia = biblia_txt[6:]

def ler_biblia_em_livros_capitulos_e_versos(biblia):
    livros = []
    livro_atual = None
    capitulo_atual = []

    for linha in biblia:
        linha = linha.rstrip()
        
        if not linha or linha == 'NOVO TESTAMENTO':
            continue

        if linha[0].isalpha():
            if livro_atual is not None:
                if capitulo_atual:
                    livro_atual.append(capitulo_atual)
                livros.append(livro_atual)

            livro_atual = []
            capitulo_atual = []
            
        elif linha.startswith(' '):
            if capitulo_atual:
                livro_atual.append(capitulo_atual)
            capitulo_atual = []
        
        elif linha[0].isdigit():
            capitulo_atual.append(linha.strip())

    if capitulo_atual:
        livro_atual.append(capitulo_atual)
    if livro_atual:
        livros.append(livro_atual)
        
    return livros

def normalizar_texto(texto):
    texto_normalizado = normalize('NFD', texto)
    texto_normalizado = ''.join(c for c in texto_normalizado if category(c) != 'Mn')
    return texto_normalizado.lower()

def print_orientacao():
    print('''
ORIENTAÇÕES:
- PARA UM LIVRO INTEIRO, DIGITE:    LIVRO
- PARA UM CAPÍTULO INTEIRO, DIGITE: LIVRO CAPÍTULO
- PARA UM VERSO, DIGITE:            LIVRO CAPÍTULO:VERSO
- PARA VÁRIOS VERSOS, DIGITE:       LIVRO CAPÍTULO:VERSO-VERSO
- PARA PESQUISAR, DIGITE:           /PESQUISA
                                    LIVRO /PESQUISA
                                    LIVRO CAPÍTULO /PESQUISA''')

def print_titulo():
    print()
    print(''.join(biblia_txt[:3]).strip())

def print_livros():
    livros = '''
LIVROS:
[GEN] - GÊNESIS                [ISA] - ISAÍAS                     [ROM] - ROMANOS
[EXO] - ÊXODO                  [JER] - JEREMIAS                   [1CO] - I CORÍNTIOS
[LEV] - LEVÍTICO               [LAM] - LAMENTAÇÕES DE JEREMIAS    [2CO] - II CORÍNTIOS
[NUM] - NÚMEROS                [EZE] - EZEQUIEL                   [GAL] - GÁLATAS
[DEU] - DEUTERONÔMIO           [DAN] - DANIEL                     [EFE] - EFÉSIOS
[JOS] - JOSUÉ                  [OSE] - OSÉIAS                     [FIL] - FILIPENSES
[JUI] - JUÍZES                 [JOE] - JOEL                       [COL] - COLOSSENSES
[RUT] - RUTE                   [AMO] - AMÓS                       [1TE] - I TESSALONICENSES
[1SM] - I SAMUEL               [OBA] - OBADIAS                    [2TE] - II TESSALONICENSES
[2SM] - II SAMUEL              [JON] - JONAS                      [1TI] - I TIMÓTEO
[1RE] - I REIS                 [MIQ] - MIQUÉIAS                   [2TI] - II TIMÓTEO
[2RE] - II REIS                [NAU] - NAUM                       [TIT] - TITO
[1CR] - I CRÔNICAS             [HAB] - HABACUQUE                  [FLM] - FILEMOM
[2CR] - II CRÔNICAS            [SOF] - SOFONIAS                   [HEB] - HEBREUS
[ESD] - ESDRAS                 [AGE] - AGEU                       [TIA] - TIAGO
[NEE] - NEEMIAS                [ZAC] - ZACARIAS                   [1PE] - I PEDRO
[EST] - ESTER                  [MAL] - MALAQUIAS                  [2PE] - II PEDRO
[JO ] - JÓ                     [MAT] - MATEUS                     [1JO] - I JOÃO
[SAL] - SALMOS                 [MAR] - MARCOS                     [2JO] - II JOÃO
[PRO] - PROVÉRBIOS             [LUC] - LUCAS                      [3JO] - III JOÃO
[ECL] - ECLESIASTES            [JOA] - JOÃO                       [JUD] - JUDAS
[CAN] - CANTARES DE SALOMÃO    [ATO] - ATOS DOS APÓSTOLOS         [APO] - APOCALIPSE'''
    print(livros)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def solicitar_entrada():
    while True:
        print()
        entrada = input('SUA CONSULTA: ').strip()
        return entrada

livro_lendo = None
capitulo_lendo = None
biblia = ler_biblia_em_livros_capitulos_e_versos(biblia)
livros = {
    'GEN': (0, 'GÊNESIS'),
    'EXO': (1, 'ÊXODO'),
    'LEV': (2, 'LEVÍTICO'),
    'NUM': (3, 'NÚMEROS'),
    'DEU': (4, 'DEUTERONÔMIO'),
    'JOS': (5, 'JOSUÉ'),
    'JUI': (6, 'JUÍZES'),
    'RUT': (7, 'RUTE'),
    '1SM': (8, 'I SAMUEL'),
    '2SM': (9, 'II SAMUEL'),
    '1RE': (10, 'I REIS'),
    '2RE': (11, 'II REIS'),
    '1CR': (12, 'I CRÔNICAS'),
    '2CR': (13, 'II CRÔNICAS'),
    'ESD': (14, 'ESDRAS'),
    'NEE': (15, 'NEEMIAS'),
    'EST': (16, 'ESTER'),
    'JO ': (17, 'JÓ'),
    'SAL': (18, 'SALMOS'),
    'PRO': (19, 'PROVÉRBIOS'),
    'ECL': (20, 'ECLESIASTES'),
    'CAN': (21, 'CANTARES DE SALOMÃO'),    
    'ISA': (22, 'ISAÍAS'),
    'JER': (23, 'JEREMIAS'),
    'LAM': (24, 'LAMENTAÇÕES DE JEREMIAS'),
    'EZE': (25, 'EZEQUIEL'),
    'DAN': (26, 'DANIEL'),
    'OSE': (27, 'OSÉIAS'),
    'JOE': (28, 'JOEL'),
    'AMO': (29, 'AMÓS'),
    'OBA': (30, 'OBADIAS'),
    'JON': (31, 'JONAS'),
    'MIQ': (32, 'MIQUÉIAS'),
    'NAU': (33, 'NAUM'),
    'HAB': (34, 'HABACUQUE'),
    'SOF': (35, 'SOFONIAS'),
    'AGE': (36, 'AGEU'),
    'ZAC': (37, 'ZACARIAS'),
    'MAL': (38, 'MALAQUIAS'),
    'MAT': (39, 'MATEUS'),
    'MAR': (40, 'MARCOS'),
    'LUC': (41, 'LUCAS'),
    'JOA': (42, 'JOÃO'),
    'ATO': (43, 'ATOS DOS APÓSTOLOS'),     
    'ROM': (44, 'ROMANOS'),
    '1CO': (45, 'I CORÍNTIOS'),
    '2CO': (46, 'II CORÍNTIOS'),
    'GAL': (47, 'GÁLATAS'),
    'EFE': (48, 'EFÉSIOS'),
    'FIL': (49, 'FILIPENSES'),
    'COL': (50, 'COLOSSENSES'),
    '1TE': (51, 'I TESSALONICENSES'),
    '2TE': (52, 'II TESSALONICENSES'),
    '1TI': (53, 'I TIMÓTEO'),
    '2TI': (54, 'II TIMÓTEO'),
    'TIT': (55, 'TITO'),
    'FLM': (56, 'FILEMOM'),
    'HEB': (57, 'HEBREUS'),
    'TIA': (58, 'TIAGO'),
    '1PE': (59, 'I PEDRO'),
    '2PE': (60, 'II PEDRO'),
    '1JO': (61, 'I JOÃO'),
    '2JO': (62, 'II JOÃO'),
    '3JO': (63, 'III JOÃO'),
    'JUD': (64, 'JUDAS'),
    'APO': (65, 'APOCALIPSE')
}
    
def main():
    while True:
        try:
            entrada = solicitar_entrada()
            
            global livro_lendo
            global capitulo_lendo
            
            if entrada == 'a':
                if livro_lendo is None and capitulo_lendo is None:
                    livro_lendo = 0
                    capitulo_lendo = 1
                    
                    limpar_tela()
                    nome_livro = next(nome for _, (num, nome) in livros.items() if num == livro_lendo)
                    print(f'{nome_livro} {capitulo_lendo}')
                    for verso in biblia[livro_lendo][capitulo_lendo - 1]:
                        print(verso.strip())
                    continue
                    
                if capitulo_lendo - 1 == 0:
                    if livro_lendo - 1 < 0:
                        livro_lendo = 65
                    else:
                        livro_lendo -= 1
                    capitulo_lendo = len(biblia[livro_lendo])
                    
                else:
                    capitulo_lendo -= 1
                
                limpar_tela()
                nome_livro = next(nome for _, (num, nome) in livros.items() if num == livro_lendo)
                print(f'{nome_livro} {capitulo_lendo}')
                for verso in biblia[livro_lendo][capitulo_lendo - 1]:
                    print(verso.strip())
                continue
            
            if entrada == 'p':
                if livro_lendo is None and capitulo_lendo is None:
                    livro_lendo = 0
                    capitulo_lendo = 1
                    
                    limpar_tela()
                    nome_livro = next(nome for _, (num, nome) in livros.items() if num == livro_lendo)
                    print(f'{nome_livro} {capitulo_lendo}')
                    for verso in biblia[livro_lendo][capitulo_lendo - 1]:
                        print(verso.strip())
                    continue
                
                livro = biblia[livro_lendo]
                if capitulo_lendo + 1 > len(livro):
                    if livro_lendo + 1 == 66:
                        livro_lendo = 0
                    else:
                        livro_lendo += 1
                    capitulo_lendo = 1
                else:
                    capitulo_lendo += 1
                
                limpar_tela()
                nome_livro = next(nome for _, (num, nome) in livros.items() if num == livro_lendo)
                print(f'{nome_livro} {capitulo_lendo}')
                for verso in biblia[livro_lendo][capitulo_lendo - 1]:
                    print(verso.strip())
                continue

            if entrada.lower().startswith('ajuda'):
                limpar_tela()
                print_titulo()
                print_livros()
                print_orientacao()
                return main()

            if entrada.startswith('sair'):
                limpar_tela()
                break

            dados = entrada.split(' ')
            limpar_tela()

            if '/' in dados[0]:
                livro_lendo = 0
                capitulo_lendo = 1
                pesquisa = ' '.join(dados[0:]).replace('/', '')
                resultados = []
                for verso in biblia_txt:
                    if verso[0] == ' ':
                        capitulo = verso.strip()
                    if normalizar_texto(pesquisa) in normalizar_texto(verso):
                        resultados.append(f'{capitulo}\n{verso}')
                
                if not resultados:
                    print(f'Nenhum resultado encontrado para a pesquisa por "{pesquisa}"...')
                    continue

                for resultado in resultados:
                    print(resultado.strip())
                continue
            
            dados_livro = livros.get(dados[0], None)
            if not dados_livro:
                raise
            
            nome_livro = dados_livro[1]
            livro = biblia[dados_livro[0]]
            livro_lendo = dados_livro[0]

            if len(dados) == 1:
                print(nome_livro)
                for indice, capitulo in enumerate(livro):
                    print(f'\n{nome_livro} {indice + 1}')
                    for verso in capitulo:
                        print(verso.strip())
                continue

            if '/' in dados[1]:
                livro_lendo = 0
                capitulo_lendo = 1
                pesquisa = ' '.join(dados[1:]).replace('/', '')
                resultados = []

                for indice, capitulo in enumerate(livro):
                    for verso in capitulo:
                        if normalizar_texto(pesquisa) in normalizar_texto(verso):
                            resultados.append(f'{nome_livro} {indice + 1}\n{verso}')
                
                if not resultados:
                    print(f'Nenhum resultado encontrado para a pesquisa por "{pesquisa}"...')
                    continue

                for resultado in resultados:
                    print(resultado.strip())
                continue

            if len(dados) == 2:
                capitulo_versos = dados[1].split(':')
                capitulo = int(capitulo_versos[0])
                capitulo_lendo = capitulo

                if len(capitulo_versos) == 1:
                    print(f'{nome_livro} {capitulo}')
                    for verso in livro[capitulo - 1]:
                        print(verso.strip())
                    continue

                if len(capitulo_versos) > 1:
                    versos = capitulo_versos[1]
                    if '-' in versos:
                        versos = versos.split('-')
                        verso_inicial = int(versos[0])
                        if versos[1]:
                            verso_final = int(versos[1])
                            texto = livro[capitulo - 1][verso_inicial - 1:verso_final]
                        else:
                            texto = livro[capitulo - 1][verso_inicial - 1:]
                    else:
                        texto = livro[capitulo - 1][int(versos) - 1]
                    print(f'{nome_livro} {capitulo}')
                    if isinstance(texto, list):
                        for verso in texto:
                            print(verso.strip())
                    else:
                        print(texto.strip())
                    continue

            if '/' in dados[2]:
                livro_lendo = 0
                capitulo_lendo = 1
                
                if ':' in dados[1]:
                    raise
                pesquisa = ' '.join(dados[2:]).replace('/', '')
                resultados = []
                capitulo = int(dados[1])

                for verso in livro[capitulo - 1]:
                    if normalizar_texto(pesquisa) in normalizar_texto(verso):
                        resultados.append(verso)
                
                if not resultados:
                    print(f'Nenhum resultado encontrado para a pesquisa por "{pesquisa}"...')
                    continue
                
                print(f'{nome_livro} {capitulo}')
                for resultado in resultados:
                    print(resultado.strip())
                continue
        except Exception as ex:
            limpar_tela()
            print(ex)
            print('SUA CONSULTA NÃO FUNCIONOU...')
            print_orientacao()
            return main()

if __name__ == '__main__':
    limpar_tela()
    print_titulo()
    print_livros()
    print_orientacao()
    main()
