"""
===============================================================================
EXERCÍCIOS DE FIXAÇÃO — INTERMEDIATE PYTHON (DataCamp)
Módulos: Matplotlib + Dictionaries & Pandas
===============================================================================

Autor: Claude (mentor de Caio Oliveira)
Data: Março 2026

INSTRUÇÕES:
- Resolva cada exercício SEM consultar o DataCamp.
- Se travar, tente por pelo menos 10 minutos antes de procurar ajuda.
- Rode o arquivo inteiro com: python exercicios_intermediario.py
- Cada bloco pode ser executado independentemente descomentando.
- Os exercícios marcados com [EXTRA] vão além do DataCamp — são coisas
  que você PRECISA saber mas que a plataforma não treina o suficiente.

COMO USAR:
- Descomente UM bloco de exercícios por vez
- Escreva sua solução onde diz "# SUA SOLUÇÃO AQUI"
- Compare com o resultado esperado no comentário
===============================================================================
"""
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# PARTE 1: MATPLOTLIB
# ============================================================================

# ---------------------------------------------------------------------------
# EXERCÍCIO 1.1 — Gráfico de linha básico
# Crie um gráfico de linha mostrando a evolução de temperatura ao longo
# de 7 dias. Use os dados abaixo.
# Adicione: título, label no eixo x, label no eixo y.
# ---------------------------------------------------------------------------
dias = [1, 2, 3, 4, 5, 6, 7]
temperaturas = [28, 30, 32, 29, 27, 31, 33]

# SUA SOLUÇÃO AQUI
#titulo = 'Evolução temperatura'
#x= 'Dias'
#y = ' temperatura'
#plt.plot(dias,temperaturas)
#plt.xlabel(x)
#plt.ylabel(y)
#plt.title(titulo)
#plt.show()
plt.clf()
# ---------------------------------------------------------------------------
# EXERCÍCIO 1.2 — Scatter plot com tamanho variável
# Crie um scatter plot onde:
# - eixo x = horas de estudo
# - eixo y = nota na prova
# - tamanho dos pontos = número de exercícios feitos (multiplique por 10)
# - cor = "teal"
# - transparência (alpha) = 0.7
# Adicione título e labels nos eixos.
# ---------------------------------------------------------------------------

horas_estudo = [1, 2, 3, 4, 5, 6, 7, 8]
notas = [4.0, 5.5, 6.0, 6.5, 7.0, 8.0, 8.5, 9.5]
exercicios = [5, 8, 12, 15, 20, 25, 30, 40] 
pontos = 10*np.array(exercicios)
# SUA SOLUÇÃO AQUI
#plt.scatter(horas_estudo,notas,s=pontos,c="teal",alpha = 0.7)
#plt.title('nota por horas estudadas')
#plt.xlabel('horas de estudo')
#plt.ylabel('nota da prova')
#plt.show()

# ---------------------------------------------------------------------------
# EXERCÍCIO 1.3 — Histograma
# Crie um histograma das idades abaixo com 5 bins.
# Adicione título e labels. Use a cor "coral".
# ---------------------------------------------------------------------------

idades = [18, 19, 20, 21, 22, 23, 24, 25, 19, 20, 21, 22, 22, 23, 23,
          24, 25, 26, 27, 20, 21, 22, 23, 24, 30, 31, 19, 20, 22, 28]

# SUA SOLUÇÃO AQUI
#plt.hist(idades,bins=5,color="coral")
#plt.title('idades')
#plt.show()

# ---------------------------------------------------------------------------
# EXERCÍCIO 1.4 — Customização avançada
# Usando os dados do exercício 1.1:
# a) Crie o gráfico de linha
# b) Mude os ticks do eixo x para mostrar "Seg", "Ter", "Qua", "Qui",
#    "Sex", "Sab", "Dom"
# c) Adicione uma linha horizontal tracejada vermelha na temperatura
#    média (use sum()/len() para calcular)
# d) Adicione texto "Média" próximo à linha horizontal
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI
#media = sum(temperaturas)/len(temperaturas)
#titulo = 'Evolução temperatura'
#x= 'Dias'
#y = ' temperatura'
#plt.plot(dias,temperaturas)
#plt.xlabel(x)
#plt.ylabel(y)
#plt.title(titulo)
#plt.xticks(dias, ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'])
#plt.axhline(media,ls='--',label='média')
#plt.legend()
#plt.show()


