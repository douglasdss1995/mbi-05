# Guia Completo: Campos do Django

## Tabela 1: Tipos de Campos do Django e Suas Utilizações

| Campo                                                        | Descrição                                       | Uso Típico                               | Exemplo                                |
|--------------------------------------------------------------|-------------------------------------------------|------------------------------------------|----------------------------------------|
| **CharField**                                                | Texto curto com tamanho limitado                | Nomes, títulos, códigos, slugs           | Nome de produto, título de artigo      |
| **TextField**                                                | Texto longo sem limite definido                 | Descrições, comentários, conteúdo        | Descrição de produto, corpo de artigo  |
| **IntegerField**                                             | Números inteiros (-2147483648 a 2147483647)     | Quantidades, idades, contadores          | Estoque, número de visualizações       |
| **PositiveIntegerField**                                     | Números inteiros positivos (0 a 2147483647)     | Quantidades que não podem ser negativas  | Estoque, quantidade de itens           |
| **PositiveSmallIntegerField**                                | Números inteiros positivos pequenos (0 a 32767) | Contadores menores, idades               | Idade, número de tentativas            |
| **SmallIntegerField**                                        | Números inteiros pequenos (-32768 a 32767)      | Valores numéricos com range limitado     | Prioridade (-10 a 10)                  |
| **BigIntegerField**                                          | Números inteiros muito grandes                  | IDs externos, números muito grandes      | ID de sistema externo                  |
| **DecimalField**                                             | Números decimais de precisão fixa               | Valores monetários, percentuais precisos | Preço, taxa de juros                   |
| **FloatField**                                               | Números decimais de ponto flutuante             | Medidas científicas, coordenadas         | Latitude, longitude, temperatura       |
| **BooleanField**                                             | Verdadeiro ou Falso                             | Flags, status binários                   | Ativo/inativo, publicado/rascunho      |
| **DateField**                                                | Data (ano, mês, dia)                            | Datas de nascimento, eventos             | Data de nascimento, data do evento     |
| **DateTimeField**                                            | Data e hora completas                           | Registro de quando algo aconteceu        | Data de criação, última atualização    |
| **TimeField**                                                | Apenas hora (hora, minuto, segundo)             | Horários de funcionamento, agendamentos  | Horário de abertura da loja            |
| **DurationField**                                            | Período de tempo (timedelta)                    | Duração de eventos, tempo decorrido      | Duração de um curso, tempo de vídeo    |
| **EmailField**                                               | Email com validação automática                  | Endereços de email                       | Email do usuário                       |
| **URLField**                                                 | URL com validação automática                    | Links, sites, referências                | Website da empresa, link externo       |
| **SlugField**                                                | Texto URL-friendly (alfanumérico + hífens)      | URLs amigáveis para SEO                  | URL de produto, slug de artigo         |
| **UUIDField**                                                | Identificador único universal                   | IDs únicos, tokens, chaves públicas      | Token de API, ID público               |
| **FileField**                                                | Upload de arquivos genéricos                    | Documentos, PDFs, arquivos diversos      | Contrato PDF, documento anexo          |
| **ImageField**                                               | Upload de imagens com validação                 | Fotos, logos, imagens                    | Foto de produto, avatar do usuário     |
| **BinaryField**                                              | Dados binários brutos                           | Arquivos pequenos em formato binário     | Pequenos arquivos criptografados       |
| **JSONField**                                                | Dados em formato JSON                           | Configurações, metadados flexíveis       | Configurações do usuário, dados extras |
| **[ForeignKey](ForeignKey (Relacionamento Muitos-para-Um))** | Relacionamento muitos-para-um                   | Relacionar um item a outro               | Produto → Categoria                    |
| **OneToOneField**                                            | Relacionamento um-para-um                       | Extensão de model, perfil de usuário     | User → Perfil                          |
| **ManyToManyField**                                          | Relacionamento muitos-para-muitos               | Tags, categorias múltiplas               | Produto ↔ Tags                         |
| **GenericIPAddressField**                                    | Endereço IP (IPv4 ou IPv6)                      | Logs de acesso, whitelist/blacklist      | IP do usuário, IP bloqueado            |
| **AutoField**                                                | Inteiro auto-incrementável (PK padrão)          | Chave primária automática                | ID padrão do Django                    |
| **BigAutoField**                                             | BigInteger auto-incrementável                   | Chave primária para tabelas grandes      | ID padrão no Django 3.2+               |

---

## Tabela 2: Parâmetros dos Campos do Django

### Parâmetros Comuns (Aplicam-se a Todos ou Maioria dos Campos)

| Parâmetro          | Tipo | Padrão | Descrição                            | Campos que Aceitam |
|--------------------|------|--------|--------------------------------------|--------------------|
| **null**           | bool | False  | Permite valor NULL no banco de dados | Todos              |
| **blank**          | bool | False  | Permite valor vazio em formulários   | Todos              |
| **default**        | any  | -      | Valor padrão quando não especificado | Todos              |
| **primary_key**    | bool | False  | Define como chave primária           | Todos              |
| **unique**         | bool | False  | Garante valores únicos               | Todos              |
| **db_index**       | bool | False  | Cria índice no banco de dados        | Todos              |
| **editable**       | bool | True   | Se pode ser editado em formulários   | Todos              |
| **verbose_name**   | str  | -      | Nome legível do campo                | Todos              |
| **help_text**      | str  | -      | Texto de ajuda em formulários        | Todos              |
| **choices**        | list | -      | Lista de opções permitidas           | Todos              |
| **validators**     | list | []     | Validadores customizados             | Todos              |
| **error_messages** | dict | -      | Mensagens de erro customizadas       | Todos              |
| **db_column**      | str  | -      | Nome da coluna no banco              | Todos              |
| **db_tablespace**  | str  | -      | Tablespace do banco de dados         | Todos              |

