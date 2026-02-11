"""
IMPORTS NO PYTHON - Guia Completo
Como importar módulos, pacotes e organizar código
ESSENCIAL para trabalhar com Django!
"""

# ============================================
# 1. IMPORT BÁSICO
# ============================================

# Importar módulo inteiro da biblioteca padrão
import datetime
import os
import sys

# Usar funções do módulo com prefixo
caminho = os.path.join("pasta", "arquivo.txt")
agora = datetime.datetime.now()

# Importar múltiplos módulos (uma linha cada é mais legível)

# ============================================
# 2. IMPORT COM ALIAS (AS)
# ============================================

# Alias para nomes longos ou convenções (MUITO COMUM!)
import pandas as pd

# Usar com alias
df = pd.DataFrame({"A": [1, 2, 3]})

# Alias para evitar conflitos de nomes

# ============================================
# 3. FROM IMPORT (IMPORTAR ESPECÍFICO)
# ============================================

# Importar função/classe específica
from datetime import datetime
from os.path import exists

# Usar diretamente (sem prefixo)
agora = datetime.now()  # Não precisa de datetime.datetime.now()
arquivo_existe = exists("arquivo.txt")

# From import com alias

# ============================================
# 4. IMPORT * (IMPORTAR TUDO - CUIDADO!)
# ============================================

# ❌ NÃO RECOMENDADO na maioria dos casos
from os.path import *

"""
Problemas do import *:
1. Polui o namespace (não sabe o que foi importado)
2. Pode sobrescrever variáveis existentes
3. Dificulta debugging
4. Ruff e outros linters reclamam (F403, F405)

✅ Exceção: Em shells interativos ou scripts descartáveis
from math import *  # OK para exploração rápida
sin(3.14)
"""

# ============================================
# 5. ESTRUTURA DE MÓDULOS E PACOTES
# ============================================

"""
Estrutura de exemplo:

meu_projeto/
├── main.py
├── utils.py
└── myapp/
    ├── __init__.py      # Torna 'myapp' um pacote
    ├── models.py
    ├── views.py
    └── services/
        ├── __init__.py  # Torna 'services' um pacote
        ├── email.py
        └── payment.py
"""

# ============================================
# 6. IMPORTS ABSOLUTOS (RECOMENDADO)
# ============================================

"""
Imports absolutos começam do diretório raiz do projeto
(onde está manage.py no Django ou onde você roda python)

# De main.py:
from utils import funcao_util
from myapp.models import User
from myapp.services.email import enviar_email

# De myapp/views.py:
from myapp.models import User  # Import absoluto
from myapp.services.email import enviar_email
"""

# Django usa imports absolutos (definido em settings.py)
from django.contrib.auth.models import User

# ============================================
# 7. IMPORTS RELATIVOS (ÚTIL EM PACOTES)
# ============================================

"""
Imports relativos usam . (ponto) para indicar localização relativa
. = diretório atual
.. = diretório pai
... = dois níveis acima

# De myapp/views.py:
from .models import User              # Mesmo pacote (myapp/)
from .services.email import enviar    # Subpacote
from ..utils import helper            # Pacote pai

# De myapp/services/payment.py:
from .email import enviar_email       # Mesmo nível (services/)
from ..models import User             # Nível acima (myapp/)
from ..views import index             # Nível acima

⚠️ IMPORTANTE:
- Imports relativos SÓ funcionam dentro de pacotes (precisa __init__.py)
- NÃO funcionam em scripts executados diretamente (python script.py)
- Django prefere absolutos, mas relativos funcionam bem
"""

# Exemplo prático Django
"""
# myapp/views.py
from django.shortcuts import render
from .models import Produto, Categoria  # Import relativo
from .forms import ProdutoForm
from ..core.utils import format_currency  # Pacote pai
"""

# ============================================
# 8. __init__.py - TORNANDO DIRETÓRIOS EM PACOTES
# ============================================

"""
__init__.py transforma um diretório em pacote Python

# myapp/__init__.py (pode ser vazio)
# Ou exportar coisas específicas para facilitar imports:

# myapp/__init__.py
from .models import User, Produto
from .views import index, produto_detail

# Agora de outros lugares você pode fazer:
from myapp import User, Produto  # Ao invés de myapp.models

# __init__.py também executa código na importação
print("Pacote myapp importado!")  # Executa quando importar myapp
"""

