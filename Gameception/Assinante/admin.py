#adicionar imports e .registers para as classes que serao manipuladas pelo admin

from django.contrib import admin
from .models import Assinante
from .models import EnderecoAssinatura
from .models import DadosAssinatura
from .models import DadosBancarios
from .models import Genero
from .models import SistOp
from .models import Processadores
from .models import ChaveDownload
from .models import HistoricoJogos
from .models import Pedido
from .models import Jogo
from .models import TipoMidia

admin.site.register(Assinante)
admin.site.register(EnderecoAssinatura)
admin.site.register(DadosAssinatura)
admin.site.register(DadosBancarios)
admin.site.register(Genero)
admin.site.register(SistOp)
admin.site.register(Processadores)
admin.site.register(ChaveDownload)
admin.site.register(HistoricoJogos)
admin.site.register(Pedido)
admin.site.register(Jogo)
admin.site.register(TipoMidia)