---

## Parâmetros Específicos por Tipo de Campo

### CharField

| Parâmetro      | Tipo | Padrão | Obrigatório | Descrição               |
|----------------|------|--------|-------------|-------------------------|
| **max_length** | int  | -      | ✅ Sim       | Tamanho máximo do texto |
| null           | bool | False  | ❌ Não       | Permite NULL no BD      |
| blank          | bool | False  | ❌ Não       | Permite vazio em forms  |
| default        | str  | -      | ❌ Não       | Valor padrão            |
| unique         | bool | False  | ❌ Não       | Valor único             |
| choices        | list | -      | ❌ Não       | Opções pré-definidas    |

**Exemplos:**

```python
nome = models.CharField(max_length=200)
status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')
codigo = models.CharField(max_length=50, unique=True, blank=True, null=True)
```

---

### TextField

| Parâmetro      | Tipo | Padrão | Obrigatório | Descrição                     |
|----------------|------|--------|-------------|-------------------------------|
| **max_length** | int  | -      | ❌ Não       | Limite opcional de caracteres |
| null           | bool | False  | ❌ Não       | Permite NULL no BD            |
| blank          | bool | False  | ❌ Não       | Permite vazio em forms        |
| default        | str  | -      | ❌ Não       | Valor padrão                  |

**Exemplos:**

```python
descricao = models.TextField()
observacoes = models.TextField(blank=True, null=True)
conteudo = models.TextField(default='')
```

---

### IntegerField / PositiveIntegerField / SmallIntegerField

| Parâmetro  | Tipo | Padrão | Obrigatório | Descrição                           |
|------------|------|--------|-------------|-------------------------------------|
| null       | bool | False  | ❌ Não       | Permite NULL no BD                  |
| blank      | bool | False  | ❌ Não       | Permite vazio em forms              |
| default    | int  | -      | ❌ Não       | Valor padrão                        |
| unique     | bool | False  | ❌ Não       | Valor único                         |
| choices    | list | -      | ❌ Não       | Opções pré-definidas                |
| validators | list | []     | ❌ Não       | Validadores (ex: MinValueValidator) |

**Exemplos:**

```python
from django.core.validators import MaxValueValidator, MinValueValidator

estoque = models.PositiveIntegerField(default=0)
idade = models.PositiveSmallIntegerField(validators=[MaxValueValidator(120)])
prioridade = models.SmallIntegerField(default=0)
quantidade = models.IntegerField(blank=True, null=True)
pontuacao = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
```

---

### DecimalField

| Parâmetro          | Tipo    | Padrão | Obrigatório | Descrição                             |
|--------------------|---------|--------|-------------|---------------------------------------|
| **max_digits**     | int     | -      | ✅ Sim       | Total de dígitos (incluindo decimais) |
| **decimal_places** | int     | -      | ✅ Sim       | Número de casas decimais              |
| null               | bool    | False  | ❌ Não       | Permite NULL no BD                    |
| blank              | bool    | False  | ❌ Não       | Permite vazio em forms                |
| default            | Decimal | -      | ❌ Não       | Valor padrão                          |
| validators         | list    | []     | ❌ Não       | Validadores customizados              |

**Exemplos:**

```python
from decimal import Decimal

preco = models.DecimalField(max_digits=10, decimal_places=2)
desconto = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
taxa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
percentual = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    validators=[MinValueValidator(0), MaxValueValidator(100)]
)
```

---

### FloatField

| Parâmetro | Tipo  | Padrão | Obrigatório | Descrição              |
|-----------|-------|--------|-------------|------------------------|
| null      | bool  | False  | ❌ Não       | Permite NULL no BD     |
| blank     | bool  | False  | ❌ Não       | Permite vazio em forms |
| default   | float | -      | ❌ Não       | Valor padrão           |

**Exemplos:**

```python
latitude = models.FloatField()
temperatura = models.FloatField(blank=True, null=True)
peso = models.FloatField(default=0.0)
longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
```

---

### BooleanField

| Parâmetro | Tipo | Padrão | Obrigatório | Descrição                          |
|-----------|------|--------|-------------|------------------------------------|
| default   | bool | -      | ❌ Não       | Valor padrão (recomendado definir) |
| null      | bool | False  | ❌ Não       | Não recomendado para Boolean       |

**Exemplos:**

```python
ativo = models.BooleanField(default=True)
publicado = models.BooleanField(default=False)
# NullBooleanField foi depreciado, use:
aceita_termos = models.BooleanField(null=True, blank=True)
verificado = models.BooleanField(default=False, db_index=True)
```

---

### DateField

| Parâmetro        | Tipo          | Padrão | Obrigatório | Descrição                                |
|------------------|---------------|--------|-------------|------------------------------------------|
| **auto_now**     | bool          | False  | ❌ Não       | Atualiza automaticamente a cada save()   |
| **auto_now_add** | bool          | False  | ❌ Não       | Define data na criação (não muda depois) |
| null             | bool          | False  | ❌ Não       | Permite NULL no BD                       |
| blank            | bool          | False  | ❌ Não       | Permite vazio em forms                   |
| default          | date/callable | -      | ❌ Não       | Valor padrão                             |

