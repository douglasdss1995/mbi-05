"""
Pandas - Biblioteca para análise e manipulação de dados
Muito usada em ciência de dados, análise, e preparação de dados para Django
"""

import pandas as pd

# ============================================
# 1. SERIES - Array unidimensional com índices
# ============================================

# Criar Series a partir de lista
notas = pd.Series([8.5, 9.0, 7.5, 10.0])
print(notas)
# 0    8.5
# 1    9.0
# 2    7.5
# 3    10.0

# Series com índices personalizados
notas = pd.Series([8.5, 9.0, 7.5, 10.0], index=["João", "Maria", "Pedro", "Ana"])
print(notas["Maria"])  # 9.0

# ============================================
# 2. DATAFRAME - Tabela com linhas e colunas
# ============================================

# Criar DataFrame a partir de dicionário
dados = {
    "nome": ["João", "Maria", "Pedro", "Ana"],
    "idade": [25, 30, 22, 28],
    "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília"],
    "salario": [3000, 4500, 2800, 5000],
}

df = pd.DataFrame(dados)
print(df)
#     nome  idade          cidade  salario
# 0   João     25       São Paulo     3000
# 1  Maria     30  Rio de Janeiro     4500
# 2  Pedro     22  Belo Horizonte     2800
# 3    Ana     28        Brasília     5000

# ============================================
# 3. VISUALIZAÇÃO E INFORMAÇÕES
# ============================================

# Primeiras linhas
df.head(2)  # Primeiras 2 linhas

# Últimas linhas
df.tail(2)  # Últimas 2 linhas

# Informações do DataFrame
df.info()  # Tipos de dados, valores nulos, memória

# Estatísticas descritivas
df.describe()  # count, mean, std, min, max, etc.

# Forma (linhas, colunas)
df.shape  # (4, 4)

# Nomes das colunas
df.columns  # ['nome', 'idade', 'cidade', 'salario']

# Tipos de dados
df.dtypes

# ============================================
# 4. SELEÇÃO DE DADOS
# ============================================

# Selecionar uma coluna (retorna Series)
df["nome"]
df.nome  # Alternativa (não funciona se nome tem espaços)

# Selecionar múltiplas colunas (retorna DataFrame)
df[["nome", "salario"]]

# Selecionar linhas por índice (iloc = index location)
df.iloc[0]  # Primeira linha
df.iloc[0:2]  # Primeiras 2 linhas
df.iloc[:, 0]  # Primeira coluna

# Selecionar linhas por label (loc = location)
df.loc[0]  # Linha com índice 0
df.loc[0:2, ["nome", "salario"]]  # Linhas 0-2, colunas específicas

# ============================================
# 5. FILTROS (MUITO USADO!)
# ============================================

# Filtrar por condição
df[df["idade"] > 25]  # Pessoas com mais de 25 anos
df[df["salario"] >= 4000]  # Salário >= 4000

# Múltiplas condições
df[(df["idade"] > 25) & (df["salario"] > 3000)]  # AND
df[(df["cidade"] == "São Paulo") | (df["cidade"] == "Brasília")]  # OR

# Filtrar com isin (igual SQL IN)
df[df["cidade"].isin(["São Paulo", "Brasília"])]

# Filtrar strings
df[df["nome"].str.startswith("M")]  # Começa com M
df[df["nome"].str.contains("a")]  # Contém 'a'

# ============================================
# 6. MANIPULAÇÃO DE DADOS
# ============================================

# Adicionar nova coluna
df["bonus"] = df["salario"] * 0.10
df["salario_total"] = df["salario"] + df["bonus"]

# Modificar valores
df.loc[0, "salario"] = 3500  # Modifica salário de João

# Renomear colunas
df.rename(columns={"nome": "funcionario", "idade": "anos"}, inplace=True)
# inplace=True modifica o DataFrame original

# Remover colunas
df.drop(columns=["bonus"], inplace=True)

# Remover linhas
df.drop(index=[0, 1], inplace=True)  # Remove linhas 0 e 1

# Ordenar
df.sort_values("salario", ascending=False)  # Maior salário primeiro
df.sort_values(["cidade", "idade"])  # Múltiplas colunas

# ============================================
# 7. AGRUPAMENTO (GROUP BY - IGUAL SQL)
# ============================================

# Exemplo com mais dados
dados_vendas = {
    "vendedor": ["João", "Maria", "João", "Pedro", "Maria", "Pedro"],
    "produto": ["Notebook", "Mouse", "Teclado", "Mouse", "Notebook", "Teclado"],
    "quantidade": [2, 5, 3, 8, 1, 4],
    "valor": [3000, 50, 150, 50, 3000, 150],
}
df_vendas = pd.DataFrame(dados_vendas)

# Agrupar e somar
df_vendas.groupby("vendedor")["valor"].sum()

# Múltiplas agregações
df_vendas.groupby("vendedor").agg(
    {
        "quantidade": "sum",
        "valor": ["sum", "mean"],
    }  # Total de quantidade  # Total e média de valor
)

