import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv')

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=gasolina_df, marker='o', color='b', label='Preço da Gasolina')

plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.title('Variação do Preço da Gasolina ao Longo do Tempo')

plt.legend()
plt.savefig('gasolina.png')
plt.show()