**Exemplos:**

```python
from django.utils import timezone
from datetime import date

data_nascimento = models.DateField()
data_evento = models.DateField(blank=True, null=True)
data_criacao = models.DateField(auto_now_add=True)
data_atualizacao = models.DateField(auto_now=True)
data_default = models.DateField(default=timezone.now)
data_vencimento = models.DateField(default=date.today)
```

**⚠️ Nota Importante sobre auto_now e auto_now_add:**

- `auto_now_add=True`: Define a data apenas na criação do objeto (não pode ser editado)
- `auto_now=True`: Atualiza a data toda vez que o objeto é salvo
- Se usar `auto_now=True` ou `auto_now_add=True`, o campo não pode ser editado manualmente
- Não é possível usar `auto_now` e `auto_now_add` juntos no mesmo campo

---

### DateTimeField

| Parâmetro        | Tipo              | Padrão | Obrigatório | Descrição                              |
|------------------|-------------------|--------|-------------|----------------------------------------|
| **auto_now**     | bool              | False  | ❌ Não       | Atualiza automaticamente a cada save() |
| **auto_now_add** | bool              | False  | ❌ Não       | Define data/hora na criação            |
| null             | bool              | False  | ❌ Não       | Permite NULL no BD                     |
| blank            | bool              | False  | ❌ Não       | Permite vazio em forms                 |
| default          | datetime/callable | -      | ❌ Não       | Valor padrão                           |

**Exemplos:**

```python
from django.utils import timezone

criado_em = models.DateTimeField(auto_now_add=True)
atualizado_em = models.DateTimeField(auto_now=True)
agendado_para = models.DateTimeField(blank=True, null=True)
timestamp = models.DateTimeField(default=timezone.now)
publicado_em = models.DateTimeField(blank=True, null=True, db_index=True)
```

---

### TimeField

| Parâmetro        | Tipo          | Padrão | Obrigatório | Descrição                |
|------------------|---------------|--------|-------------|--------------------------|
| **auto_now**     | bool          | False  | ❌ Não       | Atualiza automaticamente |
| **auto_now_add** | bool          | False  | ❌ Não       | Define hora na criação   |
| null             | bool          | False  | ❌ Não       | Permite NULL no BD       |
| blank            | bool          | False  | ❌ Não       | Permite vazio em forms   |
| default          | time/callable | -      | ❌ Não       | Valor padrão             |

**Exemplos:**

```python
from datetime import time

horario_abertura = models.TimeField()
horario_fechamento = models.TimeField(default=time(18, 0))
hora_agendamento = models.TimeField(blank=True, null=True)
hora_inicio = models.TimeField(default=time(9, 0))
```

---

### DurationField

| Parâmetro | Tipo      | Padrão | Obrigatório | Descrição              |
|-----------|-----------|--------|-------------|------------------------|
| null      | bool      | False  | ❌ Não       | Permite NULL no BD     |
| blank     | bool      | False  | ❌ Não       | Permite vazio em forms |
| default   | timedelta | -      | ❌ Não       | Valor padrão           |

**Exemplos:**

```python
from datetime import timedelta

duracao_curso = models.DurationField()
tempo_video = models.DurationField(blank=True, null=True)
prazo_entrega = models.DurationField(default=timedelta(days=7))
tempo_total = models.DurationField(default=timedelta(hours=0))
```

---

### EmailField

| Parâmetro      | Tipo | Padrão | Obrigatório | Descrição                   |
|----------------|------|--------|-------------|-----------------------------|
| **max_length** | int  | 254    | ❌ Não       | Tamanho máximo (padrão RFC) |
| null           | bool | False  | ❌ Não       | Permite NULL no BD          |
| blank          | bool | False  | ❌ Não       | Permite vazio em forms      |
| unique         | bool | False  | ❌ Não       | Email único                 |

**Exemplos:**

```python
email = models.EmailField()
email_contato = models.EmailField(blank=True)
email_principal = models.EmailField(unique=True)
email_alternativo = models.EmailField(max_length=254, blank=True, null=True)
```

---

### URLField

| Parâmetro      | Tipo | Padrão | Obrigatório | Descrição              |
|----------------|------|--------|-------------|------------------------|
| **max_length** | int  | 200    | ❌ Não       | Tamanho máximo da URL  |
| null           | bool | False  | ❌ Não       | Permite NULL no BD     |
| blank          | bool | False  | ❌ Não       | Permite vazio em forms |

**Exemplos:**

```python
website = models.URLField()
linkedin = models.URLField(blank=True, null=True)
portfolio = models.URLField(max_length=500)
github = models.URLField(max_length=200, blank=True)
```

---

### SlugField

| Parâmetro         | Tipo | Padrão | Obrigatório | Descrição                     |
|-------------------|------|--------|-------------|-------------------------------|
| **max_length**    | int  | 50     | ❌ Não       | Tamanho máximo                |
| **allow_unicode** | bool | False  | ❌ Não       | Permite caracteres Unicode    |
| unique            | bool | False  | ❌ Não       | Slug único (recomendado True) |
| null              | bool | False  | ❌ Não       | Permite NULL no BD            |
| blank             | bool | False  | ❌ Não       | Permite vazio em forms        |

**Exemplos:**

