import Perceptron as pc
import pandas as pd

X_train = pd.read_csv("train.csv", header = None)
X_test = pd.read_csv("test.csv", header= None)
perceptron = pc.Perceptron()

perceptron.__learningAlgorithm__(X_train)
print(perceptron.__classify__(X_test)) #show the results