# ============================================
# 8. VALORES NULOS (MUITO IMPORTANTE!)
# ============================================

# Criar DataFrame com valores nulos
dados_nulos = {
    "nome": ["João", "Maria", None, "Ana"],
    "idade": [25, None, 22, 28],
    "salario": [3000, 4500, 2800, None],
}
df_nulos = pd.DataFrame(dados_nulos)

# Verificar valores nulos
df_nulos.isnull()  # Retorna True/False para cada célula
df_nulos.isnull().sum()  # Conta quantos nulos por coluna

# Remover linhas com valores nulos
df_nulos.dropna()  # Remove qualquer linha com pelo menos um nulo
df_nulos.dropna(subset=["nome"])  # Remove apenas se 'nome' for nulo

# Preencher valores nulos
df_nulos.fillna(0)  # Preenche com 0
df_nulos.fillna({"idade": 0, "salario": 2500})  # Valores diferentes por coluna
df_nulos["idade"].fillna(df_nulos["idade"].mean())  # Preenche com a média

# ============================================
# 9. LEITURA E ESCRITA DE ARQUIVOS
# ============================================

# CSV (muito comum!)
# df.to_csv('dados.csv', index=False)  # Salvar
# df_csv = pd.read_csv('dados.csv')  # Ler

# Excel
# df.to_excel('dados.xlsx', index=False)
# df_excel = pd.read_excel('dados.xlsx')

# JSON
# df.to_json('dados.json', orient='records')
# df_json = pd.read_json('dados.json')

# SQL (IMPORTANTE para Django!)
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///db.sqlite3')
# df.to_sql('tabela', engine, if_exists='replace')
# df_sql = pd.read_sql('SELECT * FROM tabela', engine)

# ============================================
# 10. OPERAÇÕES ÚTEIS
# ============================================

# Contar valores únicos
df["cidade"].nunique()  # Quantidade de cidades únicas
df["cidade"].value_counts()  # Conta cada valor

# Aplicar função personalizada
df["salario_formatado"] = df["salario"].apply(lambda x: f"R$ {x:,.2f}")

# Map (substituir valores)
mapa_cidades = {"São Paulo": "SP", "Rio de Janeiro": "RJ", "Brasília": "DF"}
df["uf"] = df["cidade"].map(mapa_cidades)

# Merge (JOIN - IGUAL SQL)
df_bonus = pd.DataFrame({"nome": ["João", "Maria", "Ana"], "bonus": [500, 800, 600]})
df_completo = pd.merge(df, df_bonus, on="nome", how="left")

# Concatenar DataFrames
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
pd.concat([df1, df2], ignore_index=True)  # Empilha verticalmente

# ============================================
# 11. DATAS (IMPORTANTE!)
# ============================================

# Criar coluna de data
df["data_contratacao"] = pd.to_datetime(
    ["2020-01-15", "2021-05-20", "2019-11-10", "2022-03-25"]
)

# Extrair partes da data
df["ano"] = df["data_contratacao"].dt.year
df["mes"] = df["data_contratacao"].dt.month
df["dia_semana"] = df["data_contratacao"].dt.day_name()

# Diferença entre datas
hoje = pd.Timestamp.now()
df["dias_empresa"] = (hoje - df["data_contratacao"]).dt.days

# ============================================
# USO COM DJANGO
# ============================================

"""
# Converter QuerySet Django para DataFrame
from myapp.models import Cliente

queryset = Cliente.objects.all()
df = pd.DataFrame(list(queryset.values()))

# Ou específicas colunas
df = pd.DataFrame(list(queryset.values('nome', 'idade', 'cidade')))

# Fazer análises
total_por_cidade = df.groupby('cidade')['idade'].mean()

# Exportar para Excel
df.to_excel('relatorio_clientes.xlsx', index=False)

# Bulk create no Django a partir de DataFrame
from myapp.models import Produto

objetos = [
    Produto(nome=row['nome'], preco=row['preco'])
    for _, row in df.iterrows()
]
Produto.objects.bulk_create(objetos)
"""

# ============================================
# DICAS E BOAS PRÁTICAS
# ============================================

"""
1. Use .copy() ao modificar DataFrames para evitar SettingWithCopyWarning
   df_filtrado = df[df['idade'] > 25].copy()

2. Use inplace=True com cuidado (modifica o original)

3. Para grandes volumes, use chunking ao ler arquivos:
   for chunk in pd.read_csv('arquivo_grande.csv', chunksize=10000):
       processar(chunk)

4. Use .loc e .iloc para seleções ao invés de encadeamento
   ❌ df[df['idade'] > 25]['salario'] = 5000  # Pode dar warning
   ✅ df.loc[df['idade'] > 25, 'salario'] = 5000

5. Para performance, use tipos corretos:
   df['categoria'] = df['categoria'].astype('category')
"""