```python
slug = models.SlugField(unique=True)
slug_produto = models.SlugField(max_length=100, unique=True)
slug_unicode = models.SlugField(allow_unicode=True, blank=True)
slug_categoria = models.SlugField(max_length=200, unique=True, db_index=True)
```

**⚠️ Dica:** Use com `prepopulated_fields` no admin para gerar automaticamente:

```python
# admin.py
class ProdutoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
```

---

### UUIDField

| Parâmetro   | Tipo     | Padrão | Obrigatório | Descrição             |
|-------------|----------|--------|-------------|-----------------------|
| default     | callable | -      | ❌ Não       | Geralmente uuid.uuid4 |
| primary_key | bool     | False  | ❌ Não       | Usar como PK          |
| editable    | bool     | True   | ❌ Não       | Editável em forms     |

**Exemplos:**

```python
import uuid

id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
token = models.UUIDField(default=uuid.uuid4, unique=True)
identificador_externo = models.UUIDField(default=uuid.uuid4, editable=False)
```

---

### FileField

| Parâmetro      | Tipo         | Padrão | Obrigatório | Descrição                            |
|----------------|--------------|--------|-------------|--------------------------------------|
| **upload_to**  | str/callable | -      | ✅ Sim       | Diretório/função para upload         |
| **max_length** | int          | 100    | ❌ Não       | Tamanho do caminho do arquivo        |
| null           | bool         | False  | ❌ Não       | Permite NULL no BD                   |
| blank          | bool         | False  | ❌ Não       | Permite vazio em forms               |
| storage        | Storage      | -      | ❌ Não       | Sistema de armazenamento customizado |

**Exemplos:**

```python
def documento_upload_path(instance, filename):
    # Organizar por usuário e manter nome original
    return f'documentos/{instance.usuario.id}/{filename}'


# Upload simples
documento = models.FileField(upload_to='documentos/')

# Com estrutura de data
contrato = models.FileField(upload_to='contratos/%Y/%m/')

# Com função customizada
arquivo = models.FileField(upload_to=documento_upload_path, blank=True, null=True)

# Com validação de tamanho (requer validator customizado)
from django.core.validators import FileExtensionValidator

pdf = models.FileField(
    upload_to='pdfs/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
)
```

---

### ImageField

| Parâmetro        | Tipo         | Padrão | Obrigatório | Descrição                    |
|------------------|--------------|--------|-------------|------------------------------|
| **upload_to**    | str/callable | -      | ✅ Sim       | Diretório/função para upload |
| **height_field** | str          | -      | ❌ Não       | Campo que armazena altura    |
| **width_field**  | str          | -      | ❌ Não       | Campo que armazena largura   |
| max_length       | int          | 100    | ❌ Não       | Tamanho do caminho           |
| null             | bool         | False  | ❌ Não       | Permite NULL no BD           |
| blank            | bool         | False  | ❌ Não       | Permite vazio em forms       |

**Exemplos:**

```python
# Upload simples
imagem = models.ImageField(upload_to='produtos/')

# Opcional
foto_perfil = models.ImageField(upload_to='perfis/', blank=True, null=True)

# Com dimensões armazenadas
banner = models.ImageField(
    upload_to='banners/',
    height_field='banner_height',
    width_field='banner_width'
)
banner_height = models.PositiveIntegerField(null=True, editable=False)
banner_width = models.PositiveIntegerField(null=True, editable=False)


# Com função de upload customizada
def produto_imagem_path(instance, filename):
    return f'produtos/{instance.categoria.slug}/{filename}'


imagem_produto = models.ImageField(upload_to=produto_imagem_path)
```

**⚠️ Nota:** ImageField requer a biblioteca Pillow:

```bash
pip install Pillow
```

---

### BinaryField

| Parâmetro      | Tipo | Padrão | Obrigatório | Descrição               |
|----------------|------|--------|-------------|-------------------------|
| **max_length** | int  | -      | ❌ Não       | Tamanho máximo em bytes |
| null           | bool | False  | ❌ Não       | Permite NULL no BD      |
| blank          | bool | False  | ❌ Não       | Permite vazio em forms  |
| editable       | bool | False  | ❌ Não       | Geralmente False        |

**Exemplos:**

```python
dados_criptografados = models.BinaryField(editable=False)
hash_arquivo = models.BinaryField(max_length=64, blank=True)
assinatura_digital = models.BinaryField(null=True, blank=True)
```

**⚠️ Aviso:** BinaryField não deve ser usado para arquivos grandes. Use FileField para isso.

---

### JSONField

| Parâmetro   | Tipo               | Padrão | Obrigatório | Descrição                |
|-------------|--------------------|--------|-------------|--------------------------|
| **encoder** | JSONEncoder        | -      | ❌ Não       | Encoder JSON customizado |
| **decoder** | JSONDecoder        | -      | ❌ Não       | Decoder JSON customizado |
| null        | bool               | False  | ❌ Não       | Permite NULL no BD       |
| blank       | bool               | False  | ❌ Não       | Permite vazio em forms   |
| default     | dict/list/callable | -      | ❌ Não       | Valor padrão             |

**Exemplos:**

```python
# Dict vazio como padrão
configuracoes = models.JSONField(default=dict)

# Permite NULL
metadados = models.JSONField(blank=True, null=True)

# Lista vazia como padrão
preferencias = models.JSONField(default=list)

# Com valor padrão específico
opcoes = models.JSONField(default=dict, blank=True)

# Exemplo de dados que podem ser armazenados:
# configuracoes = {
#     "notificacoes": True,
#     "tema": "escuro",
#     "idioma": "pt-BR"
# }
```

