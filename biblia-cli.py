from os import system
from unicodedata import normalize, category

caminho_biblia = '/Bible-CLI/biblia.txt'

with open(caminho_biblia, 'r', encoding='utf-8') as arquivo_biblia:
    biblia_txt = arquivo_biblia.readlines()

biblia = biblia_txt[6:]

biblia = {
    'GEN': ('GÊNESIS', biblia[0:1582]),
    'EXO': ('ÊXODO', biblia[1582:2836]),
    'LEV': ('LEVÍTICO', biblia[2836:3723]),
    'NUM': ('NÚMEROS', biblia[3723:5046]),
    'DEU': ('DEUTERONÔMIO', biblia[5046:6040]),
    'JOS': ('JOSUÉ', biblia[6040:6723]),
    'JUI': ('JUÍZES', biblia[6723:7364]),
    'RUT': ('RUTE', biblia[7364:7454]),
    '1SM': ('I SAMUEL', biblia[7454:8297]),
    '2SM': ('II SAMUEL', biblia[8297:9017]),
    '1RE': ('I REIS', biblia[9017:9856]),
    '2RE': ('II REIS', biblia[9856:10601]),
    '1CR': ('I CRÔNICAS', biblia[10601:11573]),
    '2CR': ('II CRÔNICAS', biblia[11573:12432]),
    'ESD': ('ESDRAS', biblia[12432:12723]),
    'NEE': ('NEEMIAS', biblia[12723:13142]),
    'EST': ('ESTER', biblia[13142:13319]),
    'JO ': ('JÓ', biblia[13319:14432]),
    'SAL': ('SALMOS', biblia[14432:17044]),
    'PRO': ('PROVÉRBIOS', biblia[17044:17991]),
    'ECL': ('ECLESIASTES', biblia[17991:18226]),
    'CAN': ('CANTARES DE SALOMÃO', biblia[18226:18352]),
    'ISA': ('ISAÍAS', biblia[18352:19711]),
    'JER': ('JEREMIAS', biblia[19711:21128]),
    'LAM': ('LAMENTAÇÕES DE JEREMIAS', biblia[21128:21288]),
    'EZE': ('EZEQUIEL', biblia[21288:22609]),
    'DAN': ('DANIEL', biblia[22609:22979]),
    'OSE': ('OSÉIAS', biblia[22979:23191]),
    'JOE': ('JOEL', biblia[23191:23268]),
    'AMO': ('AMÓS', biblia[23268:23424]),
    'OBA': ('OBADIAS', biblia[23424:23447]),
    'JON': ('JONAS', biblia[23447:23500]),
    'MIQ': ('MIQUÉIAS', biblia[23500:23613]),
    'NAU': ('NAUM', biblia[23613:23664]),
    'HAB': ('HABACUQUE', biblia[23664:23724]),
    'SOF': ('SOFONIAS', biblia[23724:23781]),
    'AGE': ('AGEU', biblia[23781:23822]),
    'ZAC': ('ZACARIAS', biblia[23822:24048]),
    'MAL': ('MALAQUIAS', biblia[24048:24109]),
    'MAT': ('MATEUS', biblia[24111:25211]),
    'MAR': ('MARCOS', biblia[25211:25906]),
    'LUC': ('LUCAS', biblia[25906:27080]),
    'JOA': ('JOÃO', biblia[27080:27981]),
    'ATO': ('ATOS DOS APÓSTOLOS', biblia[27981:29017]),
    'ROM': ('ROMANOS', biblia[29017:29467]),
    '1CO': ('I CORÍNTIOS', biblia[29467:29921]),
    '2CO': ('II CORÍNTIOS', biblia[29921:30191]),
    'GAL': ('GÁLATAS', biblia[30191:30347]),
    'EFE': ('EFÉSIOS', biblia[30347:30509]),
    'FIL': ('FILIPENSES', biblia[30509:30618]),
    'COL': ('COLOSSENSES', biblia[30618:30718]),
    '1TE': ('I TESSALONICENSES', biblia[30718:30813]),
    '2TE': ('II TESSALONICENSES', biblia[30813:30864]),
    '1TI': ('I TIMÓTEO', biblia[30864:30985]),
    '2TI': ('II TIMÓTEO', biblia[30985:31073]),        
    'TIT': ('TITO', biblia[31073:31123]),
    'FLM': ('FILEMOM', biblia[31123:31150]),
    'HEB': ('HEBREUS', biblia[31150:31467]),
    'TIA': ('TIAGO', biblia[31467:31581]),
    '1PE': ('I PEDRO', biblia[31581:31693]),
    '2PE': ('II PEDRO', biblia[31693:31758]),
    '1JO': ('I JOÃO', biblia[31758:31869]),
    '2JO': ('II JOÃO', biblia[31869:31884]),
    '3JO': ('III JOÃO', biblia[31884:31901]),
    'JUD': ('JUDAS', biblia[31901:31928]),
    'APO' : ('APOCALIPSE', biblia[31928:])
}

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

def solicitar_entrada():
    while True:
        print()
        entrada = input('SUA CONSULTA: ').strip()
        return entrada

def ler_livro(texto_livro):
    livro = []
    _versos = []
    for linha in texto_livro:
        if linha[0].isalpha() and linha[0] != ' ':
            continue
        if linha[0] == ' ':
            if _versos:
                livro.append(_versos)
            _versos = []
            continue
        _versos.append(linha)
    return livro
        
def main():
    while True:
        try:
            entrada = solicitar_entrada()

            if entrada.startswith('ajuda'):
                system('cls')
                print_titulo()
                print_livros()
                print_orientacao()
                return main()

            if entrada.startswith('sair'):
                break

            dados = entrada.split(' ')
            system('cls')

            if '/' in dados[0]:
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
            
            livro = biblia.get(dados[0])
            nome_livro = livro[0]
            texto_livro = livro[1]
            livro = ler_livro(texto_livro)

            if len(dados) == 1:
                print(nome_livro)
                for indice, capitulo in enumerate(livro):
                    print(f'\n{nome_livro} {indice + 1}')
                    for verso in capitulo:
                        print(verso.strip())
                continue

            if '/' in dados[1]:
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
            system('cls')
            print('SUA CONSULTA NÃO FUNCIONOU...')
            print_orientacao()
            main()

if __name__ == '__main__':
    system('cls')
    print_titulo()
    print_livros()
    print_orientacao()
    main()