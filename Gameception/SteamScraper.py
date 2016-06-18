#!/usr/bin/env python

import urllib.request
import re
from bs4 import BeautifulSoup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gameception.settings')
import django, random
django.setup()
from Assinante.models import Jogo, Genero

def add_genero(nome):
    try:
        g = Genero.objects.get(nome=nome)   # Verifica se o genero já existe
    except:
        g = Genero()
        g.nome = nome               # Se nao existir cria-se um genero com o nome desejado
        g.save()

def add_jogo(nome, idjogo, img, generos, preco, ram, descricao):
    try:
        j = Jogo.objects.get(nome=nome)     # Verifica se o jogo ja existe
    except:
        j = Jogo()
    j.nome = nome
    j.img1 = idjogo                 # Define os atributos do jogo
    j.img2 = img
    j.preco = preco
    j.memRAM = ram
    j.descricao = descricao
    j.disponivel = random.choice([True, True, True, False])         # Define aleatoriamente se o jogo estará disponível ou não
    j.tipoMidia = random.choice(["FISICA", "DIGITAL", "DIGITAL"])   # Define aleatoriamente se o jogo será em mídia física ou digital
    j.save()
    for genero in generos:
        try:
            g = Genero.objects.get(nome=genero)         # Varre a lista de generos procurando os generos que existem e adicionando à lista de generos do jogo
            j.listaGeneros.add(g)
        except:
            pass
    j.save()

generosENtoPT = [ ['FPS','Tiro'], ['Shooter','Tiro'], ['Action','Ação'], ['Multiplayer','Multijogador'], ['Classic','Clássico'], ['Strategy','Estratégia'], ['Survival','Sobrevivência'], ['Competitive','Competitivo'], ['First-Person','Primeira Pessoa'], ['Sci-fi','Ficção Científica'], ['Singleplayer','Um Jogador'], ['Adventure','Aventura'], ['Horror','Terror'], ['Puzzle','Quebra-Cabeça'], ['RPG','RPG'], ['Simulation','Simulação'], ['Indie','Indie'], ['Casual','Casual'], ['Racing','Corrida'], ['Sports','Esportes'], ['Massively Multiplayer','MMO'] ]
for dupla in generosENtoPT:         # Como o programa estava pegando os generos da steam em inglês eu achei mais facil fazer essa lista de traduções pra converter os nomes pra português
    add_genero(dupla[1])