**⚠️ Nota:** JSONField está disponível nativamente no Django 3.1+. Para versões anteriores, use `django.contrib.postgres.fields.JSONField` (apenas PostgreSQL).

---

### ForeignKey (Relacionamento Muitos-para-Um)

| Parâmetro              | Tipo      | Padrão | Obrigatório | Descrição                      |
|------------------------|-----------|--------|-------------|--------------------------------|
| **to**                 | Model/str | -      | ✅ Sim       | Model relacionado              |
| **on_delete**          | callable  | -      | ✅ Sim       | Comportamento ao deletar       |
| **related_name**       | str       | -      | ❌ Não       | Nome do relacionamento reverso |
| **related_query_name** | str       | -      | ❌ Não       | Nome para queries reversas     |
| **to_field**           | str       | -      | ❌ Não       | Campo do model relacionado     |
| **db_constraint**      | bool      | True   | ❌ Não       | Criar constraint no BD         |
| **limit_choices_to**   | dict/Q    | -      | ❌ Não       | Limitar opções                 |
| null                   | bool      | False  | ❌ Não       | Permite NULL no BD             |
| blank                  | bool      | False  | ❌ Não       | Permite vazio em forms         |

**Opções de on_delete:**

- `CASCADE`: Deleta registros relacionados
- `PROTECT`: Impede deleção se houver relacionados
- `SET_NULL`: Define como NULL (requer null=True)
- `SET_DEFAULT`: Define valor padrão (requer default)
- `SET()`: Define valor específico via função
- `DO_NOTHING`: Não faz nada (cuidado com integridade!)
- `RESTRICT`: Impede deleção (diferente de PROTECT em alguns casos)

**Exemplos:**

```python
from django.db import models
from django.contrib.auth.models import User

# Básico - CASCADE
categoria = models.ForeignKey(
    'Categoria',
    on_delete=models.CASCADE
)

# Com related_name customizado
criado_por = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='produtos_criados'
)
# Uso: user.produtos_criados.all()

# Opcional com PROTECT
autor = models.ForeignKey(
    'Autor',
    on_delete=models.PROTECT,  # Não permite deletar autor se tiver artigos
    related_name='artigos'
)

# String reference (evita import circular)
empresa = models.ForeignKey(
    'empresas.Empresa',
    on_delete=models.CASCADE
)

# Self-reference (hierarquia)
categoria_pai = models.ForeignKey(
    'self',
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    related_name='subcategorias'
)

# Com limit_choices_to
autor_ativo = models.ForeignKey(
    'Autor',
    on_delete=models.CASCADE,
    limit_choices_to={'ativo': True},
    related_name='artigos'
)

# Com to_field (relacionar com campo não-PK)
produto_por_codigo = models.ForeignKey(
    'Produto',
    on_delete=models.CASCADE,
    to_field='codigo',  # Ao invés de 'id'
    related_name='referencias'
)
```

**Uso do related_name:**

```python
# Model
class Categoria(models.Model):
    nome = models.CharField(max_length=100)


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='produtos'  # Define nome do relacionamento reverso
    )


# Queries
categoria = Categoria.objects.get(id=1)
produtos = categoria.produtos.all()  # Usa related_name
produtos_ativos = categoria.produtos.filter(ativo=True)
```

---

### OneToOneField (Relacionamento Um-para-Um)

| Parâmetro        | Tipo      | Padrão | Obrigatório | Descrição                          |
|------------------|-----------|--------|-------------|------------------------------------|
| **to**           | Model/str | -      | ✅ Sim       | Model relacionado                  |
| **on_delete**    | callable  | -      | ✅ Sim       | Comportamento ao deletar           |
| **related_name** | str       | -      | ❌ Não       | Nome do relacionamento reverso     |
| **parent_link**  | bool      | False  | ❌ Não       | Se é link para model pai (herança) |
| null             | bool      | False  | ❌ Não       | Permite NULL no BD                 |
| blank            | bool      | False  | ❌ Não       | Permite vazio em forms             |

**Exemplos:**

```python
from django.contrib.auth.models import User


# Perfil de usuário (padrão mais comum)
class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='perfis/', blank=True)


# Uso:
# user.perfil.bio
# perfil.usuario.username

# Configuração opcional
class Configuracao(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='configuracao'
    )
    tema = models.CharField(max_length=20, default='claro')
    notificacoes = models.BooleanField(default=True)


# Endereço principal (opcional)
class EndereçoPrincipal(models.Model):
    cliente = models.OneToOneField(
        'Cliente',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='endereco_principal'
    )
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)


# Herança (parent_link)
class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)


class RestauranteItaliano(Restaurante):
    parent_link = models.OneToOneField(
        Restaurante,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True
    )
    especialidade_massa = models.CharField(max_length=100)
```

