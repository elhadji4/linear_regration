
import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math

def show_data(df):
	"""
	1 - initialiser la figure
	2 - indiquer ce que l'on veut dessiner dans la figure
	3 - afficher le graphique
	"""
	plt.figure(figsize=(15, 6))
	plt.plot(df["surface"], df["prix"], "bo")
	plt.show()



def prepare_data(df):
	"""
	Cette fonction split le jeu de donnée en de groupe train / test
	"""
	split_index = int(len(df) * 0.75)
	train_df = df.iloc[ : split_index]
	test_df = df.iloc[split_index : ]

	x_train = train_df[ ["surface"] ]
	y_train = train_df[ ["prix"] ]

	x_test = test_df[ ["surface"] ]
	y_test = test_df[ ["prix"] ]

	return x_train, y_train, x_test, y_test


def regression(x_train, y_train):
	model = LinearRegression()
	model.fit(x_train, y_train)
	return model


def test_model(model, x_test, y_test):
	y_test_predicted = model.predict(x_test)

	rmse = math.sqrt(1/len(x_test) * sum((y_test.values - y_test_predicted)**2))
	print(rmse)

	plt.figure(figsize=(15, 6))
	plt.plot(x_test, y_test, "bo")
	plt.plot(x_test, y_test_predicted, "ro")
	plt.show()

data_df = pandas.read_csv("./prix_maisons.csv")
#show_data(df=data_df)
x_train, y_train, x_test, y_test = prepare_data(df=data_df)
model = regression(x_train, y_train)
test_model(model, x_test, y_test)