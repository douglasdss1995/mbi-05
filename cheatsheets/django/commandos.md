# Django Commands Cheatsheet

## Instalação

```bash
# Instalar Django com pip
pip install django

# Instalar Django com UV
uv pip install django

# Instalar versão específica com pip
pip install django==4.2

# Instalar versão específica com UV
uv pip install django==4.2

# Adicionar Django ao projeto UV
uv add django
```

## Criar Projeto

```bash
# Criar novo projeto
django-admin startproject nome_projeto
uv run django-admin startproject nome_projeto

# Criar projeto na pasta atual (usa o diretório atual)
django-admin startproject nome_projeto .
uv run django-admin startproject nome_projeto .

# Verificar versão do Django
python -m django --version
uv run python -m django --version
```

## Criar App

```bash
# Criar novo app
python manage.py startapp nome_app
uv run python manage.py startapp nome_app

# Criar app dentro de uma pasta específica
python manage.py startapp nome_app pasta/
uv run python manage.py startapp nome_app pasta/
```

## Servidor de Desenvolvimento

```bash
# Iniciar servidor (padrão: localhost:8000)
python manage.py runserver
uv run python manage.py runserver

# Iniciar em porta específica
python manage.py runserver 8080
uv run python manage.py runserver 8080

# Iniciar em IP e porta específicos
python manage.py runserver 0.0.0.0:8000
uv run python manage.py runserver 0.0.0.0:8000

# Desabilitar auto-reload
python manage.py runserver --noreload
uv run python manage.py runserver --noreload
```

## Migrações de Banco de Dados

```bash
# Criar migrações (detecta mudanças nos models)
python manage.py makemigrations
uv run python manage.py makemigrations

# Criar migração para app específico
python manage.py makemigrations nome_app
uv run python manage.py makemigrations nome_app

# Aplicar migrações
python manage.py migrate
uv run python manage.py migrate

# Aplicar migração específica
python manage.py migrate nome_app
uv run python manage.py migrate nome_app

# Ver SQL de uma migração
python manage.py sqlmigrate nome_app 0001
uv run python manage.py sqlmigrate nome_app 0001

# Listar migrações
python manage.py showmigrations
uv run python manage.py showmigrations

# Reverter migração
python manage.py migrate nome_app 0001
uv run python manage.py migrate nome_app 0001
```

## Banco de Dados

```bash
# Acessar shell do banco de dados
python manage.py dbshell
uv run python manage.py dbshell

# Limpar banco de dados
python manage.py flush
uv run python manage.py flush
```

## Shell Interativo

```bash
# Abrir shell do Django
python manage.py shell
uv run python manage.py shell

# Shell com IPython (se instalado)
python manage.py shell -i ipython
uv run python manage.py shell -i ipython

# Shell com BPython (se instalado)
python manage.py shell -i bpython
uv run python manage.py shell -i bpython
```

## Super Usuário

```bash
# Criar superusuário
python manage.py createsuperuser
uv run python manage.py createsuperuser

# Alterar senha de usuário
python manage.py changepassword username
uv run python manage.py changepassword username
```

## Arquivos Estáticos

```bash
# Coletar arquivos estáticos
python manage.py collectstatic
uv run python manage.py collectstatic

# Coletar sem confirmação
python manage.py collectstatic --noinput
uv run python manage.py collectstatic --noinput

# Limpar arquivos antigos
python manage.py collectstatic --clear
uv run python manage.py collectstatic --clear
```

## Testes

```bash
# Executar todos os testes
python manage.py test
uv run python manage.py test

# Testar app específico
python manage.py test nome_app
uv run python manage.py test nome_app

# Testar classe específica
python manage.py test nome_app.tests.MinhaClasseTest
uv run python manage.py test nome_app.tests.MinhaClasseTest

# Testar método específico
python manage.py test nome_app.tests.MinhaClasseTest.test_metodo
uv run python manage.py test nome_app.tests.MinhaClasseTest.test_metodo

# Manter banco de dados de teste
python manage.py test --keepdb
uv run python manage.py test --keepdb

# Executar testes em paralelo
python manage.py test --parallel
uv run python manage.py test --parallel
```

## Inspeção

```bash
# Verificar problemas no projeto
python manage.py check
uv run python manage.py check

# Verificar deploy
python manage.py check --deploy
uv run python manage.py check --deploy

# Listar comandos disponíveis
python manage.py help
uv run python manage.py help

# Ajuda de comando específico
python manage.py help comando
uv run python manage.py help comando
```

## Dados

```bash
# Exportar dados (dump)
python manage.py dumpdata > dados.json
uv run python manage.py dumpdata > dados.json

# Exportar app específico
python manage.py dumpdata nome_app > dados.json
uv run python manage.py dumpdata nome_app > dados.json

# Exportar com indentação
python manage.py dumpdata --indent 2 > dados.json
uv run python manage.py dumpdata --indent 2 > dados.json

# Importar dados (load)
python manage.py loaddata dados.json
uv run python manage.py loaddata dados.json
```

## Limpeza e Manutenção

```bash
# Limpar sessões expiradas
python manage.py clearsessions
uv run python manage.py clearsessions

# Criar cache tables
python manage.py createcachetable
uv run python manage.py createcachetable
```

## URLs

```bash
# Listar todas as URLs do projeto (requer django-extensions)
python manage.py show_urls
uv run python manage.py show_urls
```

## Mensagens

```bash
# Compilar arquivos de tradução
python manage.py compilemessages
uv run python manage.py compilemessages

# Criar arquivos de tradução
python manage.py makemessages -l pt_BR
uv run python manage.py makemessages -l pt_BR
```

## Comandos Personalizados

Para criar comandos personalizados, crie a estrutura:

```
nome_app/
  management/
    __init__.py
    commands/
      __init__.py
      meu_comando.py
```

Exemplo de comando personalizado:

```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Descrição do comando'

    def add_arguments(self, parser):
        parser.add_argument('argumento', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Executando comando...')
```

## Dicas Úteis

### Criar Projeto na Pasta Atual
Use o ponto (`.`) após o nome do projeto:
```bash
django-admin startproject config .
uv run django-admin startproject config .
```
Isso cria o projeto sem criar uma pasta adicional com o nome do projeto.

### Estrutura Típica de Projeto
```
projeto/
├── manage.py
├── config/              # Pasta do projeto principal
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── apps/                # Apps do projeto
    ├── app1/
    └── app2/
```

### Variáveis de Ambiente
```bash
# Usar settings específico
python manage.py runserver --settings=config.settings.development
uv run python manage.py runserver --settings=config.settings.development

# Definir via variável de ambiente
export DJANGO_SETTINGS_MODULE=config.settings.production
python manage.py runserver
uv run python manage.py runserver
```

### Debug
```bash
# Executar com debug SQL
python manage.py runserver --verbosity 2
uv run python manage.py runserver --verbosity 2

# Mostrar SQL gerado
python manage.py runserver --settings=config.settings --debug-sql
uv run python manage.py runserver --settings=config.settings --debug-sql
```

## Atalhos Comuns

### Usando Python

```bash
# Criar projeto, app e rodar servidor
django-admin startproject config .
python manage.py startapp core
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Reset completo do banco
python manage.py flush
python manage.py migrate

# Rebuild do banco
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Usando UV

```bash
# Criar projeto, app e rodar servidor
uv run django-admin startproject config .
uv run python manage.py startapp core
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver

# Reset completo do banco
uv run python manage.py flush
uv run python manage.py migrate

# Rebuild do banco
rm db.sqlite3
uv run python manage.py migrate
uv run python manage.py createsuperuser
```