**⚠️ Dica:** Para criar perfil automaticamente ao criar usuário, use signals:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
```

---

### ManyToManyField (Relacionamento Muitos-para-Muitos)

| Parâmetro          | Tipo      | Padrão | Obrigatório | Descrição                        |
|--------------------|-----------|--------|-------------|----------------------------------|
| **to**             | Model/str | -      | ✅ Sim       | Model relacionado                |
| **related_name**   | str       | -      | ❌ Não       | Nome do relacionamento reverso   |
| **through**        | Model/str | -      | ❌ Não       | Tabela intermediária customizada |
| **through_fields** | tuple     | -      | ❌ Não       | Campos da tabela intermediária   |
| **db_table**       | str       | -      | ❌ Não       | Nome da tabela no BD             |
| **symmetrical**    | bool      | True   | ❌ Não       | Se relação é simétrica (self)    |
| blank              | bool      | False  | ❌ Não       | Permite vazio em forms           |

**Exemplos:**

```python
# Simples - Tags
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    tags = models.ManyToManyField(
        'Tag',
        related_name='produtos',
        blank=True
    )


class Tag(models.Model):
    nome = models.CharField(max_length=50)


# Uso:
# produto.tags.add(tag1, tag2)
# produto.tags.all()
# tag.produtos.all()

# Com tabela intermediária customizada
class Receita(models.Model):
    nome = models.CharField(max_length=200)
    ingredientes = models.ManyToManyField(
        'Ingrediente',
        through='ReceitaIngrediente',
        related_name='receitas'
    )


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)


class ReceitaIngrediente(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=20)

    class Meta:
        unique_together = ['receita', 'ingrediente']


# Uso:
# receita.ingredientes.add(ingrediente, through_defaults={'quantidade': 100, 'unidade': 'g'})

# Relacionamento self - Simétrico (amizades)
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    amigos = models.ManyToManyField(
        'self',
        symmetrical=True,  # Se A é amigo de B, B é amigo de A
        blank=True
    )


# Relacionamento self - Assimétrico (seguidores/seguindo)
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    seguidores = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='seguindo',
        blank=True
    )


# Uso:
# usuario1.seguindo.add(usuario2)  # usuario1 segue usuario2
# usuario2.seguidores.all()  # Lista quem segue usuario2

# Múltiplos relacionamentos entre models
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    alunos = models.ManyToManyField(
        'Usuario',
        related_name='cursos_como_aluno',
        blank=True
    )
    professores = models.ManyToManyField(
        'Usuario',
        related_name='cursos_como_professor',
        blank=True
    )


# Com through_fields (quando há múltiplos FKs na tabela intermediária)
class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    membros = models.ManyToManyField(
        User,
        through='Associacao',
        through_fields=('grupo', 'pessoa')  # Especifica quais FKs usar
    )


class Associacao(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    convidado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='convites_feitos'
    )
    data_entrada = models.DateTimeField(auto_now_add=True)
```

**Operações comuns com ManyToMany:**

```python
# Adicionar
produto.tags.add(tag1)
produto.tags.add(tag1, tag2, tag3)

# Remover
produto.tags.remove(tag1)
produto.tags.clear()  # Remove todas

# Verificar
if tag in produto.tags.all():
    print("Tag existe")

# Contar
total_tags = produto.tags.count()

# Filtrar
produtos_com_tag = Produto.objects.filter(tags__nome='Python')

# Criar relacionamento ao criar objeto
produto = Produto.objects.create(nome='Curso Python')
produto.tags.set([tag1, tag2])  # Define todas de uma vez
```

---

### GenericIPAddressField

| Parâmetro       | Tipo | Padrão | Obrigatório | Descrição                         |
|-----------------|------|--------|-------------|-----------------------------------|
| **protocol**    | str  | 'both' | ❌ Não       | 'both', 'IPv4', ou 'IPv6'         |
| **unpack_ipv4** | bool | False  | ❌ Não       | Descompactar IPv4 mapeado em IPv6 |
| null            | bool | False  | ❌ Não       | Permite NULL no BD                |
| blank           | bool | False  | ❌ Não       | Permite vazio em forms            |

**Exemplos:**

```python
# Aceita IPv4 e IPv6 (padrão)
ip_acesso = models.GenericIPAddressField()

# Apenas IPv4
ip_v4 = models.GenericIPAddressField(protocol='IPv4')

# Apenas IPv6
ip_v6 = models.GenericIPAddressField(protocol='IPv6', blank=True, null=True)

# Com índice para consultas rápidas
ip_origem = models.GenericIPAddressField(db_index=True)


# Exemplo de uso em log de acesso
class LogAcesso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField()
```

---

### AutoField e BigAutoField

| Parâmetro   | Tipo | Padrão | Obrigatório | Descrição                               |
|-------------|------|--------|-------------|-----------------------------------------|
| primary_key | bool | True   | ❌ Não       | Sempre True quando usado explicitamente |

**Exemplos:**

```python
# AutoField (int de 32 bits)
id = models.AutoField(primary_key=True)

# BigAutoField (int de 64 bits - padrão desde Django 3.2)
id = models.BigAutoField(primary_key=True)


# Geralmente não precisa definir explicitamente, Django cria automaticamente:
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    # Django cria automaticamente: id = models.BigAutoField(primary_key=True)
```

**Configuração global no settings.py (Django 3.2+):**

```python
# settings.py
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

---

## Exemplo Completo de Model com Diversos Tipos de Campos

