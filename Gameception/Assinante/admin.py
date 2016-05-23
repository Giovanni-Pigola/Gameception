#adicionar imports e .registers para as classes que serao manipuladas pelo admin

from django.contrib import admin
from .models import Assinante
from .models import EnderecoAssinatura
from .models import DadosAssinatura
from .models import DadosBancarios
from .models import Genero
#from .models import HistoricoJogos

admin.site.register(Assinante)
admin.site.register(EnderecoAssinatura)
admin.site.register(DadosAssinatura)
admin.site.register(DadosBancarios)
admin.site.register(Genero)
#admin.site.register(HistoricoJogos)