# Exemplo real Django
"""
# myapp/__init__.py
default_app_config = 'myapp.apps.MyappConfig'  # Django 3.1-
"""

# ============================================
# 9. IMPORT CONDICIONAL
# ============================================

# Importar baseado em condições (útil para dependências opcionais)
try:
    import pandas as pd

    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    pd = None

# Uso
if PANDAS_AVAILABLE:
    df = pd.DataFrame({"A": [1, 2, 3]})
else:
    print("Pandas não está instalado")

# Import condicional por versão

if sys.version_info >= (3, 10):
    from typing import TypeAlias  # Só existe em Python 3.10+
else:
    TypeAlias = type  # Fallback

# Import condicional por plataforma
import platform

if platform.system() == "Windows":
    pass
else:
    pass

# ============================================
# 10. IMPORT DINÂMICO (RUNTIME)
# ============================================

# Importar módulo por string (menos comum)
import importlib

# Import dinâmico básico
modulo_nome = "datetime"
modulo = importlib.import_module(modulo_nome)
agora = modulo.datetime.now()

# Import dinâmico de função específica
from importlib import import_module

modulo = import_module("myapp.models")
User = modulo.User

# Útil para plugins ou apps dinâmicos
APPS = ["myapp", "blog", "shop"]
for app_name in APPS:
    try:
        app = import_module(f"{app_name}.models")
        print(f"App {app_name} carregado")
    except ImportError:
        print(f"App {app_name} não encontrado")

# Django usa isso para carregar apps (INSTALLED_APPS)

# ============================================
# 11. CIRCULAR IMPORTS (PROBLEMA COMUM!)
# ============================================

"""
❌ CIRCULAR IMPORT - Quando A importa B e B importa A

# arquivo_a.py
from arquivo_b import funcao_b
def funcao_a():
    return funcao_b()

# arquivo_b.py
from arquivo_a import funcao_a  # ❌ ERRO! ImportError
def funcao_b():
    return funcao_a()

SOLUÇÕES:

1. ✅ Reestruturar código (melhor solução)
   - Mover código compartilhado para terceiro módulo
   - Repensar a arquitetura

2. ✅ Import dentro da função
   def funcao_b():
       from arquivo_a import funcao_a  # Import local
       return funcao_a()

3. ✅ Import no final do arquivo
   # arquivo_a.py
   def funcao_a():
       return funcao_b()
   from arquivo_b import funcao_b  # Import no final

4. ✅ Usar TYPE_CHECKING (para type hints)
   from typing import TYPE_CHECKING
   if TYPE_CHECKING:
       from arquivo_b import ClasseB  # Só para type checker
"""

# Exemplo prático Django (circular import comum)
"""
❌ PROBLEMA:
# models.py
from .views import get_context
class User(models.Model):
    pass

# views.py
from .models import User  # ❌ Circular import!

✅ SOLUÇÃO:
# views.py
def minhas_views(request):
    from .models import User  # Import dentro da função
    users = User.objects.all()
"""

# ============================================
# 12. ORDEM DE IMPORTS (PEP 8 + DJANGO)
# ============================================

"""
Ordem recomendada (Ruff organiza automaticamente!):

1. Biblioteca padrão
2. Bibliotecas terceiras
3. Imports locais/projeto

Separado por linha em branco entre grupos
"""

# ✅ Exemplo correto (Ruff faz isso automaticamente):
# Biblioteca padrão
import os
import sys
from datetime import datetime

# Bibliotecas terceiras
import pandas as pd

# Imports locais

# ============================================
# 13. LAZY IMPORTS (PERFORMANCE)
# ============================================

"""
Import pesados dentro de funções para melhorar tempo de inicialização
"""


# ❌ Lento: import no topo (sempre carrega mesmo se não usar)
# ✅ Rápido: import dentro da função (só carrega quando usar)
def processar_imagem(img_path):
    from PIL import Image  # Só importa se função for chamada

    img = Image.open(img_path)
    return img.resize((100, 100))


def analise_dados():
    import pandas as pd  # Pesado, só carrega se necessário

    return pd.read_csv("dados.csv")


# Django faz muito isso internamente

# ============================================
# 14. __all__ - CONTROLAR "FROM MODULE IMPORT *"
# ============================================