```python
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import uuid


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    descricao = models.TextField(blank=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    cor = models.CharField(max_length=7, default='#000000')  # Hex color

    def __str__(self):
        return self.nome


class Produto(models.Model):
    # Identificação
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # Campos de texto
    nome = models.CharField(
        max_length=200,
        verbose_name='Nome do Produto',
        help_text='Nome completo do produto'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='URL amigável'
    )
    descricao = models.TextField(
        blank=True,
        verbose_name='Descrição',
        help_text='Descrição detalhada do produto'
    )
    especificacoes = models.TextField(
        blank=True,
        verbose_name='Especificações Técnicas'
    )

    # Campos numéricos
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name='Preço'
    )
    preco_promocional = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )
    estoque = models.PositiveIntegerField(
        default=0,
        verbose_name='Quantidade em Estoque'
    )
    estoque_minimo = models.PositiveIntegerField(
        default=10,
        help_text='Alerta quando estoque atingir este valor'
    )
    peso = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Peso (kg)',
        validators=[MinValueValidator(0)]
    )
    avaliacao = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    # Campos booleanos
    ativo = models.BooleanField(
        default=True,
        db_index=True,
        help_text='Produto visível no site'
    )
    destaque = models.BooleanField(
        default=False,
        verbose_name='Produto em Destaque'
    )
    frete_gratis = models.BooleanField(
        default=False,
        verbose_name='Frete Grátis'
    )

    # Campos de data/hora
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Última Atualização'
    )
    disponivel_em = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Disponibilidade'
    )
    fabricado_em = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Fabricação'
    )

    # Campos de arquivo
    imagem_principal = models.ImageField(
        upload_to='produtos/%Y/%m/',
        blank=True,
        null=True,
        height_field='imagem_height',
        width_field='imagem_width',
        verbose_name='Imagem Principal'
    )
    imagem_height = models.PositiveIntegerField(
        null=True,
        editable=False
    )
    imagem_width = models.PositiveIntegerField(
        null=True,
        editable=False
    )
    manual = models.FileField(
        upload_to='manuais/',
        blank=True,
        null=True,
        verbose_name='Manual do Produto'
    )

    # Campos de escolha
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('esgotado', 'Esgotado'),
        ('pre_venda', 'Pré-venda'),
        ('descontinuado', 'Descontinuado'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='disponivel',
        db_index=True
    )

    CONDICAO_CHOICES = [
        ('novo', 'Novo'),
        ('usado', 'Usado'),
        ('recondicionado', 'Recondicionado'),
    ]
    condicao = models.CharField(
        max_length=20,
        choices=CONDICAO_CHOICES,
        default='novo'
    )

    # Relacionamentos
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='produtos',
        verbose_name='Categoria'
    )
    criado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='produtos_criados',
        verbose_name='Criado Por'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='produtos',
        verbose_name='Tags'
    )
    produtos_relacionados = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='relacionado_com',
        verbose_name='Produtos Relacionados'
    )

    # Campos extras
    metadados = models.JSONField(
        default=dict,
        blank=True,
        verbose_name='Metadados',
        help_text='Dados extras em formato JSON'
    )
    caracteristicas = models.JSONField(
        default=list,
        blank=True,
        verbose_name='Características'
    )

    # Campos de URL
    video_url = models.URLField(
        max_length=500,
        blank=True,
        verbose_name='URL do Vídeo'
    )
    fabricante_site = models.URLField(
        max_length=200,
        blank=True,
        verbose_name='Site do Fabricante'
    )

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['categoria', 'ativo']),
            models.Index(fields=['status']),
            models.Index(fields=['-criado_em']),
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(preco__gte=0),
                name='preco_nao_negativo'
            ),
        ]

    def __str__(self):
        return self.nome

    def get_preco_final(self):
        """Retorna preço promocional se existir, senão retorna preço normal"""
        return self.preco_promocional if self.preco_promocional else self.preco

    def esta_disponivel(self):
        """Verifica se produto está disponível para venda"""
        return self.ativo and self.estoque > 0 and self.status == 'disponivel'

    def precisa_reposicao(self):
        """Verifica se estoque está abaixo do mínimo"""
        return self.estoque <= self.estoque_minimo

    def save(self, *args, **kwargs):
        # Lógica customizada antes de salvar
        if self.estoque == 0 and self.status == 'disponivel':
            self.status = 'esgotado'
        super().save(*args, **kwargs)


# Model de exemplo com OneToOneField
class DetalheProduto(models.Model):
    produto = models.OneToOneField(
        Produto,
        on_delete=models.CASCADE,
        related_name='detalhe',
        primary_key=True
    )
    codigo_barras = models.CharField(max_length=13, unique=True)
    ncm = models.CharField(max_length=8, blank=True)
    garantia_meses = models.PositiveSmallIntegerField(default=12)
    origem = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'Detalhes de {self.produto.nome}'


# Model de exemplo com tabela intermediária customizada
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField(
        Produto,
        through='ItemPedido',
        related_name='pedidos'
    )

    def get_total(self):
        return sum(item.get_subtotal() for item in self.itens.all())


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='itens'
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT
    )
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ['pedido', 'produto']

    def get_subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'
```

---

## Dicas Importantes

### 1. null vs blank

- **null=True**: Permite valor NULL no **banco de dados**
- **blank=True**: Permite valor vazio em **formulários**

```python
# Campos de texto: use apenas blank=True
descricao = models.TextField(blank=True)  # Salva string vazia ''

# Campos numéricos/data/boolean: use blank=True, null=True
preco_promocional = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    blank=True,
    null=True
)
```

### 2. auto_now vs auto_now_add vs default

