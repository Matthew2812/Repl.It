#Checando as versões das bibliotecas
 
#Imprimindo versões de cada biblioteca
#Python versão
import sys
print('Python: {}'.format(sys.version))
#Scipy versão
import scipy
print('Scipy: {}'.format(scipy.__version__))
#Numpy versão
import numpy
print('Numpy: {}'.format(numpy.__version__))
#Matplotib versão
import matplotlib
print('Matplotlib: {}'.format(matplotlib.__version__))
#Pandas versão
import pandas
print('Pandas: {}'.format(pandas.__version__))
#Scikit-Learn Versão
import sklearn
print('Sklearn: {}'.format(sklearn.__version__))

#Carregando bibliotecas que serão utilizadas
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#Carregando o conjunto de dados
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

#Configuração (Quantidade de linhas(instâncias) e colunas(atributos))
print("Configuração dos dados (Linhas e Colunas):", dataset.shape)

#Primeiras 20 linhas do conjunto de dados
print(dataset.head(20))

#Sumário para cada atributo (linhas, média, normal, menor, 25%, 50%, 75%, máximo)
print(dataset.describe())

#Distribuição da classe
print("\n")
print(dataset.groupby("class").size())

#Diagrama de caixa e bigode de cada classe
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.savefig("Diagrama de Caixa e Bigode de cada classe.png")

#Histograma de cada variável
dataset.hist()
plt.savefig("Histograma dos Dados de cada variável.png")

#Gráfico de pontos
scatter_matrix(dataset)
plt.savefig("Gráfico de pontos do conjunto de dados")

#Dividindo o conjunto de dados
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
print("Vetor de dados:\n", array)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

#Algoritmos de Verificação Pontual
models = []
print("\nLogistic Regression = LR")
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
print("Linear Discriminant Analysis = LDA")
models.append(('LDA', LinearDiscriminantAnalysis()))
print("KNeighborsClassifier = KNN")
models.append(('KNN', KNeighborsClassifier()))
print("DecisionTreeClassifier = CART")
models.append(('CART', DecisionTreeClassifier()))
print("GaussianNB = NB")
models.append(('NB', GaussianNB()))
print("SVC = SVM\n")
models.append(('SVM', SVC(gamma='auto')))
#Avaliando cada modelo
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print("Mensagem:",msg)

# Comparando Algoritmos
fig = plt.figure()
fig.suptitle('Comparação de Algoritmos')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.savefig("Diagrama de Caixa e Bigode: Comparação de Algoritmos")

#Previsões da validação do conjunto de dados
sv = SVC()
sv.fit(X_train, Y_train)
predictions = sv.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))