# ---------------------------------------------------------------------------
# [EXTRA] EXERCÍCIO 1.5 — Subplots (DataCamp não cobre bem isso)
# Crie uma figura com 1 linha e 2 colunas de gráficos:
# - Esquerda: gráfico de linha das temperaturas
# - Direita: histograma das temperaturas
# Use plt.subplots() e o objeto axes retornado. 
# Dica: fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(dias, temperaturas)
ax2.hist(temperaturas,bins=6,)
plt.show()

# ---------------------------------------------------------------------------
# [EXTRA] EXERCÍCIO 1.6 — Múltiplas séries no mesmo gráfico
# Plote as vendas de dois produtos no mesmo gráfico de linha.
# Adicione uma legenda para diferenciar os produtos.
# Dica: use o argumento "label" em cada plt.plot() e depois plt.legend()
# ---------------------------------------------------------------------------

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas_produto_a = [100, 120, 140, 130, 150, 170]
vendas_produto_b = [80, 90, 110, 140, 135, 160]

# SUA SOLUÇÃO AQUI


# ============================================================================
# PARTE 2: DICIONÁRIOS
# ============================================================================

# ---------------------------------------------------------------------------
# EXERCÍCIO 2.1 — Criar e acessar dicionário
# Crie um dicionário chamado "aluno" com as chaves:
# "nome", "idade", "curso", "semestre"
# Preencha com seus dados reais.
# Depois, printe apenas o valor da chave "curso".
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# EXERCÍCIO 2.2 — Adicionar e remover chaves
# Partindo do dicionário "aluno" do exercício anterior:
# a) Adicione a chave "universidade" com valor "SENAI CIMATEC"
# b) Adicione a chave "linguagens" com uma LISTA: ["Python", "SQL"]
# c) Remova a chave "idade" usando del
# d) Printe o dicionário completo
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# EXERCÍCIO 2.3 — Dicionário de dicionários (aninhado)
# Crie um dicionário chamado "turma" onde cada chave é o nome de um aluno
# e o valor é outro dicionário com "nota" e "frequencia".
# Exemplo: turma = {"Ana": {"nota": 8.5, "frequencia": 90}, ...}
# Crie para 3 alunos.
# Depois, acesse e printe a nota do segundo aluno.
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# [EXTRA] EXERCÍCIO 2.4 — Iterar sobre dicionário
# Usando o dicionário "turma" do exercício anterior:
# a) Use um loop for para printar cada aluno e sua nota no formato:
#    "Ana: nota 8.5"
# Dica: use .items() para acessar chave e valor ao mesmo tempo
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# [EXTRA] EXERCÍCIO 2.5 — Verificar existência de chave
# Dado o dicionário abaixo, escreva um código que:
# a) Verifica se a chave "email" existe. Se sim, printa o email.
#    Se não, printa "Email não cadastrado".
# b) Use o método .get() para acessar a chave "telefone" com valor
#    padrão "Não informado".
# Dica: "chave" in dicionario retorna True/False
# ---------------------------------------------------------------------------

cadastro = {"nome": "Caio", "curso": "Eng. Computação", "cidade": "Salvador"}

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# [EXTRA] EXERCÍCIO 2.6 — Dictionary comprehension
# (DataCamp NÃO ensina isso, mas é essencial)
# Dada a lista de nomes abaixo, crie um dicionário onde:
# - chave = nome
# - valor = número de caracteres do nome
# Faça em UMA linha usando dictionary comprehension.
# Resultado esperado: {"Ana": 3, "Carlos": 6, "Maria": 5, "João": 4}
# ---------------------------------------------------------------------------

nomes = ["Ana", "Carlos", "Maria", "João"]

# SUA SOLUÇÃO AQUI


# ============================================================================
# PARTE 3: PANDAS
# ============================================================================

import pandas as pd

