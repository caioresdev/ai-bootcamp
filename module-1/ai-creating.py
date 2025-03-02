# Criar um previsor de preços de casa utilizando um dataset pronto.

# Importando as bibliotecas
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Carregando o dataset
housing = datasets.fetch_california_housing()

# Criando um DataFrame
df = pd.DataFrame(data=housing.data, columns=housing.feature_names)
df.head()

# Dividindo o dataset em treino e teste
dfTarget = pd.DataFrame(housing.target, columns=housing.target_names)
dfTarget.head()

X = df
y = dfTarget

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Normalizando os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

# Transformando os dados em DataFrame
X_train_Scaled = pd.DataFrame(X_train, columns=X.columns)
X_test_Scaled = pd.DataFrame(X_test, columns=X.columns)

# Treinando o modelo
reg = LinearRegression().fit(X_train_Scaled, y_train)
results = reg.predict(X_test_Scaled)

# Avaliando o modelo
score_model = reg.score(X_test_Scaled, y_test)
print(score_model)