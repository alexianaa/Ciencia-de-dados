# Importando os módulos necessários
import matplotlib.pyplot as plt # Módulo de geração de gráficos
import pandas as pd # Módulo de manipulação de tabelas

# Contruindo o link de importação dos dados do restaurante de João
url='https://drive.google.com/file/d/1QWHUHWhcW-EiL6PX94AmVipaVmK6ZDxN/view?usp=sharing'
file_id=url.split('/')[-2]
dwn_url='https://drive.google.com/uc?id=' + file_id

# Download dos dados do restaurante
df = pd.read_csv(dwn_url)

# Mostrar linhas inicias da tabela
print(df.head())

# Figura onde o gráfico será construido
fig = plt.figure()

# Adicionar os eixos do gráfico
ax = fig.add_axes([0,0,1,1])

# Armazenando os dados de horas na variável x
x = df['hora']

# Armazenando os dados de ocupação na variável y
y = df['ocupacao']

# Uso do gráfico de barras
ax.bar(x, y)

# Rótulo do eixo x
plt.xlabel("Hora")

# Rótulo do eixo y
plt.ylabel("Ocupação")

# Título do gráfico
plt.title("Gráfico de Horário x Ocupação", fontsize=20)

# Aumentar tamanho da fonte dos rótulos dos eixos x e y
plt.rc('axes', labelsize=15)

# Aumentar tamanho da fonte dos elementos do eixo x
plt.rc('xtick', labelsize=15)

# Aumentar tamanho da fonte dos elementos do eixo y
plt.rc('ytick', labelsize=15)

# Mostrar o gráfico
plt.show()

""" 
# Armazenando os dados de ? na variável x
x = df['hora']

# Armazenando os dados de ? na variável y
y = df['temperatura']

# Crie o gráfico das Horas x Temperatura
plt.plot(x, y)

# Rótulo do eixo x
plt.xlabel("Hora")

# Rótulo do eixo y
plt.ylabel("Temperatura ºC")

# Título do gráfico e tamanho da fonte
plt.title("Gráfico Ocupação x Temperatura", fontsize=20)

# Aumentar tamanho da fonte dos rótulos dos eixos x e y
plt.rc('axes', labelsize=15)

# Aumentar tamanho da fonte dos elementos do eixo x
plt.rc('xtick', labelsize=15)

# Aumentar tamanho da fonte dos elementos do eixo y
plt.rc('ytick', labelsize=15)

# Mostrar o gráfico
plt.show()
"""