# ---------------------------------------------------------------------------
# EXERCÍCIO 3.1 — Criar DataFrame a partir de dicionário
# Crie um DataFrame com dados de 5 cidades brasileiras contendo:
# - nome da cidade
# - estado (sigla)
# - população (em milhões, pode ser aproximado)
# - área (km², pode ser aproximado)
# Use o nome da cidade como índice do DataFrame (index).
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# EXERCÍCIO 3.2 — Seleção com loc e iloc
# Usando o DataFrame do exercício anterior:
# a) Selecione APENAS a coluna "populacao" usando colchetes simples
# b) Selecione a coluna "populacao" como DataFrame (colchetes duplos)
# c) Use .loc[] para selecionar a linha de uma cidade específica
# d) Use .iloc[] para selecionar a terceira linha
# e) Use .loc[] para selecionar populacao e area de duas cidades
# Printe cada resultado separadamente com um print("--- a) ---") antes.
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# EXERCÍCIO 3.3 — Criar DataFrame a partir de CSV (simulado)
# Primeiro, crie um arquivo CSV com os dados abaixo usando Python.
# Depois, leia ele com pd.read_csv().
#
# Conteúdo do CSV:
# produto,preco,quantidade,categoria
# Notebook,3500,10,Eletrônicos
# Mouse,80,50,Periféricos
# Teclado,150,30,Periféricos
# Monitor,1200,15,Eletrônicos
# Webcam,200,25,Periféricos
# Headset,300,20,Áudio
#
# Dica para criar o CSV:
# with open("produtos.csv", "w") as f:
#     f.write("produto,preco,quantidade,categoria\n")
#     f.write("Notebook,3500,10,Eletrônicos\n")
#     ... etc
#
# Depois de ler, defina a coluna "produto" como índice.
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# EXERCÍCIO 3.4 — Criar colunas calculadas
# Usando o DataFrame de produtos (exercício 3.3):
# a) Crie uma nova coluna "valor_total" = preco * quantidade
# b) Crie uma nova coluna "preco_com_desconto" = preco * 0.9
# c) Printe o DataFrame atualizado
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# [EXTRA] EXERCÍCIO 3.5 — Métodos descritivos
# (DataCamp menciona por cima, mas você precisa dominar)
# Usando o DataFrame de produtos:
# a) Use .describe() e observe o resultado
# b) Calcule a média da coluna "preco" com .mean()
# c) Encontre o produto mais caro com .max() e .idxmax()
# d) Conte quantos produtos tem em cada categoria com .value_counts()
# e) Calcule a soma total da coluna "valor_total"
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# [EXTRA] EXERCÍCIO 3.6 — Filtragem com condições booleanas
# (Isso aparece no módulo 3 do DataCamp, mas é tão importante que
# você deveria praticar agora)
# Usando o DataFrame de produtos:
# a) Filtre apenas produtos com preço acima de 200
# b) Filtre apenas produtos da categoria "Periféricos"
# c) Filtre produtos com preço > 100 E quantidade > 20
# d) Filtre produtos que são "Eletrônicos" OU custam menos de 100
# Printe cada resultado.
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# [EXTRA] EXERCÍCIO 3.7 — Ordenação
# Usando o DataFrame de produtos:
# a) Ordene por preço do menor para o maior
# b) Ordene por preço do maior para o menor
# c) Ordene por categoria (alfabético) e depois por preço (decrescente)
# Dica: use .sort_values()
# ---------------------------------------------------------------------------

# SUA SOLUÇÃO AQUI


# ============================================================================
# DESAFIO FINAL — INTEGRAÇÃO
# ============================================================================

# ---------------------------------------------------------------------------
# EXERCÍCIO 4.1 — Juntando tudo
# Este exercício integra matplotlib, dicionários e pandas.
#
# Contexto: Você tem dados de vendas mensais de uma loja.
#
# Tarefas:
# 1) Crie o dicionário com os dados abaixo
# 2) Converta para DataFrame
# 3) Crie uma coluna "receita" = preco_medio * unidades_vendidas
# 4) Encontre o mês com maior receita
# 5) Calcule a receita total do semestre
# 6) Crie um gráfico de BARRAS (plt.bar) mostrando a receita por mês
#    com título, labels nos eixos, e o valor de receita total no título
# ---------------------------------------------------------------------------

dados_vendas = {
    "mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "unidades_vendidas": [150, 200, 180, 220, 250, 300],
    "preco_medio": [45.0, 42.0, 48.0, 44.0, 46.0, 50.0]
}

# SUA SOLUÇÃO AQUI


# ---------------------------------------------------------------------------
# [EXTRA] EXERCÍCIO 4.2 — Pensamento analítico
# Este não é de código. Responda em comentários:
#
# Olhando para os dados de vendas acima:
# a) As vendas estão crescendo, caindo, ou estáveis? Justifique.
# b) O mês com mais unidades vendidas é o mesmo com maior receita? Por quê?
# c) Se você fosse o dono da loja, que decisão tomaria baseado nesses dados?
#
# (Este tipo de pergunta é o que diferencia um programador de um
# analista de dados. Não ignore.)
# ---------------------------------------------------------------------------

# SUAS RESPOSTAS AQUI (em comentários):
# a)
# b)
# c)


#print("\n" + "="*60)
#print("Parabéns por completar os exercícios!")
#print("Rode cada bloco, confira os resultados, e me manda")
#print("os que te deram mais dificuldade.")
#print("="*60)
