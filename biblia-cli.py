
caminho_biblia = '/Bible-CLI/biblia.txt'

with open(caminho_biblia, 'r', encoding='utf-8') as arquivo_biblia:
    biblia_txt = arquivo_biblia.readlines()

titulo = ''.join(biblia_txt[:3]).strip()

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
    '2SM ': ('II SAMUEL', biblia[8297:9017]),
    '1RE': ('I REIS', biblia[9017:9856]),
    '2RE': ('II REIS', biblia[9856:10601]),
    '1CR': ('I CRÔNICAS', biblia[10601:11573]),
    '2CR': ('II CRÔNICAS', biblia[11573:12432]),
    'ESD': ('ESDRAS', biblia[12432:12723]),
    'NEE': ('NEEMIAS', biblia[12723:13142]),
    'EST': ('ESTER', biblia[13142:13319]),
    'JO': ('JÓ', biblia[13319:14432]),
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

def imprimir(texto):
    if type(texto) == 'list':
        for linha in texto:
            print(linha.strip())
    else:
        print(texto)

def solicitar_entrada():
    return input('>>> ').split(' ')

entrada = solicitar_entrada()
capitulo = 3
verso = 16

if entrada[0]:
    livro_escolhido = biblia.get(entrada[0])
    
if len(entrada) == 2:
    capitulo = int(entrada[1])

if len(entrada) == 3:
    verso = int(entrada[2])

nome_livro = livro_escolhido[0]
texto_livro = livro_escolhido[1]

livro = []
versos = []
for linha in texto_livro:
    if linha[0].isalpha() and linha[0] != ' ':
        continue
    if linha[0] == ' ':
        if versos:
            livro.append(versos)
        versos = []
        continue
    versos.append(linha)

print(nome_livro)
print(livro[capitulo - 1][verso - 1])


