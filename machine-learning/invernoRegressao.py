import pandas as pd
from neuralprophet import NeuralProphet
from matplotlib import pyplot as plt

url='https://drive.google.com/file/d/1RZ1DX76zAA5GDKaQnaVFOB3KMoLiWxHh/view?usp=sharing'
file_id=url.split('/')[-2]
dwn_url='https://drive.google.com/uc?id=' + file_id

df = pd.read_csv(dwn_url)
# print(df.tail())
# print(df.Date.unique())
# print(df.columns)
# print(df.dtypes)

df ['Date'] = pd.to_datetime(df ['Date'])
# print(df.dtypes)

plt.plot(df ['Date'], df ['TempAvgF'])
plt.show()

new_column = df[['Date', 'TempAvgF']]
new_column.dropna(inplace=True)
new_column.columns = ['ds', 'y'] 
print(new_column.tail())

# Carregar modelo
n = NeuralProphet()

# Treinamento
model = n.fit(new_column, freq='D')

# Predições para 1500 dias
future = n.make_future_dataframe(new_column, periods=1500)

# Gerar predições
forecast = n.predict(future)
#print(forecast.tail())

plot = n.plot(forecast)