for i in range(1,99999):
    try:
        idjogo = 10 * i                 # Eu descobri que as URLs dos jogos na steam sempre terminam em 0, então foi só multiplicar o valor iterado por 10
        steampage = BeautifulSoup(urllib.request.urlopen('http://store.steampowered.com/app/'+str(idjogo)).read())      # Obtem o HTML da pagina desejada na forma de uma string gigante
        nome = str(steampage.find('div', attrs={'class': 'page_title_area game_title_area page_content'}).find('span')) # Busca na string do HTML o div com atributo de classe 'page_title_area game_title_area page_content' e dentro deste pega o 'span'
        nome = nome.replace('<span itemprop="name">', '')       # Remove as tags inuteis da string, para manter só o nome
        nome = nome.replace('</span>', '')
        img = str(steampage.find('div', attrs={'class': 'game_header_image_ctn'}).find('img'))      # Busca a tag de imagem dentro do div cuja classe é 'game_header_image_ctn'
        img = img.replace('<img class="game_header_image_full" src="http://cdn.akamai.steamstatic.com/steam/apps/', '')
        img = img.replace(str(idjogo), '')
        img = img.replace('/header.jpg?t=', '')         # Remove o resto da tag da imagem, deixando só o id da própria imagem
        img = img.replace('">', '')
        img = img.replace('</img>', '')
        img = img.replace('\n', '')
        generos = str(steampage.find('div', attrs={'class': 'glance_tags popular_tags'}))       # Busca os gêneros do jogo
        generos = generos.replace('+', '')
        generos = generos.replace('\t', '')         # Remove os comandos de formatação
        generos = generos.replace('\r', '')
        generos = re.sub(r'<.+?>', '', generos)     # Remove as tags
        listageneros = generos.split('\n')          # Divide a string de generos em uma lista, a divisão é feita em todos os pulos de linha
        listageneros = list(filter(None, listageneros))     # Remove elementos vazios da lista
        generosPT = []
        for dupla in generosENtoPT:      # Percorre a lista definida no início do arquivo para verificar se foi declarado uma tradução daquele genero
            if dupla[0] in listageneros:
                generosPT.append(dupla[1])         # Se existe uma tradução declarada ela é adicionada à nova lista
        preco = str(steampage.find('div', attrs={'class': 'game_purchase_price price'}))        # Busca o div que contém o preço
        preco = preco.replace('R$', '')
        preco = preco.replace('\t', '')     # Remove tags, comandos de formatação e caracteres a mais
        preco = re.sub(r'<.+?>', '', preco)
        preco = preco.split('\n')
        preco = preco[1]        # Depois do split ele sempre gera uma lista com uma string vazia na primeira posição e a string do preço na segunda posição
        preco = preco.replace(' ', '')      # A string do preço sempre começa com um espaço
        preco = preco.replace(',', '.')     # Converte a , do valor em R$ para .
        preco = round(float(preco))         # Converte o valor para float e arredonda para inteiro
        ram = str(steampage.find('div', attrs={'class': 'game_area_sys_req sysreq_content active'}))
        ram = re.sub(r'<.+?>', '', ram)     # Remove as tags
        ram = ram.split('\n')               # Separa a string nos pulos de linha
        ram = list(filter(None, ram))       # Remove os elementos nulos (strings vazias) da lista
        ram = ' '.join(ram)                 # Converte a lista de volta para uma única string, colocando espaços entre os elementos
        ram = ram.replace('\t', '')
        ram = ram.replace('\r', ' ')        # Remove comandos de formatação
        ram = ram.replace(',', ' ')
        ram = ram.replace(':', ' ')         # Converte os separadores para espaços
        ram = ram.lower()                   # Converte as letras para minúsculas
        listaram = ram.split(' ')           # Separa a string nos espaços
        listaram = list(filter(None, listaram))     # Remove os elementos nulos (sim, denovo)
        ram = []
        for i in range(0, len(listaram)):   # Os valores sempre possuiam a palavra 'memory' à sua esquerda ou 'ram' à sua direita e o 'mb'/'gb' podia estar separado do valor por um espaço ou não
            if ((listaram[i] == 'mb') and (listaram[i + 1] == 'ram' or 'memory' in listaram[i - 2])):       # Então são necessários 4 casos para obter apenas o valor
                ram.append(int(listaram[i - 1]))                                                            # A maior parte dos jogos possui valores mínimo e recomendado de RAM
            else:                                                                                           # então a lista ram fica com 2 elementos, mas só o primeiro interessa
                if (('mb' in listaram[i]) and (listaram[i + 1] == 'ram' or 'memory' in listaram[i - 1])):
                    listaram[i] = listaram[i].replace('mb', '')
                    ram.append(int(listaram[i]))
            if ((listaram[i] == 'gb') and (listaram[i + 1] == 'ram' or 'memory' in listaram[i - 2])):
                ram.append(int(listaram[i - 1]) * 1024)
            else:
                if (('gb' in listaram[i]) and (listaram[i + 1] == 'ram' or 'memory' in listaram[i - 1])):
                    listaram[i] = listaram[i].replace('gb', '')
                    ram.append(int(listaram[i])*1024)
        descricao = str(steampage.find('div', attrs={'class': 'game_description_snippet'}))
        descricao = descricao.replace('\t', '')     # Remove comandos de formataçãp
        descricao = descricao.replace('\r', '')
        descricao = re.sub(r'<.+?>', '', descricao) # Remove tags
        descricao = descricao.split('\n')           # Separa nos pulos de linha
        descricao = list(filter(None, descricao))   # Remove os elementos nulos da lista
        descricao = descricao[0]                    # Após remover os elementos nulos a lista fica com apenas um valor, que é a própria string que contém a descrição
        if descricao != 'None' and len(generosPT) != 0 and preco != 0:      # Se não há descrição ou generos definidos ou preço o jogo não é adicionado
            add_jogo(nome, idjogo, img, generosPT, preco, ram[0], descricao)
    except:
        pass