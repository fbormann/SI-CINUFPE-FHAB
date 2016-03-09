import numpy as np

class Perceptron:

	def __init__(self):
		self.__weights = []

	def __classify__(self, X_test):
		outputs = []
		test_vector = X_test.values
		for example in test_vector:
			outputs.append(self.__classifyInstance__(example))
			
		mean = sum(outputs)/len(outputs)
		print("Mean is" + str(mean)) #Only for test purposes
		i = 0
		for value in outputs:
			if value >= mean:
				outputs[i] = 1
			else:
				outputs[i] = 0
			i += 1
		return outputs


	def __classifyInstance__(self, example):
		output = 0
		i = 0
		for value in example[:len(example)-1]:
			output += value*self.__weights[i]
			i += 1
		return output

	def __learningAlgorithm__(self, X_train):
		for i in range(len(X_train.columns)): #initialize the weights in 0
			self.__weights.append(0)
			#print(len(self.__weights))

		train_vector = X_train.values
		one_incorrect = True
		amount = 0
		while one_incorrect and amount <= 100:
			one_incorrect = False
			amount += 1
			for example in train_vector:
				output = self.__classifyInstance__(example)
				if example[len(example)-1] == 1: #N Foi classificado corretamente
					if output <= 0:
						one_incorrect = True
						self.__add__(example)
				else: # == 0
					if output >= 0:
						one_incorrect = True
						self.__subtract__(example)


	def __add__(self, example):
		i = 0
		for value in example[:len(example)-1]:
			self.__weights[i] += value
			i += 1

	def __subtract__(self, example):
		i = 0
		for value in example[:len(example)-1]:
			self.__weights[i] -= value
			i += 1

