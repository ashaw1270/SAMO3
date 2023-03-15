import csv
from tensorflow import keras
import numpy as np

# import csv files and convert to numpy arrays
with open(file='Training_X.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    x_train = np.float_(list(reader))

with open(file='Training_Y.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    y_train = np.float_(list(reader))

with open(file='Tests_X.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    x_test = np.float_(list(reader))

with open(file='Tests_Y.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    y_test = np.float_(list(reader))

# create the model
model = keras.Sequential([
    keras.layers.Dense(units=2, activation='sigmoid', input_shape=(2,)),
    keras.layers.Dense(units=128, activation='sigmoid'),
    keras.layers.Dense(units=2, activation='softmax')
])

# compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['binary_accuracy'])

# train the model
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# evaluate the model on the test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)
