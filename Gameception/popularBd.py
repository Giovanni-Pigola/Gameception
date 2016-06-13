import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gameception.settings')

import django
django.setup()

from Assinante.models import Jogo, Genero


def populate():

    add_genero("Aventura")
    add_genero("Ação")
    add_genero("Casual")
    add_genero("Corrida")
    add_genero("Esportes")
    add_genero("Estratégia")
    add_genero("Indie")
    add_genero("MMO")
    add_genero("RPG")
    add_genero("Simulação")

    add_jogo(nome="POPixel"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/485560/header.jpg?t=1464998779"
        ,generos=["Ação", "Aventura", "Casual", "Indie"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=2000
        ,preco=5)

    add_jogo(nome="Turmoil"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/361280/header.jpg?t=1465378225"
        ,generos=["Indie", "Simulação", "Estratégia"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=2000
        ,preco=20)

    add_jogo(nome="CREA"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/280520/header.jpg?t=1465501327"
        ,generos=["RPG",]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=2000
        ,preco=10)

    add_jogo(nome="Landmark"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/297810/header.jpg?t=1465599592"
        ,generos=["RPG","Aventura","MMO"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=4000
        ,preco=20)

    add_jogo(nome="XCOM2"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/268500/header.jpg?t=1463073148"
        ,generos=["Estratégia",]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=4000
        ,preco=65)

    add_jogo(nome="Rocket League"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/252950/header.jpg?t=1464386066"
        ,generos=["Corrida","Indie","Ação","Esportes"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=2000
        ,preco=30)

    add_jogo(nome="Gloria Victis"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/327070/header.jpg?t=1465508322"
        ,generos=["RPG","MMO","Ação","Indie"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=3000
        ,preco=35)

    add_jogo(nome="Football Manager 2016"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/378120/header.jpg?t=1462576113"
        ,generos=["Simulação","Esportes"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=2000
        ,preco=35)

    add_jogo(nome="Legends of Callasia"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/438920/header.jpg?t=1465586404"
        ,generos=["Estratégia"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=512
        ,preco=20)

    add_jogo(nome="Youtubers Life"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/428690/header.jpg?t=1464882002"
        ,generos=["Estratégia","Indie","Simulação"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=2000
        ,preco=28)

    add_jogo(nome="Hearts of Iron IV"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/394360/header.jpg?t=1465232664"
        ,generos=["Estratégia","Simulação"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=4000
        ,preco=73)

    add_jogo(nome="V ARRR"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/478950/header.jpg?t=1465553581"
        ,generos=["Ação","Simulação","Indie","Aventura"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=4000
        ,preco=28)

    add_jogo(nome="Fallout 4"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/377160/header.jpg?t=1465562950"
        ,generos=["RPG",]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=8000
        ,preco=230)

    add_jogo(nome="SteamWorld Heist"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/322190/header.jpg?t=1465492526"
        ,generos=["RPG","Aventura","Indie","Estratégia"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=1024
        ,preco=32)

    add_jogo(nome="Thirty Years' War"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/477750/header.jpg?t=1465480340"
        ,generos=["Simulação","Estratégia"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=2000
        ,preco=50)

    add_jogo(nome="Golf With Your Friends"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/431240/header.jpg?t=1464706733"
        ,generos=[ "Casual", "Indie", "Esportes"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=4000
        ,preco=12)

    add_jogo(nome="American Truck Simulator"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/270880/header.jpg?t=1465230866"
        ,generos=[ "Indie", "Simulação"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=4000
        ,preco=55)

    add_jogo(nome="Milford Heaven - Luken's Chronicles"
        ,urlSteam="http://cdn.akamai.steamstatic.com/steam/apps/485570/header.jpg?t=1465598931"
        ,generos=[  "Aventura", "Indie", "RPG"]
        ,disponivel=True,tipoMidia="DIGITAL"
        ,ram=2000
        ,preco=3)

def add_genero(nome):
    try:
        g = Genero.objects.get(nome=nome)
    except:
        g = Genero()
        g.nome=nome
    g.save()

def add_jogo(nome,urlSteam,generos,disponivel,tipoMidia,ram,preco):
    try:
        j = Jogo.objects.get(nome=nome)
    except:
        j = Jogo()
    j.nome = nome
    j.img1 = urlSteam[45:51]
    j.img2 = urlSteam[65:75]
    j.disponivel = disponivel
    j.preco = preco
    j.tipoMidia = tipoMidia
    j.memRAM = ram
    j.save()
    for genero in generos:
        try:
            g = Genero.objects.get(nome=genero)
            j.listaGeneros.add(g)
        except:
            pass
    j.save()


# Start execution here!
if __name__ == '__main__':
    print ("Populando BD...")
    populate()
