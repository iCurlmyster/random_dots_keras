from keras.models import Sequential
from keras.layers import Dense, Dropout
import numpy as np
import csv

np.random.seed(7)

with open("./blue_red_sample.csv",newline='') as csvfile:
	f_read = csv.reader(csvfile, delimiter=',')
	dataset = []
	for row in f_read:
		dataset.append(np.array(row))

dataset = np.array(dataset)

x = dataset[:,1:3]
y = dataset[:,0]
y = [1.0 if "blue" in x else 0.0 for x in y]
y = np.array(y)

model = Sequential()

# allow first layer to use sigmoid. (gives better results)
model.add(Dense(10, input_dim=2, init="uniform", activation="sigmoid"))

#perform dropout of neurons at 0.4 threshold
model.add(Dropout(0.4))

# only use relu in middle layer
model.add(Dense(8, init="uniform", activation="relu"))

# also dropout neurons if below 0.3
model.add(Dropout(0.3))

model.add(Dense(1, init="uniform", activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x, y, nb_epoch=150, batch_size=10)

del dataset
with open("./blue_red_sample_2.csv",newline='') as csvfile:
	f_read = csv.reader(csvfile, delimiter=',')
	dataset = []
	for row in f_read:
		dataset.append(np.array(row))

dataset = np.array(dataset)

x2 = dataset[:,1:3]
y2 = dataset[:,0]
y2 = [1.0 if "blue" in x else 0.0 for x in y2]
y2 = np.array(y2)

print("\nevaluating data that the model was trained on.")
scores = model.evaluate(x, y, batch_size=32)
print("\n{0}: {1}".format(model.metrics_names[1], scores[1]*100))
print("{0}: {1}\n".format(model.metrics_names[0], scores[0]*100))

print("\nevaluating new random data that the model hasn't seen.")
scores = model.evaluate(x2, y2, batch_size=32)
print("\n{0}: {1}".format(model.metrics_names[1], scores[1]*100))
print("{0}: {1}\n".format(model.metrics_names[0], scores[0]*100))

print("predict 34")
print(model.predict(x[34].reshape(1,2)))
print("actual value {0}\n".format(y[34]))

print("predict 35")
print(model.predict(x[35].reshape(1,2)))
print("actual value {0}".format(y[35]))

predict_array = model.predict(x)

print("\nPrinting predicted values 0-100 to file br_results.txt")
with open("br_results.txt","w") as new_file:
	for val in predict_array:
		new_file.write("{0}\n".format(val[0]))