"""
# utils.py
__all__ = ['funcao_publica', 'ClassePublica']  # Lista o que exportar

def funcao_publica():
    pass

def _funcao_privada():  # _ indica privado (convenção)
    pass

class ClassePublica:
    pass

# Em outro arquivo:
from utils import *  # Importa só funcao_publica e ClassePublica
"""

# ============================================
# 15. IMPORTS NO DJANGO - PADRÕES COMUNS
# ============================================

"""
# views.py - Estrutura típica
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from .models import Produto, Categoria
from .forms import ProdutoForm
from .utils import calcular_frete


# models.py - Estrutura típica
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# urls.py - Estrutura típica
from django.urls import path, include
from . import views
# ou
from .views import ProdutoListView, ProdutoDetailView


# settings.py - Imports mínimos (é só configuração)
from pathlib import Path
import os
# Evite imports de models ou views em settings.py!


# apps.py - Configuração de app
from django.apps import AppConfig


# admin.py - Registro de modelos
from django.contrib import admin
from .models import Produto, Categoria
"""

# ============================================
# 16. BOAS PRÁTICAS E DICAS
# ============================================

"""
✅ FAÇA:
1. Use imports absolutos (mais claro)
2. Import específico (from x import y) ao invés de import x
3. Uma linha por import (legibilidade)
4. Organize com Ruff/isort automaticamente
5. Use alias para nomes longos (pandas as pd)
6. Evite circular imports (reestruture código)

❌ NÃO FAÇA:
1. from module import * (exceto em shell)
2. Import dentro de loops (performance)
3. Imports não usados (Ruff remove automaticamente)
4. Nomes conflitantes sem alias
5. Import de models em settings.py

PERFORMANCE:
- Imports são cachados (só carregam uma vez)
- Import dentro de função = lazy loading (útil para pesados)
- Import no topo = eager loading (padrão, recomendado)

DEBUGGING:
- Use print(modulo.__file__) para ver de onde vem
- Use dir(modulo) para ver o que tem dentro
- Use help(modulo) para documentação
"""

# Exemplo debug
import pandas as pd

print(pd.__file__)  # Mostra localização do arquivo
print(pd.__version__)  # Versão (se disponível)
# print(dir(pd))  # Lista tudo disponível (muito output!)

# ============================================
# 17. CASOS ESPECIAIS E TRUQUES
# ============================================

# Import de arquivo com hífen (não pode usar from x-y import z)
my_module = __import__("my-module")

# Import de arquivo .py fora do projeto
import sys

sys.path.append("/caminho/para/diretorio")

# Verificar se módulo está importado
if "pandas" in sys.modules:
    print("Pandas já foi importado")

# Recarregar módulo (útil em desenvolvimento)
import importlib

import meu_modulo

importlib.reload(meu_modulo)  # Recarrega mudanças

# ============================================
# 18. TYPE HINTS COM IMPORTS
# ============================================

"""
# Python 3.9+
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Imports só para type checking (não executa em runtime)
    from myapp.models import User

def get_user() -> 'User':  # String annotation evita erro se User não importado
    from myapp.models import User  # Import real dentro
    return User.objects.first()

# Python 3.10+
from typing import TypeAlias
from myapp.models import User

UserType: TypeAlias = User  # Alias de tipo
"""

# ============================================
# RESUMO FINAL
# ============================================

"""
IMPORTS NO PYTHON:
- import modulo              → Importa módulo completo
- import modulo as alias     → Com alias
- from modulo import x       → Importa específico
- from modulo import *       → Tudo (evitar!)
- from . import x            → Relativo (pacotes)
- from .. import x           → Relativo (pai)

DJANGO:
- Prefira imports absolutos
- Organize por: stdlib → third-party → local
- Use Ruff para organizar automaticamente
- Evite circular imports
- Import models/views/forms de seus apps

PERFORMANCE:
- Imports são cachados
- Import dentro de função = lazy loading
- Import no topo = padrão recomendado

DEBUGGING:
- __file__, __version__, dir(), help()
- importlib.reload() para desenvolver
"""

# Para ver este guia funcionando:
if __name__ == "__main__":
    print("✅ Guia de Imports carregado com sucesso!")
    print(f"📁 Localização: {__file__}")
    print("📚 Execute cada seção individualmente para testar")