```python
# auto_now_add: Define APENAS na criação
criado_em = models.DateTimeField(auto_now_add=True)

# auto_now: Atualiza TODA VEZ que salvar
atualizado_em = models.DateTimeField(auto_now=True)

# default: Valor padrão se não fornecido (pode ser editado)
publicado_em = models.DateTimeField(default=timezone.now)
```

### 3. related_name

Sempre defina `related_name` em ForeignKey para evitar conflitos:

```python
# BOM
criado_por = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='produtos_criados'
)
atualizado_por = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='produtos_atualizados'
)

# RUIM (causará erro de conflito)
criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE)
```

### 4. Choices - Use TextChoices (Django 3.0+)

```python
# NOVO (recomendado)
class Status(models.TextChoices):
    DISPONIVEL = 'disponivel', 'Disponível'
    ESGOTADO = 'esgotado', 'Esgotado'
    DESCONTINUADO = 'descontinuado', 'Descontinuado'


status = models.CharField(
    max_length=20,
    choices=Status.choices,
    default=Status.DISPONIVEL
)

# ANTIGO (ainda funciona)
STATUS_CHOICES = [
    ('disponivel', 'Disponível'),
    ('esgotado', 'Esgotado'),
]
status = models.CharField(max_length=20, choices=STATUS_CHOICES)
```

### 5. Indexação

Use `db_index=True` em campos frequentemente usados em queries:

```python
slug = models.SlugField(unique=True, db_index=True)
categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_index=True)


# Ou use Meta.indexes para índices compostos
class Meta:
    indexes = [
        models.Index(fields=['categoria', 'ativo']),
        models.Index(fields=['-criado_em']),
    ]
```

### 6. Validadores

```python
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    EmailValidator,
    URLValidator,
    FileExtensionValidator
)

preco = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(0), MaxValueValidator(1000000)]
)

email = models.EmailField(validators=[EmailValidator()])

arquivo = models.FileField(
    upload_to='documentos/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
)
```

### 7. Upload de Arquivos

```python
# Função para path dinâmico
def produto_image_path(instance, filename):
    # Arquivo será salvo em MEDIA_ROOT/produtos/<id>/<filename>
    return f'produtos/{instance.id}/{filename}'


imagem = models.ImageField(upload_to=produto_image_path)

# Ou com data
documento = models.FileField(upload_to='documentos/%Y/%m/%d/')
```

### 8. JSONField - Exemplos de Uso

```python
# Configurações flexíveis
configuracoes = models.JSONField(default=dict)
# configuracoes = {"tema": "escuro", "notificacoes": True}

# Lista de valores
tags = models.JSONField(default=list)
# tags = ["python", "django", "web"]

# Dados estruturados
endereco = models.JSONField(default=dict)
# endereco = {
#     "rua": "Av. Principal",
#     "numero": "100",
#     "cidade": "São Paulo",
#     "cep": "01000-000"
# }
```

---

## Resumo de Quando Usar Cada Campo

| Necessidade                | Campo Recomendado                 |
|----------------------------|-----------------------------------|
| Nome, título curto         | CharField                         |
| Descrição longa            | TextField                         |
| Quantidade, idade          | PositiveIntegerField              |
| Preço, dinheiro            | DecimalField                      |
| Coordenadas GPS            | FloatField                        |
| Sim/Não, Ativo/Inativo     | BooleanField                      |
| Data de nascimento         | DateField                         |
| Data e hora de criação     | DateTimeField (auto_now_add=True) |
| Horário de funcionamento   | TimeField                         |
| Email                      | EmailField                        |
| Website, link              | URLField                          |
| URL amigável               | SlugField                         |
| Token único                | UUIDField                         |
| PDF, documento             | FileField                         |
| Foto, imagem               | ImageField                        |
| Configurações variáveis    | JSONField                         |
| Categoria de produto       | ForeignKey                        |
| Perfil de usuário          | OneToOneField                     |
| Tags, múltiplas categorias | ManyToManyField                   |
| IP de acesso               | GenericIPAddressField             |

---

## Checklist de Boas Práticas

- [ ] Sempre defina `verbose_name` para melhor leitura no Admin
- [ ] Use `help_text` para campos que precisam de explicação
- [ ] Defina `related_name` em relacionamentos para evitar conflitos
- [ ] Use `blank=True` para campos opcionais em formulários
- [ ] Use `null=True` apenas quando necessário no banco
- [ ] Prefira `TextChoices` ao invés de tuplas para choices
- [ ] Adicione `db_index=True` em campos usados em filtros frequentes
- [ ] Use `validators` para validações customizadas
- [ ] Defina `__str__()` em todos os models
- [ ] Adicione `Meta.ordering` para ordenação padrão
- [ ] Use `auto_now_add` para data de criação
- [ ] Use `auto_now` para data de atualização
- [ ] Sempre especifique `on_delete` em ForeignKey
- [ ] Use `upload_to` com função para organizar arquivos
- [ ] Adicione `Meta.indexes` para otimizar consultas complexas

---

## Referências Úteis

- [Documentação Oficial - Model Field Reference](https://docs.djangoproject.com/en/stable/ref/models/fields/)
- [Documentação Oficial - Field Options](https://docs.djangoproject.com/en/stable/ref/models/fields/#field-options)
- [Documentação Oficial - Relationship Fields](https://docs.djangoproject.com/en/stable/ref/models/fields/#module-django.db.models.fields.related)

---

**Criado para: FPFTech - Curso de Django Backend**  
**Instrutor: Douglas**  
**Data: 2026**
