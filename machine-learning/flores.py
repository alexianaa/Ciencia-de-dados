from sklearn.model_selection import train_test_split # Modulo de divisão dos dados
from sklearn.metrics import accuracy_score, confusion_matrix # Modulo para avaliação
from sklearn import  datasets # Dados do dataset Iris
from sklearn import neighbors # Modulo do modelo KNN
from sklearn import tree # Modulo do modelo Arvore de Decisao

iris = datasets.load_iris()
""" print(iris.target_names)
print(iris.feature_names)
print(iris.target) """

# Dados de entrada
x = iris.data

# Rótulos
y = iris.target

# Divisão de dados para treinamento e teste na proporção 70/30
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x,y,test_size=.3)

# Definição do modelo de Árvore de Decisão
classificador_arvore = tree.DecisionTreeClassifier()

# Definição do modelo KNN
classificador_knn = neighbors.KNeighborsClassifier()

# Treinamento dos modelos
classificador_arvore.fit(x_treinamento,y_treinamento)
classificador_knn.fit(x_treinamento,y_treinamento)

# Fazer predições
arvore_predicoes = classificador_arvore.predict(x_teste)
knn_predicoes = classificador_knn.predict(x_teste)

# Avaliação das predições do modelo classificador_arvore
print(accuracy_score(y_teste, arvore_predicoes))

# Avaliação das predições do modelo classificador_knn
print(accuracy_score(y_teste, knn_predicoes))

print(confusion_matrix(y_teste, knn_predicoes))
